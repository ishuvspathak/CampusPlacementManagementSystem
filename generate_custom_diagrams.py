import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("screenshots/figures", exist_ok=True)

font_large_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
font_med_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 16)
font_regular = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 13)
font_small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 11)
font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)

# -----------------------------------------------------------------------------
# 1. Architecture Diagram (Page 9)
# -----------------------------------------------------------------------------
def generate_architecture_diagram():
    w, h = 1400, 920
    img = Image.new("RGB", (w, h), "#f8fafc")
    draw = ImageDraw.Draw(img)
    
    # Outer Border
    draw.rectangle([(10, 10), (w-10, h-10)], fill="#ffffff", outline="#0284c7", width=3)
    
    # Top Banner
    draw.rectangle([(10, 10), (w-10, 75)], fill="#0f172a")
    draw.text((w//2 - 380, 20), "CAMPUS PLACEMENT SYSTEM – ARCHITECTURE DIAGRAM", font=font_large_bold, fill="#ffffff")
    draw.text((w//2 - 310, 48), "End-to-End CI/CD Pipeline with Docker, Jenkins, Ansible and Persistent SQLite", font=font_regular, fill="#93c5fd")
    
    # Top Row: 6 Pipeline Stages
    top_stages = [
        ("1. DEVELOPMENT", "#10b981", [
            ("Developer (You)", True),
            ("Candidate: Ishu Pathak", False),
            ("Edit app.py, HTML/CSS", False),
            ("Add unit tests in test_app.py", False),
            ("Local Git feature branches", False)
        ], 30),
        ("2. SOURCE CONTROL", "#3b82f6", [
            ("GitHub Repository", True),
            ("ishuvspathak/", False),
            ("CampusPlacement...", False),
            ("Branches: main, features", False),
            ("Webhook / Poll SCM", False)
        ], 260),
        ("3. CI PIPELINE (JENKINS)", "#6366f1", [
            ("Jenkins Server", True),
            ("http://localhost:8080", False),
            ("1. Checkout SCM", False),
            ("2. Build Docker Image", False),
            ("3. Run Pytest Suite", False),
            ("4. Deploy via Ansible", False)
        ], 490),
        ("4. CONFIG & DEPLOYMENT", "#f59e0b", [
            ("Ansible Automation", True),
            ("ansible-docker-lab", False),
            ("Playbook: docker-deploy.yml", False),
            ("Inventory: inventory.ini", False),
            ("State: started", False),
            ("Port & Volume binding", False)
        ], 720),
        ("5. CONTAINERIZATION", "#06b6d4", [
            ("Docker Engine", True),
            ("Container:", False),
            ("placement-system-ansible", False),
            ("Exposed Port: 5001->5000", False),
            ("Restart: unless-stopped", False)
        ], 950),
        ("6. APP STACK (CONTAINER)", "#8b5cf6", [
            ("Flask Application", True),
            ("Frontend: HTML5/CSS3/JS", False),
            ("Backend: Python 3.11", False),
            ("REST APIs: /api/jobs, /apply", False),
            ("Database: SQLite", False)
        ], 1180)
    ]
    
    for title, col, items, x in top_stages:
        box_w = 195
        draw.rectangle([(x, 95), (x + box_w, 360)], fill="#f8fafc", outline=col, width=2)
        draw.rectangle([(x, 95), (x + box_w, 130)], fill=col)
        draw.text((x + 10, 103), title, font=font_med_bold, fill="#ffffff")
        
        y = 145
        for text, is_b in items:
            draw.text((x + 12, y), text, font=font_med_bold if is_b else font_small, fill="#0f172a" if is_b else "#334155")
            y += 24
            
        # Draw arrow to next
        if x < 1180:
            arrow_x = x + box_w
            draw.line([(arrow_x, 220), (arrow_x + 35, 220)], fill="#64748b", width=3)
            draw.polygon([(arrow_x + 35, 215), (arrow_x + 42, 220), (arrow_x + 35, 225)], fill="#64748b")
            
    # Middle Arrow down from Jenkins to Ansible/Docker
    draw.line([(600, 360), (600, 410)], fill="#6366f1", width=3)
    draw.polygon([(595, 410), (600, 420), (605, 410)], fill="#6366f1")
    draw.text((615, 380), "Build & Test Passed -> Trigger Deployment", font=font_small, fill="#475569")
    
    # Bottom Row: Users, Running Application, Data Persistence
    bottom_sections = [
        ("7. USERS & ACTORS", "#ec4899", [
            ("• Students / Candidates:", True),
            ("  Browse Drives, Filter by CGPA", False),
            ("  Submit Application Form", False),
            ("  Instant Tracking ID #", False),
            ("• Placement Officer (TPO):", True),
            ("  Review Applications", False),
            ("  Screening: Shortlist / Select", False)
        ], 30, 380),
        ("8. RUNNING PLACEMENT APPLICATION", "#0284c7", [
            ("Live Portal: http://localhost:5001", True),
            ("• Student Portal (Home Page)", False),
            ("  Active Company Drives Cards", False),
            ("  Search & Eligibility Cutoff Validation", False),
            ("• TPO Admin Dashboard (/admin)", False),
            ("  Real-time Application Table", False),
            ("  Review Faculty: Dr. M. Sangeetha & Dr. E. Arul", False)
        ], 440, 520),
        ("9. DATA PERSISTENCE", "#10b981", [
            ("SQLite Database: placement.db", True),
            ("Docker Volume: placement_data", True),
            ("Host storage: /app/data", False),
            ("Persistent across container restarts", False),
            ("Verified data retention: 100%", False)
        ], 990, 380)
    ]
    
    for title, col, items, x, bw in bottom_sections:
        draw.rectangle([(x, 435), (x + bw, 690)], fill="#f8fafc", outline=col, width=2)
        draw.rectangle([(x, 435), (x + bw, 470)], fill=col)
        draw.text((x + 15, 443), title, font=font_med_bold, fill="#ffffff")
        
        y = 485
        for text, is_b in items:
            draw.text((x + 18, y), text, font=font_med_bold if is_b else font_regular, fill="#0f172a" if is_b else "#334155")
            y += 26
            
    # Connecting arrows bottom
    draw.line([(410, 560), (440, 560)], fill="#64748b", width=3)
    draw.polygon([(435, 555), (443, 560), (435, 565)], fill="#64748b")
    
    draw.line([(960, 560), (990, 560)], fill="#64748b", width=3)
    draw.polygon([(985, 555), (993, 560), (985, 565)], fill="#64748b")
    
    # Bottom Summary Grid
    draw.rectangle([(30, 715), (w-30, 890)], fill="#0f172a")
    
    # Column 1: Tech Stack
    draw.text((50, 730), "TECHNOLOGY STACK", font=font_med_bold, fill="#38bdf8")
    draw.text((50, 760), "Frontend: HTML5, CSS3, JavaScript (ES6+)", font=font_regular, fill="#cbd5e1")
    draw.text((50, 785), "Backend: Python 3.11, Flask 3.1.3", font=font_regular, fill="#cbd5e1")
    draw.text((50, 810), "Database: SQLite 3.x (placement.db)", font=font_regular, fill="#cbd5e1")
    draw.text((50, 835), "CI/CD & DevOps: Git, GitHub, Docker, Jenkins, Ansible, Pytest", font=font_regular, fill="#cbd5e1")
    
    # Column 2: Key Ports
    draw.text((580, 730), "KEY PORTS & ACCESS", font=font_med_bold, fill="#38bdf8")
    draw.text((580, 760), "Jenkins Server   ->  http://localhost:8080", font=font_code, fill="#cbd5e1")
    draw.text((580, 785), "Student Portal   ->  http://localhost:5001", font=font_code, fill="#cbd5e1")
    draw.text((580, 810), "TPO Admin Portal ->  http://localhost:5001/admin", font=font_code, fill="#cbd5e1")
    draw.text((580, 835), "Health Check API ->  http://localhost:5001/health", font=font_code, fill="#cbd5e1")
    
    # Column 3: Benefits
    draw.text((1050, 730), "DEVOPS BENEFITS", font=font_med_bold, fill="#38bdf8")
    draw.text((1050, 760), "✓ Automated CI/CD Pipeline (Build #1 Success)", font=font_regular, fill="#34d399")
    draw.text((1050, 785), "✓ Persistent SQLite Data via Docker Volume", font=font_regular, fill="#34d399")
    draw.text((1050, 810), "✓ 6/6 Pytest Tests Passed Automatically", font=font_regular, fill="#34d399")
    draw.text((1050, 835), "✓ Repeatable Infrastructure via Ansible", font=font_regular, fill="#34d399")
    
    img.save("screenshots/figures/fig_architecture.png")
    print("Generated clean fig_architecture.png for Campus Placement Management System!")

# -----------------------------------------------------------------------------
# 2. Docker Flow Diagram (Page 16)
# -----------------------------------------------------------------------------
def generate_docker_flow_diagram():
    w, h = 1400, 850
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    
    # Title Banner
    draw.rectangle([(20, 20), (w-20, 80)], fill="#1e3a8a")
    draw.text((w//2 - 270, 32), "Docker Flow – Campus Placement System", font=font_large_bold, fill="#ffffff")
    
    steps = [
        ("Application Code", "#fee2e2", "#991b1b", "placement-app/", [
            ("• Contains the Flask application code and related files.", False),
            ("• Includes app.py, templates/, requirements.txt, test_app.py.", False)
        ]),
        ("Dockerfile", "#fef3c7", "#92400e", "FROM python:3.11-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"app.py\"]", [
            ("• Defines the container environment and build steps to package the image.", False),
            ("• Installs Python dependencies and sets startup execution commands.", False)
        ]),
        ("Docker Image", "#e0e7ff", "#3730a3", "placement-system-ci", [
            ("• Built directly from the project Dockerfile.", False),
            ("• Contains Python 3.11, Flask, dependencies, and application source.", False),
            ("• Image name: placement-system-ci (tag: latest)", True)
        ]),
        ("Docker Container", "#e0f2fe", "#075985", "placement-system-ansible", [
            ("• A running, isolated instance of the placement-system-ci image.", False),
            ("• Container name: placement-system-ansible", True),
            ("• Runs the Flask backend on port 5000 inside the container.", False)
        ]),
        ("Flask Application", "#f3e8ff", "#6b21a8", "Flask", [
            ("• Campus Placement web server runs inside the running container.", False),
            ("• Accessible via the container's mapped port (http://localhost:5001).", True),
            ("• Handles student applications, TPO screening, and SQLite storage.", False)
        ])
    ]
    
    y = 105
    for title, bg, fg, code_text, bullets in steps:
        draw.rectangle([(40, y), (w-40, y + 115)], fill=bg, outline=fg, width=2)
        
        # Left badge
        draw.rectangle([(55, y + 15), (280, y + 50)], fill=fg)
        draw.text((70, y + 22), title, font=font_med_bold, fill="#ffffff")
        
        # Code/sub box
        draw.rectangle([(55, y + 60), (320, y + 105)], fill="#ffffff", outline=fg)
        draw.text((65, y + 66), code_text[:40], font=font_code, fill="#0f172a")
        
        # Right bullets
        bx = 350
        by = y + 25
        for b_text, is_bold in bullets:
            draw.text((bx, by), b_text, font=font_med_bold if is_bold else font_regular, fill="#0f172a")
            by += 28
            
        # Down arrow
        if y < 650:
            ay = y + 115
            draw.line([(w//2, ay), (w//2, ay + 20)], fill="#64748b", width=3)
            draw.polygon([(w//2 - 6, ay + 15), (w//2, ay + 22), (w//2 + 6, ay + 15)], fill="#64748b")
            
        y += 140
        
    img.save("screenshots/figures/fig_docker_flow.png")
    print("Generated clean fig_docker_flow.png for Campus Placement System!")

# -----------------------------------------------------------------------------
# 3. Storage Flow Diagram (Page 22)
# -----------------------------------------------------------------------------
def generate_storage_flow_diagram():
    w, h = 1400, 620
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    
    # Title Banner
    draw.rectangle([(20, 15), (w-20, 75)], fill="#1e3a8a")
    draw.text((w//2 - 270, 27), "Storage Flow – Campus Placement System", font=font_large_bold, fill="#ffffff")
    
    steps = [
        ("Flask Backend", "#0f172a", "Flask handles student applications and database queries."),
        ("SQLite Database", "#0369a1", "Embedded database engine managing relational tables."),
        ("placement.db", "#047857", "Stores drives, students, eligibility cutoffs, and application records."),
        ("/app/data", "#b45309", "Database storage directory inside the Docker container."),
        ("placement_data", "#4338ca", "Dedicated named Docker volume mounted to /app/data."),
        ("Persistent Storage", "#be123c", "Guarantees student candidate data is permanently retained across container rebuilds.")
    ]
    
    y = 95
    for title, col, desc in steps:
        draw.rectangle([(50, y), (350, y + 55)], fill=col)
        draw.text((70, y + 16), title, font=font_med_bold, fill="#ffffff")
        
        draw.rectangle([(370, y), (w-50, y + 55)], fill="#f8fafc", outline=col, width=1)
        draw.text((390, y + 18), desc, font=font_regular, fill="#1e293b")
        
        if y < 450:
            draw.line([(200, y + 55), (200, y + 75)], fill="#64748b", width=3)
            draw.polygon([(195, y + 70), (200, y + 78), (205, y + 70)], fill="#64748b")
            
        y += 75
        
    img.save("screenshots/figures/fig_storage_flow.png")
    print("Generated clean fig_storage_flow.png for Campus Placement System!")

# -----------------------------------------------------------------------------
# 4. Application Flow Diagram (Page 23 / 24)
# -----------------------------------------------------------------------------
def generate_order_flow_diagram():
    w, h = 1400, 750
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    
    # Title Banner
    draw.rectangle([(20, 15), (w-20, 75)], fill="#1e3a8a")
    draw.text((w//2 - 290, 27), "Application Flow – Campus Placement System", font=font_large_bold, fill="#ffffff")
    
    # Top Row: Student Steps
    student_steps = [
        ("Student Candidate", "#10b981", "Logs in / visits portal\nat http://localhost:5001", 50),
        ("Browse / Search Drives", "#3b82f6", "Explores Google, AWS,\nZoho, TCS, Microsoft", 320),
        ("Select Drive & Check Cutoff", "#6366f1", "Validates CGPA eligibility\n(e.g., Min 8.5 CGPA)", 590),
        ("Fill Application Form", "#f59e0b", "Enters Roll No, Name,\nEmail, Mobile, CGPA", 860),
        ("Submit Application", "#ec4899", "Receives generated\nTracking ID #", 1130)
    ]
    
    for title, col, desc, x in student_steps:
        box_w = 220
        draw.rectangle([(x, 105), (x + box_w, 240)], fill="#f8fafc", outline=col, width=2)
        draw.rectangle([(x, 105), (x + box_w, 145)], fill=col)
        draw.text((x + 10, 115), title, font=font_med_bold, fill="#ffffff")
        draw.text((x + 15, 160), desc, font=font_regular, fill="#1e293b")
        
        if x < 1130:
            arrow_x = x + box_w
            draw.line([(arrow_x, 170), (arrow_x + 50, 170)], fill="#64748b", width=3)
            draw.polygon([(arrow_x + 45, 165), (arrow_x + 53, 170), (arrow_x + 45, 175)], fill="#64748b")
            
    # Arrow down from Submit Application
    draw.line([(1240, 240), (1240, 310)], fill="#64748b", width=3)
    draw.line([(1240, 310), (150, 310)], fill="#64748b", width=3)
    draw.line([(150, 310), (150, 370)], fill="#64748b", width=3)
    draw.polygon([(145, 365), (150, 373), (155, 365)], fill="#64748b")
    draw.text((600, 285), "HTTP POST /api/apply Payload Transmitted", font=font_small, fill="#475569")
    
    # Bottom Row: Processing & Admin Screening Steps
    backend_steps = [
        ("Flask REST Backend", "#0f172a", "Validates input payload\n& checks database state", 50),
        ("SQLite Storage", "#0369a1", "Inserts candidate record into\napplications table in placement.db", 380),
        ("Persistent Docker Volume", "#047857", "placement_data retains\nrecords permanently on host", 710),
        ("TPO Screening Dashboard", "#7c3aed", "Placement Officers view,\nshortlist & select candidates", 1040)
    ]
    
    for title, col, desc, x in backend_steps:
        box_w = 310
        draw.rectangle([(x, 380), (x + box_w, 520)], fill="#f8fafc", outline=col, width=2)
        draw.rectangle([(x, 380), (x + box_w, 420)], fill=col)
        draw.text((x + 15, 390), title, font=font_med_bold, fill="#ffffff")
        draw.text((x + 15, 435), desc, font=font_regular, fill="#1e293b")
        
        if x < 1040:
            arrow_x = x + box_w
            draw.line([(arrow_x, 450), (arrow_x + 20, 450)], fill="#64748b", width=3)
            draw.polygon([(arrow_x + 15, 445), (arrow_x + 23, 450), (arrow_x + 15, 455)], fill="#64748b")
            
    # Bottom summary box
    draw.rectangle([(50, 560), (w-50, 710)], fill="#f1f5f9", outline="#94a3b8", width=1)
    draw.text((70, 575), "END-TO-END PLACEMENT WORKFLOW VERIFICATION", font=font_med_bold, fill="#0f172a")
    draw.text((70, 605), "1. Candidate Ishu Pathak (2303717620521021) registers for Google Cloud Solutions Architect drive.", font=font_regular, fill="#334155")
    draw.text((70, 630), "2. Application is serialized into JSON and stored in persistent SQLite placement.db database.", font=font_regular, fill="#334155")
    draw.text((70, 655), "3. Placement Review Members (Dr. M. Sangeetha & Dr. E. Arul) access /admin and change status to 'Selected'.", font=font_regular, fill="#334155")
    draw.text((70, 680), "4. Status changes persist even when the Docker container placement-system-ansible is destroyed and rebuilt.", font=font_regular, fill="#334155")
    
    img.save("screenshots/figures/fig_order_flow.png")
    print("Generated clean fig_order_flow.png for Campus Placement System!")

generate_architecture_diagram()
generate_docker_flow_diagram()
generate_storage_flow_diagram()
generate_order_flow_diagram()
