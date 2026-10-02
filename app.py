import os
import sqlite3
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'cit-devops-campus-placement-2026')

# Resolve database path for both local execution and Docker persistent container mount
DB_DIR = os.environ.get('DATA_DIR', '/app/data' if os.path.exists('/app') else 'data')
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, 'placement.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Placement drives table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS drives (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            ctc TEXT NOT NULL,
            eligibility_cgpa REAL NOT NULL,
            location TEXT NOT NULL,
            deadline TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    
    # Student applications table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            drive_id INTEGER NOT NULL,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            student_name TEXT NOT NULL,
            roll_no TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            status TEXT DEFAULT 'Applied',
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (drive_id) REFERENCES drives(id)
        )
    ''')
    
    # Populate default campus placement drives if empty
    cursor.execute('SELECT COUNT(*) FROM drives')
    if cursor.fetchone()[0] == 0:
        default_drives = [
            ('Google Cloud', 'Cloud Solutions Architect', '32 LPA', 8.5, 'Bengaluru / Hyderabad', '15 Oct 2026', 'Design and scale cloud architectures on GCP for enterprise clients.', 'Product'),
            ('Microsoft India', 'Software Development Engineer (SDE)', '28 LPA', 8.0, 'Hyderabad / Noida', '18 Oct 2026', 'Develop distributed backend microservices and modern cloud applications.', 'Product'),
            ('Amazon Web Services', 'DevOps & Systems Engineer', '26 LPA', 7.5, 'Chennai / Bengaluru', '20 Oct 2026', 'Automate CI/CD pipelines, container orchestration, and multi-region infrastructure.', 'Product'),
            ('Zoho Corporation', 'Product Developer', '12 LPA', 7.0, 'Coimbatore / Chennai', '22 Oct 2026', 'Build scalable SaaS modules using Python, Java, and modern web frameworks.', 'Product'),
            ('TCS Digital', 'Systems Engineer (DevOps & Cloud)', '7.5 LPA', 6.5, 'Pan India', '25 Oct 2026', 'Implement automated build pipelines, container deployments, and quality gates.', 'Services'),
            ('Cognizant GenC Next', 'Cloud DevOps Specialist', '6.8 LPA', 6.5, 'Coimbatore / Chennai', '28 Oct 2026', 'Continuous integration, container orchestration, and automated test automation.', 'Services')
        ]
        cursor.executemany('''
            INSERT INTO drives (company, role, ctc, eligibility_cgpa, location, deadline, description, category)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', default_drives)
        
        # Seed an initial student application record for verification
        cursor.execute('''
            INSERT INTO applications (drive_id, company, role, student_name, roll_no, department, cgpa, email, phone, status)
            VALUES (1, 'Google Cloud', 'Cloud Solutions Architect', 'Ishu Pathak', '2303717620521021', 'Information Technology', 8.9, 'ishupathak@cit.edu.in', '+91 9876543210', 'Shortlisted')
        ''')
        
    conn.commit()
    conn.close()

# Initialize DB on module startup
init_db()

@app.route('/')
def home():
    """Main student view: lists all placement drives and allows filtering/applying."""
    conn = get_db()
    category = request.args.get('category', 'All')
    search = request.args.get('search', '').strip()
    
    query = 'SELECT * FROM drives WHERE 1=1'
    params = []
    
    if category != 'All':
        query += ' AND category = ?'
        params.append(category)
        
    if search:
        query += ' AND (company LIKE ? OR role LIKE ? OR location LIKE ?)'
        like_term = f'%{search}%'
        params.extend([like_term, like_term, like_term])
        
    query += ' ORDER BY id ASC'
    drives = conn.execute(query, params).fetchall()
    
    # Total counts for stat banner
    total_drives = conn.execute('SELECT COUNT(*) FROM drives').fetchone()[0]
    total_apps = conn.execute('SELECT COUNT(*) FROM applications').fetchone()[0]
    conn.close()
    
    return render_template('index.html', drives=drives, selected_category=category, search=search, total_drives=total_drives, total_apps=total_apps)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """REST API endpoint returning active placement drives."""
    conn = get_db()
    drives = conn.execute('SELECT * FROM drives ORDER BY id ASC').fetchall()
    conn.close()
    return jsonify([dict(drive) for drive in drives])

