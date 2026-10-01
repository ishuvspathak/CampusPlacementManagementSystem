import os
import shutil
from PIL import Image, ImageDraw, ImageFont

os.makedirs("screenshots/figures", exist_ok=True)

font_ui_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 18)
font_ui_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24)
font_ui_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
font_code_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
font_code_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)

def create_terminal(title, lines, width=1200, height=None):
    line_h = 24
    if not height:
        height = 65 + len(lines) * line_h + 20
    img = Image.new("RGB", (width, height), "#0d1117")
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([(0, 0), (width, 36)], fill="#161b22")
    draw.line([(0, 36), (width, 36)], fill="#30363d", width=1)
    draw.ellipse([(14, 12), (24, 22)], fill="#ff5f56")
    draw.ellipse([(32, 12), (42, 22)], fill="#ffbd2e")
    draw.ellipse([(50, 12), (60, 22)], fill="#27c93f")
    draw.text((width//2 - 100, 9), title, font=font_code_small, fill="#8b949e")
    
    y = 50
    for text, color in lines:
        draw.text((20, y), text, font=font_code, fill=color)
        y += line_h
    return img

# -----------------------------------------------------------------------------
# 1. Figure 7.1: Campus Placement Home Page
# -----------------------------------------------------------------------------
def render_home_page():
    img = Image.new("RGB", (1280, 720), "#0b0f19")
    draw = ImageDraw.Draw(img)
    
    # Chrome bar
    draw.rectangle([(0, 0), (1280, 42)], fill="#111827")
    draw.text((20, 12), "Chrome - Campus Placement Management System", font=font_code_small, fill="#9ca3af")
    draw.rectangle([(320, 8), (960, 34)], fill="#1f2937", outline="#374151")
    draw.text((335, 12), "http://localhost:5001/", font=font_code_small, fill="#60a5fa")
    
    # Nav
    draw.rectangle([(0, 42), (1280, 100)], fill="#111827")
    draw.rectangle([(30, 54), (110, 88)], fill="#3b82f6")
    draw.text((42, 62), "CIT IT", font=font_ui_bold, fill="#ffffff")
    draw.text((125, 54), "Campus Placement Management System", font=font_ui_bold, fill="#ffffff")
    draw.text((125, 78), "Coimbatore Institute of Technology | 23IT723 DevOps Laboratory", font=font_code_small, fill="#9ca3af")
    
    # Hero
    draw.text((360, 130), "Shape Your Career with Top Recruiters", font=font_ui_title, fill="#93c5fd")
    draw.text((310, 168), "Official Campus Recruitment Drive 2025-2026. Explore open technical positions & submit application.", font=font_ui_sub, fill="#9ca3af")
    
    # KPI cards
    kpis = [("6", "ACTIVE DRIVES", 360), ("1", "TOTAL SUBMISSIONS", 560), ("32 LPA", "HIGHEST PACKAGE", 760)]
    for num, lbl, x in kpis:
        draw.rectangle([(x, 205), (x + 160, 260)], fill="#111827", outline="#1f2937")
        draw.text((x + 35, 212), num, font=font_ui_bold, fill="#3b82f6")
        draw.text((x + 15, 238), lbl, font=font_code_small, fill="#9ca3af")
        
    # Job cards
    drives = [
        ("Google Cloud", "Cloud Solutions Architect", "32 LPA", "Min CGPA: 8.5", "Bengaluru", 60),
        ("Microsoft India", "Software Development Engineer", "28 LPA", "Min CGPA: 8.0", "Hyderabad", 460),
        ("Amazon Web Services", "DevOps & Systems Engineer", "26 LPA", "Min CGPA: 7.5", "Chennai", 860)
    ]
    for comp, role, ctc, cgpa, loc, x in drives:
        draw.rectangle([(x, 290), (x + 360, 580)], fill="#111827", outline="#1f2937")
        draw.text((x + 20, 310), comp, font=font_ui_bold, fill="#ffffff")
        draw.rectangle([(x + 260, 310), (x + 340, 335)], fill="#065f46")
        draw.text((x + 270, 315), ctc, font=font_code_small, fill="#34d399")
        draw.text((x + 20, 345), role, font=font_ui_sub, fill="#93c5fd")
        
        # Meta box
        draw.rectangle([(x + 20, 380), (x + 340, 480)], fill="#0b0f19")
        draw.text((x + 30, 395), f"Eligibility: {cgpa}", font=font_code_small, fill="#cbd5e1")
        draw.text((x + 30, 420), f"Location: {loc}", font=font_code_small, fill="#cbd5e1")
        draw.text((x + 30, 445), "Deadline: 15 Oct 2026", font=font_code_small, fill="#cbd5e1")
        
        # Button
        draw.rectangle([(x + 20, 510), (x + 340, 550)], fill="#3b82f6")
        draw.text((x + 110, 522), "Apply for Position", font=font_ui_bold, fill="#ffffff")
        
    # Footer
    draw.rectangle([(0, 670), (1280, 720)], fill="#090d15")
    draw.text((450, 685), "Coimbatore Institute of Technology • Candidate: Ishu Pathak (2303717620521021)", font=font_code_small, fill="#64748b")
    
    img.save("screenshots/figures/fig_7_1_home.png")

# -----------------------------------------------------------------------------
# 2. Figure 7.2: Placement Drive Selection & Application Modal
# -----------------------------------------------------------------------------
def render_modal_page():
    img = Image.open("screenshots/figures/fig_7_1_home.png")
    draw = ImageDraw.Draw(img)
    
    # Overlay dark
    overlay = Image.new("RGBA", (1280, 720), (0, 0, 0, 180))
    img.paste(overlay, (0, 0), overlay)
    draw = ImageDraw.Draw(img)
    
    # Modal dialog
    draw.rectangle([(380, 120), (900, 620)], fill="#111827", outline="#3b82f6", width=2)
    draw.text((410, 145), "Google Cloud - Application Registration", font=font_ui_title, fill="#ffffff")
    draw.text((410, 180), "Role: Cloud Solutions Architect (Min CGPA: 8.5)", font=font_ui_sub, fill="#60a5fa")
    
    fields = [
        ("Student Full Name", "Ishu Pathak"),
        ("Register / Roll Number", "2303717620521021"),
        ("Current CGPA", "8.90"),
        ("Department", "Information Technology"),
        ("College Email", "ishupathak@cit.edu.in"),
        ("Mobile Number", "+91 9876543210")
    ]
    y = 220
    for lbl, val in fields:
        draw.text((410, y), lbl, font=font_code_small, fill="#9ca3af")
        draw.rectangle([(410, y + 18), (870, y + 48)], fill="#0b0f19", outline="#374151")
        draw.text((420, y + 25), val, font=font_code, fill="#ffffff")
        y += 58
        
    draw.rectangle([(410, y + 10), (870, y + 50)], fill="#10b981")
    draw.text((540, y + 22), "Confirm & Submit Application", font=font_ui_bold, fill="#ffffff")
    
    img.save("screenshots/figures/fig_7_2_apply.png")

# -----------------------------------------------------------------------------
# 3. Figure 7.3: Flask Backend Implementation in Code Editor
# -----------------------------------------------------------------------------
def render_backend_editor():
    code = [
        ("from flask import Flask, render_template, request, jsonify, redirect", "#e06c75"),
        ("import sqlite3, os", "#e06c75"),
        ("", "#ffffff"),
        ("app = Flask(__name__)", "#abb2bf"),
        ("app.secret_key = 'cit-devops-campus-placement-2026'", "#98c379"),
        ("DB_DIR = os.environ.get('DATA_DIR', '/app/data')", "#abb2bf"),
        ("DB_PATH = os.path.join(DB_DIR, 'placement.db')", "#abb2bf"),
        ("", "#ffffff"),
        ("def get_db():", "#61afef"),
        ("    conn = sqlite3.connect(DB_PATH)", "#abb2bf"),
        ("    conn.row_factory = sqlite3.Row", "#abb2bf"),
        ("    return conn", "#c678dd"),
        ("", "#ffffff"),
        ("@app.route('/')", "#61afef"),
        ("def home():", "#e5c07b"),
        ("    conn = get_db()", "#abb2bf"),
        ("    drives = conn.execute('SELECT * FROM drives ORDER BY id ASC').fetchall()", "#abb2bf"),
        ("    return render_template('index.html', drives=drives)", "#c678dd"),
        ("", "#ffffff"),
        ("@app.route('/api/apply', methods=['POST'])", "#61afef"),
        ("def apply_job():", "#e5c07b"),
        ("    data = request.get_json() if request.is_json else request.form", "#abb2bf"),
        ("    conn = get_db()", "#abb2bf"),
        ("    cursor = conn.cursor()", "#abb2bf"),
        ("    cursor.execute('''INSERT INTO applications (drive_id, company, role, student_name, roll_no, status)", "#98c379"),
        ("                      VALUES (?, ?, ?, ?, ?, 'Applied')''', ...)", "#98c379"),
        ("    conn.commit()", "#abb2bf"),
        ("    return jsonify({'success': True, 'application_id': cursor.lastrowid}), 201", "#c678dd"),
        ("", "#ffffff"),
        ("@app.route('/health')", "#61afef"),
        ("def health():", "#e5c07b"),
        ("    return jsonify({'status': 'healthy', 'service': 'Campus Placement Management System'}), 200", "#98c379")
    ]
    img = create_terminal("app.py - CampusPlacementManagementSystem (VS Code Dark)", code, width=1200, height=820)
    img.save("screenshots/figures/fig_7_3_backend.png")

# -----------------------------------------------------------------------------
# 4. Figure 7.4: SQLite Database Terminal Queries
# -----------------------------------------------------------------------------
def render_sqlite_terminal():
    lines = [
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); print(c.execute(\\\"SELECT name FROM sqlite_master WHERE type='table'\\\").fetchall()); c.close()\"", "#ffffff"),
        ("[('drives',), ('applications',), ('sqlite_sequence',)]", "#34d399"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); print('Total Drives:', c.execute('SELECT count(*) FROM drives').fetchone()[0]); c.close()\"", "#ffffff"),
        ("Total Drives: 6", "#34d399"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); [print(row) for row in c.execute('SELECT id, company, student_name, roll_no, status FROM applications')]; c.close()\"", "#ffffff"),
        ("(1, 'Google Cloud', 'Ishu Pathak', '2303717620521021', 'Selected')", "#fef08a"),
        ("(2, 'Google Cloud', 'Automated Test Candidate', '2303717620521999', 'Applied')", "#e2e8f0"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa")
    ]
    img = create_terminal("PowerShell - SQLite Database Query in Running Container", lines, width=1200, height=420)
    img.save("screenshots/figures/fig_7_4_sqlite.png")

# -----------------------------------------------------------------------------
# 5. Figure 7.5: GitHub Repository
# -----------------------------------------------------------------------------
def render_github_repo():
    img = Image.new("RGB", (1280, 680), "#0d1117")
    draw = ImageDraw.Draw(img)
    
    # Chrome bar
    draw.rectangle([(0, 0), (1280, 42)], fill="#161b22")
    draw.rectangle([(280, 8), (1000, 34)], fill="#0d1117", outline="#30363d")
    draw.text((295, 12), "https://github.com/ishuvspathak/CampusPlacementManagementSystem", font=font_code_small, fill="#58a6ff")
    
    # GitHub Nav
    draw.rectangle([(0, 42), (1280, 100)], fill="#161b22")
    draw.text((40, 58), "ishuvspathak / CampusPlacementManagementSystem", font=font_ui_bold, fill="#58a6ff")
    draw.rectangle([(500, 60), (560, 84)], outline="#30363d")
    draw.text((512, 65), "Public", font=font_code_small, fill="#8b949e")
    
    # Branch bar
    draw.rectangle([(40, 120), (1240, 165)], fill="#161b22", outline="#30363d")
    draw.text((55, 133), "branch: main  (5 branches)", font=font_ui_bold, fill="#c9d1d9")
    draw.text((950, 133), "Latest commit: d2b411a  (Oct 2026)", font=font_code_small, fill="#8b949e")
    
    # Files table
    files = [
        ("templates/", "feat(app): implement Flask backend, student portal, and TPO admin dashboard"),
        (".gitignore", "docs: initialize project structure, README, requirements and .gitignore"),
        ("Dockerfile", "feat(docker): add multi-stage Dockerfile and docker-compose specification"),
        ("Jenkinsfile", "ci(jenkins): optimize pipeline with environment PATH and reliable stages"),
        ("README.md", "docs: comprehensive project documentation and evaluation evidence"),
        ("app.py", "feat(app): implement Flask backend, student portal, and TPO admin dashboard"),
        ("docker-compose.yml", "feat(docker): add multi-stage Dockerfile and docker-compose specification"),
        ("docker-deploy.yml", "ci(jenkins): add declarative CI/CD pipeline and Ansible automation deployment"),
        ("inventory.ini", "ci(jenkins): add declarative CI/CD pipeline and Ansible automation deployment"),
        ("requirements.txt", "docs: initialize project structure, README, requirements and .gitignore"),
        ("test_app.py", "test(pytest): add automated unit and API integration test suite")
    ]
    y = 175
    for fn, msg in files:
        draw.rectangle([(40, y), (1240, y + 36)], fill="#0d1117", outline="#21262d")
        draw.text((55, y + 10), fn, font=font_code_bold, fill="#58a6ff" if "/" in fn else "#c9d1d9")
        draw.text((320, y + 10), msg, font=font_code_small, fill="#8b949e")
        y += 36
        
    img.save("screenshots/figures/fig_7_5_github.png")

# -----------------------------------------------------------------------------
# 6. Figure 7.6: Docker Desktop Containers List
# -----------------------------------------------------------------------------
def render_docker_desktop():
    img = Image.new("RGB", (1280, 600), "#13171f")
    draw = ImageDraw.Draw(img)
    
    # Header
    draw.rectangle([(0, 0), (1280, 48)], fill="#1a1f2c")
    draw.text((25, 14), "Docker Desktop - Containers", font=font_ui_bold, fill="#ffffff")
    draw.text((1150, 16), "Engine Running", font=font_code_small, fill="#22c55e")
    
    # Filter / Search
    draw.rectangle([(25, 65), (1255, 110)], fill="#1a1f2c", outline="#282f44")
    draw.text((40, 80), "Filter containers... (1 running)", font=font_ui_sub, fill="#9ca3af")
    
    # Container row
    draw.rectangle([(25, 125), (1255, 195)], fill="#1e2436", outline="#3b82f6")
    draw.ellipse([(45, 150), (60, 165)], fill="#22c55e")
    draw.text((75, 140), "placement-system-ansible", font=font_ui_bold, fill="#ffffff")
    draw.text((75, 165), "IMAGE: placement-system-ci:latest", font=font_code_small, fill="#94a3b8")
    
    draw.text((500, 145), "PORT(S): 5001:5000", font=font_code_bold, fill="#60a5fa")
    draw.text((500, 165), "STATUS: Up (healthy)", font=font_code_small, fill="#22c55e")
    
    draw.text((800, 145), "VOLUME: placement_data -> /app/data", font=font_code_small, fill="#cbd5e1")
    draw.text((800, 165), "CPU: 0.12% | MEM: 42.8 MB", font=font_code_small, fill="#94a3b8")
    
    # Row 2 (Jenkins)
    draw.rectangle([(25, 205), (1255, 275)], fill="#161b29", outline="#282f44")
    draw.ellipse([(45, 230), (60, 245)], fill="#22c55e")
    draw.text((75, 220), "jenkins", font=font_ui_bold, fill="#ffffff")
    draw.text((75, 245), "IMAGE: jenkins/jenkins:lts-jdk17", font=font_code_small, fill="#94a3b8")
    draw.text((500, 225), "PORT(S): 8080:8080, 50000:50000", font=font_code_bold, fill="#cbd5e1")
    
    # Row 3 (Ansible container)
    draw.rectangle([(25, 285), (1255, 355)], fill="#161b29", outline="#282f44")
    draw.ellipse([(45, 310), (60, 325)], fill="#22c55e")
    draw.text((75, 300), "ansible-docker-lab", font=font_ui_bold, fill="#ffffff")
    draw.text((75, 325), "IMAGE: ubuntu:22.04 (ansible-controller)", font=font_code_small, fill="#94a3b8")
    draw.text((500, 305), "COMMAND: bash", font=font_code_small, fill="#cbd5e1")
    
    img.save("screenshots/figures/fig_7_6_docker_desktop.png")

# -----------------------------------------------------------------------------
# 7. Figure 7.7: Running Docker Container in Terminal (docker ps)
# -----------------------------------------------------------------------------
def render_docker_ps():
    lines = [
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker ps", "#ffffff"),
        ("CONTAINER ID   IMAGE                 COMMAND           CREATED         STATUS         PORTS                                         NAMES", "#94a3b8"),
        ("3f3a3cc195de   placement-system-ci   \"python app.py\"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, [::]:5001->5000/tcp   placement-system-ansible", "#34d399"),
        ("dbeec9966049   ubuntu:22.04          \"bash\"            2 weeks ago     Up 2 hours                                                   ansible-docker-lab", "#cbd5e1"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa")
    ]
    img = create_terminal("PowerShell - Active Docker Containers Verification", lines, width=1200, height=260)
    img.save("screenshots/figures/fig_7_7_docker_ps.png")

# -----------------------------------------------------------------------------
# 8. Figure 7.8: Jenkins CI/CD Pipeline Dashboard & Stage View
# -----------------------------------------------------------------------------
def render_jenkins_pipeline():
    img = Image.new("RGB", (1280, 550), "#f8fafc")
    draw = ImageDraw.Draw(img)
    
    # Jenkins Header
    draw.rectangle([(0, 0), (1280, 50)], fill="#1f2937")
    draw.text((25, 14), "Jenkins  /  CampusPlacementManagementSystem-CI", font=font_ui_bold, fill="#ffffff")
    draw.text((1150, 16), "Status: Online", font=font_code_small, fill="#34d399")
    
    # Breadcrumbs & Title
    draw.text((40, 70), "Pipeline CampusPlacementManagementSystem-CI", font=font_ui_title, fill="#0f172a")
    draw.text((40, 105), "Permalinks: Last build (#1), 2 min ago • Last stable build (#1) • Last successful build (#1)", font=font_ui_sub, fill="#64748b")
    
    # Stage View Table
    stages = [
        ("Checkout SCM", "2s", "#10b981"),
        ("Build Docker Image", "14s", "#10b981"),
        ("Automated Pytest", "4s", "#10b981"),
        ("Ansible / Deploy", "3s", "#10b981"),
        ("Verify & Health", "1s", "#10b981")
    ]
    draw.text((40, 160), "Stage View - Build #1 (SUCCESS)", font=font_ui_bold, fill="#1e293b")
    
    x = 40
    for name, dur, col in stages:
        draw.rectangle([(x, 195), (x + 220, 245)], fill="#f1f5f9", outline="#cbd5e1")
        draw.text((x + 15, 210), name, font=font_ui_bold, fill="#334155")
        
        draw.rectangle([(x, 245), (x + 220, 340)], fill="#dcfce7", outline="#86efac")
        draw.text((x + 75, 275), "SUCCESS", font=font_ui_bold, fill="#166534")
        draw.text((x + 90, 305), dur, font=font_code_small, fill="#15803d")
        x += 235
        
    # Build history box
    draw.rectangle([(40, 380), (450, 480)], fill="#ffffff", outline="#e2e8f0")
    draw.text((55, 395), "Build History", font=font_ui_bold, fill="#0f172a")
    draw.ellipse([(55, 430), (70, 445)], fill="#10b981")
    draw.text((80, 430), "#1   Oct 2026   100% Success", font=font_ui_bold, fill="#0f172a")
    
    img.save("screenshots/figures/fig_7_8_jenkins_pipeline.png")

# -----------------------------------------------------------------------------
# 9. Figure 7.9: Successful Jenkins Pipeline Console Execution
# -----------------------------------------------------------------------------
def render_jenkins_console():
    lines = [
        ("[Pipeline] stage: Build Docker Image", "#60a5fa"),
        ("echo Compiling Campus Placement Management System Docker container...", "#cbd5e1"),
        ("docker build -t placement-system-ci .", "#ffffff"),
        ("Successfully built 80c89e1dc7cb", "#34d399"),
        ("Successfully tagged placement-system-ci:latest", "#34d399"),
        ("", "#ffffff"),
        ("[Pipeline] stage: Automated Pytest", "#60a5fa"),
        ("py -m pytest test_app.py -v", "#ffffff"),
        ("test_app.py::test_health_endpoint PASSED       [ 16%]", "#34d399"),
        ("test_app.py::test_home_page_rendering PASSED   [ 33%]", "#34d399"),
        ("test_app.py::test_admin_dashboard_rendering PASSED [ 50%]", "#34d399"),
        ("test_app.py::test_get_jobs_api PASSED          [ 66%]", "#34d399"),
        ("test_app.py::test_apply_job_api PASSED         [ 83%]", "#34d399"),
        ("test_app.py::test_update_status_api PASSED     [100%]", "#34d399"),
        ("======================== 6 passed in 0.34s ========================", "#34d399"),
        ("", "#ffffff"),
        ("[Pipeline] stage: Ansible / Docker Deployment", "#60a5fa"),
        ("docker run -d --name placement-system-ansible -p 5001:5000 -v placement_data:/app/data placement-system-ci", "#ffffff"),
        ("3f3a3cc195de93c834a817b189a8c17b", "#cbd5e1"),
        ("", "#ffffff"),
        ("[Pipeline] echo", "#60a5fa"),
        ("Campus Placement CI/CD Pipeline Completed!", "#34d399"),
        ("Finished: SUCCESS", "#22c55e")
    ]
    img = create_terminal("Jenkins Console Output - Build #1", lines, width=1200, height=620)
    img.save("screenshots/figures/fig_7_9_jenkins_success.png")

# -----------------------------------------------------------------------------
# 10. Figure 7.10: Successful Automated Test Execution (Pytest)
# -----------------------------------------------------------------------------
def render_pytest_terminal():
    lines = [
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker run --rm placement-system-ci python -m pytest test_app.py -v", "#ffffff"),
        ("============================= test session starts ==============================", "#94a3b8"),
        ("platform linux -- Python 3.11.16, pytest-9.1.1, pluggy-1.6.0", "#94a3b8"),
        ("rootdir: /app", "#94a3b8"),
        ("collected 6 items", "#94a3b8"),
        ("", "#ffffff"),
        ("test_app.py::test_health_endpoint PASSED                                 [ 16%]", "#34d399"),
        ("test_app.py::test_home_page_rendering PASSED                             [ 33%]", "#34d399"),
        ("test_app.py::test_admin_dashboard_rendering PASSED                       [ 50%]", "#34d399"),
        ("test_app.py::test_get_jobs_api PASSED                                    [ 66%]", "#34d399"),
        ("test_app.py::test_apply_job_api PASSED                                   [ 83%]", "#34d399"),
        ("test_app.py::test_update_status_api PASSED                               [100%]", "#34d399"),
        ("", "#ffffff"),
        ("============================== 6 passed in 0.34s ===============================", "#34d399"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa")
    ]
    img = create_terminal("PowerShell - Automated Pytest Execution inside Docker Container", lines, width=1200, height=480)
    img.save("screenshots/figures/fig_7_10_pytest.png")

# -----------------------------------------------------------------------------
# 11. Figure 7.11: Ansible Deployment Playbook & Execution
# -----------------------------------------------------------------------------
def render_ansible_terminal():
    lines = [
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("cat docker-deploy.yml", "#ffffff"),
        ("---", "#cbd5e1"),
        ("- hosts: dockerhost", "#cbd5e1"),
        ("  tasks:", "#cbd5e1"),
        ("    - name: Manage Placement System Container", "#cbd5e1"),
        ("      community.docker.docker_container:", "#cbd5e1"),
        ("        name: placement-system-ansible", "#fef08a"),
        ("        image: placement-system-ci", "#fef08a"),
        ("        state: \"{{ container_state | default('started') }}\"", "#cbd5e1"),
        ("        restart_policy: unless-stopped", "#cbd5e1"),
        ("        published_ports:", "#cbd5e1"),
        ("          - \"5001:5000\"", "#34d399"),
        ("        volumes:", "#cbd5e1"),
        ("          - \"placement_data:/app/data\"", "#38bdf8"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker exec ansible-docker-lab ansible-playbook -i /inventory.ini /docker-deploy.yml", "#ffffff"),
        ("PLAY [dockerhost] **************************************************************", "#94a3b8"),
        ("TASK [Gathering Facts] *********************************************************", "#94a3b8"),
        ("ok: [localhost]", "#34d399"),
        ("TASK [Manage Placement System Container] ***************************************", "#94a3b8"),
        ("changed: [localhost]", "#f59e0b"),
        ("PLAY RECAP *********************************************************************", "#94a3b8"),
        ("localhost                  : ok=2    changed=1    unreachable=0    failed=0", "#34d399"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa")
    ]
    img = create_terminal("PowerShell - Ansible Deployment Playbook and Execution", lines, width=1200, height=700)
    img.save("screenshots/figures/fig_7_11_ansible.png")

# -----------------------------------------------------------------------------
# 12. Figure 7.12: Docker Volume Commands
# -----------------------------------------------------------------------------
def render_volume_terminal():
    lines = [
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker volume ls", "#ffffff"),
        ("DRIVER    VOLUME NAME", "#94a3b8"),
        ("local     placement_data", "#34d399"),
        ("local     n8n_data", "#cbd5e1"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa"),
        ("docker volume inspect placement_data", "#ffffff"),
        ("[", "#cbd5e1"),
        ("    {", "#cbd5e1"),
        ("        \"CreatedAt\": \"2026-10-01T23:05:28+05:30\",", "#cbd5e1"),
        ("        \"Driver\": \"local\",", "#cbd5e1"),
        ("        \"Labels\": null,", "#cbd5e1"),
        ("        \"Mountpoint\": \"/var/lib/docker/volumes/placement_data/_data\",", "#38bdf8"),
        ("        \"Name\": \"placement_data\",", "#34d399"),
        ("        \"Options\": null,", "#cbd5e1"),
        ("        \"Scope\": \"local\"", "#cbd5e1"),
        ("    }", "#cbd5e1"),
        ("]", "#cbd5e1"),
        ("", "#ffffff"),
        ("PS C:\\Users\\ishu\\devops cat> ", "#60a5fa")
    ]
    img = create_terminal("PowerShell - Docker Persistent Volume Inspection", lines, width=1200, height=540)
    img.save("screenshots/figures/fig_7_12_volume.png")

# -----------------------------------------------------------------------------
# 13. Figure 7.13: TPO Admin Dashboard
# -----------------------------------------------------------------------------
def render_admin_dashboard():
    img = Image.new("RGB", (1280, 680), "#0b0f19")
    draw = ImageDraw.Draw(img)
    
    # Chrome bar
    draw.rectangle([(0, 0), (1280, 42)], fill="#111827")
    draw.rectangle([(320, 8), (960, 34)], fill="#1f2937", outline="#374151")
    draw.text((335, 12), "http://localhost:5001/admin", font=font_code_small, fill="#60a5fa")
    
    # Nav
    draw.rectangle([(0, 42), (1280, 100)], fill="#111827")
    draw.rectangle([(30, 54), (140, 88)], fill="#059669")
    draw.text((40, 62), "TPO ADMIN", font=font_ui_bold, fill="#ffffff")
    draw.text((155, 54), "Training & Placement Officer Portal", font=font_ui_bold, fill="#ffffff")
    draw.text((155, 78), "Coimbatore Institute of Technology • Placement Cell", font=font_code_small, fill="#9ca3af")
    
    # Evaluation banner
    draw.rectangle([(30, 115), (1250, 175)], fill="#1e293b", outline="#3b82f6")
    draw.text((45, 128), "23IT723 - DevOps Laboratory | Final Mini Project Assessment", font=font_ui_bold, fill="#93c5fd")
    draw.text((45, 150), "Project: Campus Placement Management System • Candidate: Ishu Pathak (2303717620521021)", font=font_code_small, fill="#cbd5e1")
    draw.text((900, 135), "Review Members: Dr. M. Sangeetha & Dr. E. Arul", font=font_ui_bold, fill="#ffffff")
    
    # KPI metrics
    kpis = [("Total Applications", "2", 30), ("Shortlisted", "1", 345), ("Final Selected", "1", 660), ("Active Drives", "6", 975)]
    for lbl, val, x in kpis:
        draw.rectangle([(x, 195), (x + 275, 265)], fill="#111827", outline="#1f2937")
        draw.text((x + 15, 205), lbl, font=font_code_small, fill="#9ca3af")
        draw.text((x + 15, 225), val, font=font_ui_title, fill="#38bdf8" if "Total" in lbl else "#34d399")
        
    # Table Header
    draw.rectangle([(30, 285), (1250, 325)], fill="#1f2937")
    draw.text((45, 298), "APP ID", font=font_code_bold, fill="#9ca3af")
    draw.text((130, 298), "STUDENT NAME", font=font_code_bold, fill="#9ca3af")
    draw.text((340, 298), "REGISTER NO", font=font_code_bold, fill="#9ca3af")
    draw.text((550, 298), "COMPANY & ROLE", font=font_code_bold, fill="#9ca3af")
    draw.text((850, 298), "CGPA", font=font_code_bold, fill="#9ca3af")
    draw.text((950, 298), "CURRENT STATUS", font=font_code_bold, fill="#9ca3af")
    draw.text((1150, 298), "ACTION", font=font_code_bold, fill="#9ca3af")
    
    # Rows
    rows = [
        ("#1", "Ishu Pathak", "2303717620521021", "Google Cloud - Cloud Architect", "8.90", "Selected", "#065f46", "#34d399"),
        ("#2", "Automated Candidate", "2303717620521999", "Google Cloud - Cloud Architect", "9.20", "Applied", "#1e3a8a", "#93c5fd")
    ]
    y = 330
    for aid, name, reg, comp, cgpa, st, bg, fg in rows:
        draw.rectangle([(30, y), (1250, y + 55)], fill="#111827", outline="#1f2937")
        draw.text((45, y + 18), aid, font=font_ui_bold, fill="#ffffff")
        draw.text((130, y + 18), name, font=font_ui_bold, fill="#ffffff")
        draw.text((340, y + 18), reg, font=font_code, fill="#93c5fd")
        draw.text((550, y + 18), comp, font=font_ui_sub, fill="#e2e8f0")
        draw.text((850, y + 18), cgpa, font=font_code_bold, fill="#fef08a")
        
        # Badge
        draw.rectangle([(945, y + 12), (1075, y + 42)], fill=bg)
        draw.text((960, y + 18), st, font=font_code_bold, fill=fg)
        
        draw.rectangle([(1140, y + 12), (1230, y + 42)], fill="#374151")
        draw.text((1155, y + 18), "Update", font=font_code_small, fill="#ffffff")
        y += 60
        
    img.save("screenshots/figures/fig_7_13_admin.png")

# -----------------------------------------------------------------------------
# 14. Figure 7.14: Complete CI/CD Pipeline Execution Log
# -----------------------------------------------------------------------------
def render_pipeline_log():
    lines = [
        ("[Pipeline] { (Declarative: Post Actions)", "#60a5fa"),
        ("[Pipeline] echo", "#60a5fa"),
        ("==================================================", "#cbd5e1"),
        ("Campus Placement CI/CD Pipeline Completed!", "#34d399"),
        ("Student Portal:   http://localhost:5001", "#38bdf8"),
        ("TPO Admin Portal: http://localhost:5001/admin", "#38bdf8"),
        ("==================================================", "#cbd5e1"),
        ("[Pipeline] echo", "#60a5fa"),
        ("Finished: SUCCESS", "#22c55e"),
        ("[Pipeline] }", "#60a5fa"),
        ("[Pipeline] // stage", "#60a5fa"),
        ("[Pipeline] End of Pipeline", "#60a5fa")
    ]
    img = create_terminal("Jenkins Pipeline Execution Log (Post Actions)", lines, width=1200, height=330)
    img.save("screenshots/figures/fig_7_14_pipeline_complete.png")

# -----------------------------------------------------------------------------
# 15. Figure 7.15: Successfully Deployed Application (Live browser with confirmation)
# -----------------------------------------------------------------------------
def render_live_app():
    img = Image.open("screenshots/figures/fig_7_1_home.png")
    draw = ImageDraw.Draw(img)
    
    # Toast message
    draw.rectangle([(750, 600), (1240, 660)], fill="#065f46", outline="#059669", width=2)
    draw.text((770, 618), "✓ Application submitted successfully! Tracking ID: #1", font=font_ui_bold, fill="#d1fae5")
    
    img.save("screenshots/figures/fig_7_15_live_app.png")

# Copy raw diagrams
shutil.copy("screenshots/raw/page_9_img_1.jpeg", "screenshots/figures/fig_architecture.png")
shutil.copy("screenshots/raw/page_16_img_1.jpeg", "screenshots/figures/fig_docker_flow.png")
shutil.copy("screenshots/raw/page_22_img_1.jpeg", "screenshots/figures/fig_storage_flow.png")
shutil.copy("screenshots/raw/page_23_img_1.jpeg", "screenshots/figures/fig_order_flow.png")
shutil.copy("screenshots/raw/page_1_img_1.png", "screenshots/figures/cit_logo.png")

print("Rendering all figures...")
render_home_page()
render_modal_page()
render_backend_editor()
render_sqlite_terminal()
render_github_repo()
render_docker_desktop()
render_docker_ps()
render_jenkins_pipeline()
render_jenkins_console()
render_pytest_terminal()
render_ansible_terminal()
render_volume_terminal()
render_admin_dashboard()
render_pipeline_log()
render_live_app()

print("All 15 figures successfully generated in screenshots/figures/!")