@app.route('/api/apply', methods=['POST'])
def apply_job():
    """Handle student job application submission."""
    data = request.get_json() if request.is_json else request.form
    
    drive_id = data.get('drive_id')
    student_name = data.get('student_name', '').strip()
    roll_no = data.get('roll_no', '').strip()
    department = data.get('department', '').strip()
    cgpa = float(data.get('cgpa', 0))
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    
    if not (drive_id and student_name and roll_no and email):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
        
    conn = get_db()
    drive = conn.execute('SELECT * FROM drives WHERE id = ?', (drive_id,)).fetchone()
    if not drive:
        conn.close()
        return jsonify({'success': False, 'message': 'Placement drive not found'}), 404
        
    # Enforce minimum eligibility CGPA cutoff
    if cgpa < drive['eligibility_cgpa']:
        conn.close()
        if request.is_json:
            return jsonify({
                'success': False,
                'message': f'Your CGPA ({cgpa}) does not meet the minimum eligibility requirement of {drive["eligibility_cgpa"]} for {drive["company"]}.'
            }), 400
        return redirect(url_for('home', error='cgpa_cutoff', min_cgpa=drive['eligibility_cgpa']))
        
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO applications (drive_id, company, role, student_name, roll_no, department, cgpa, email, phone, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Applied')
    ''', (drive_id, drive['company'], drive['role'], student_name, roll_no, department, cgpa, email, phone))
    
    app_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    if request.is_json:
        return jsonify({'success': True, 'application_id': app_id, 'message': 'Application submitted successfully'}), 201
    return redirect(url_for('home', applied='success', app_id=app_id))

@app.route('/admin')
def admin():
    """Placement Officer / Faculty Review Dashboard."""
    conn = get_db()
    applications = conn.execute('SELECT * FROM applications ORDER BY id DESC').fetchall()
    drives = conn.execute('SELECT * FROM drives ORDER BY id ASC').fetchall()
    
    stats = {
        'total': conn.execute('SELECT COUNT(*) FROM applications').fetchone()[0],
        'shortlisted': conn.execute("SELECT COUNT(*) FROM applications WHERE status='Shortlisted'").fetchone()[0],
        'selected': conn.execute("SELECT COUNT(*) FROM applications WHERE status='Selected'").fetchone()[0],
        'drives_count': conn.execute('SELECT COUNT(*) FROM drives').fetchone()[0]
    }
    conn.close()
    
    return render_template('admin.html', applications=applications, drives=drives, stats=stats)

@app.route('/api/status', methods=['POST'])
def update_status():
    """Update candidate application status from TPO dashboard."""
    data = request.get_json() if request.is_json else request.form
    app_id = data.get('application_id')
    new_status = data.get('status')
    
    if not (app_id and new_status):
        return jsonify({'success': False, 'message': 'Missing application_id or status'}), 400
        
    conn = get_db()
    conn.execute('UPDATE applications SET status = ? WHERE id = ?', (new_status, app_id))
    conn.commit()
    conn.close()
    return jsonify({'success': True, 'message': f'Application #{app_id} status updated to {new_status}'})

@app.route('/health')
def health():
    """Health check endpoint used by Docker and CI/CD pipelines."""
    try:
        conn = get_db()
        conn.execute('SELECT 1').fetchone()
        conn.close()
        db_status = 'Connected'
    except Exception as e:
        db_status = f'Error: {str(e)}'
        
    return jsonify({
        'status': 'healthy',
        'service': 'Campus Placement Management System',
        'institution': 'Coimbatore Institute of Technology',
        'course': '23IT723 - DevOps Laboratory',
        'database': db_status,
        'storage_path': DB_PATH
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
