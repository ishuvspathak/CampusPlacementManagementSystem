import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def add_header_footer(doc):
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
        # Header: empty or minimal
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("23IT723 – DevOps Laboratory | Final Project")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(9)
        hrun.font.color.rgb = RGBColor(120, 120, 120)
        
        # Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        frun1 = fp.add_run("23IT723 – DevOps Laboratory | Final Project                      ")
        frun1.font.name = "Times New Roman"
        frun1.font.size = Pt(9.5)
        frun1.font.color.rgb = RGBColor(80, 80, 80)
        
        fldSimple = OxmlElement('w:fldSimple')
        fldSimple.set(qn('w:instr'), 'PAGE')
        fp._p.append(fldSimple)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 23, 42)
    return p

def add_subheading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.bold = True
    return p

def add_body_paragraph(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    return p

def add_bullet_point(doc, text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(2.5)
    p.paragraph_format.line_spacing = 1.12
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(10.5)
    return p

def add_image_figure(doc, img_path, caption_text, width=Inches(5.5)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(3)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(caption_text)
        run_cap.font.name = "Times New Roman"
        run_cap.font.size = Pt(10.5)
        run_cap.font.bold = True
    else:
        print(f"Warning: Image {img_path} not found!")

def generate_full_document():
    doc = docx.Document()
    add_header_footer(doc)

    # =========================================================================
    # PAGE 1: TITLE PAGE
    # =========================================================================
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(40)
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("COIMBATORE INSTITUTE OF TECHNOLOGY")
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 23, 42)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(30)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("(Government Aided Autonomous Institution Affiliated to Anna University)")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.italic = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("23IT723 - DEVOPS LABORATORY")
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(12)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("PROJECT")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(30)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("CAMPUS PLACEMENT MANAGEMENT SYSTEM")
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 58, 138)

    # CIT Circular Emblem Logo
    logo_path = "screenshots/figures/cit_logo.png"
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(24)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(1.8))

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(70)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("OCTOBER 2026")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run("Submitted by\n\n")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.italic = True

    run2 = p.add_run("2303717620521021   ISHU PATHAK")
    run2.font.name = "Times New Roman"
    run2.font.size = Pt(13)
    run2.font.bold = True

    doc.add_page_break()

    # =========================================================================
    # PAGE 2: BONAFIDE CERTIFICATE
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run("COIMBATORE INSTITUTE OF TECHNOLOGY")
    run.font.name = "Times New Roman"
    run.font.size = Pt(15)
    run.font.bold = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(30)
    run = p.add_run("(Government Aided Autonomous Institution Affiliated to Anna University)")
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.italic = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(30)
    run = p.add_run("BONAFIDE CERTIFICATE")
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(30)
    run = p.add_run(
        "Certified that this project report titled “CAMPUS PLACEMENT MANAGEMENT SYSTEM” is the bonafide work of "
        "2303717620521021 - ISHU PATHAK completed during the academic year 2025–2026 – Semester VII for the project "
        "presentation of 23IT723 – DEVOPS LABORATORY under our supervision.\n\n"
        "Certified that the candidate was examined by using the project work examination."
    )
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(40)
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run("Review Members:")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("1.  Dr.M.Sangeetha")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(20)
    run = p.add_run("2.  Dr.E.Arul")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    doc.add_page_break()

    # =========================================================================
    # PAGE 3: EVALUATION SCHEME
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("23IT723 – DEVOPS LABORATORY\nFINAL MINI PROJECT – EVALUATION SCHEME")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run(
        "The final mini project shall require students to integrate the major DevOps practices covered in the laboratory. "
        "The project should demonstrate practical implementation of version control, collaborative development, Continuous "
        "Integration, containerization and/or automated configuration/provisioning, with proper execution evidence."
    )
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)

    # Evaluation Scheme Table
    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    headers = ["S.No.", "Evaluation Component", "Key Verification Points", "Marks"]
    col_widths = [Inches(0.6), Inches(1.8), Inches(3.4), Inches(0.7)]

    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(hdr_cells[i], "E2E8F0")

    eval_data = [
        ("1", "Problem Definition & Project Planning", "Problem statement, objectives, requirements, scope, module identification, technology selection and workflow planning.", "10"),
        ("2", "Git Repository & Version Control", "Repository creation, meaningful commits, README, .gitignore, remote repository, push/pull/fetch operations and commit history.", "15"),
        ("3", "Branching, Merging & Collaboration", "Feature branches, parallel development, merging, conflict handling, branch organization and collaborative workflow.", "10"),
        ("4", "Application Development & Build", "Working application/source code, project structure, dependency management, build configuration and successful execution.", "15"),
        ("5", "Jenkins Continuous Integration", "Jenkins configuration, source-code integration, automated checkout, build job/pipeline, build execution and console verification.", "15"),
        ("6", "Docker / Containerization", "Dockerfile, image creation, container execution, port/configuration handling, application deployment and container verification.", "10"),
        ("7", "Automation / Configuration Management", "Ansible/Chef/Puppet/SaltStack or equivalent automation where applicable; repeatable configuration/provisioning and successful execution.", "5"),
        ("8", "Testing & Verification", "Functional testing, build verification, error identification, test evidence and corrective action.", "5"),
        ("9", "Documentation & Technical Presentation", "Architecture/workflow diagram, commands/configuration, screenshots, results, troubleshooting, conclusion and repository details.", "5"),
        ("10", "Final Demonstration & Viva-Voce", "Live demonstration, explanation of implementation, troubleshooting responses and technical understanding.", "10"),
        ("", "TOTAL", "", "100")
    ]

    for row_idx, data in enumerate(eval_data):
        row_cells = table.add_row().cells
        for col_idx, text in enumerate(data):
            row_cells[col_idx].text = text
            p = row_cells[col_idx].paragraphs[0]
            if len(p.runs) > 0:
                p.runs[0].font.size = Pt(8.5)
                p.runs[0].font.name = "Times New Roman"
                if row_idx == len(eval_data) - 1:
                    p.runs[0].font.bold = True
                    set_cell_background(row_cells[col_idx], "CBD5E1")

    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    doc.add_page_break()

    # =========================================================================
    # PAGE 4: MARK DISTRIBUTION & FACULTY EVALUATION RECORD
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run("Recommended Mark Distribution within the Final Demonstration")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    table2 = doc.add_table(rows=1, cols=4)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = table2.rows[0].cells
    hdr[0].text = "Assessment Area"
    hdr[1].text = "Marks"
    hdr[2].text = "Awarded Marks"
    hdr[3].text = "Remarks"
    for c in hdr:
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.size = Pt(9)
        set_cell_background(c, "E2E8F0")

    splits = [
        ("Working implementation and correctness", "30", "", ""),
        ("DevOps tool integration and automation", "20", "", ""),
        ("Version control and collaborative workflow", "15", "", ""),
        ("Build / deployment / container verification", "15", "", ""),
        ("Testing and troubleshooting", "5", "", ""),
        ("Documentation and technical presentation", "5", "", ""),
        ("Live demonstration and viva-voce", "10", "", ""),
        ("TOTAL", "100", "", "")
    ]
    for row_idx, s in enumerate(splits):
        row = table2.add_row().cells
        for col_idx, val in enumerate(s):
            row[col_idx].text = val
            p = row[col_idx].paragraphs[0]
            if len(p.runs) > 0:
                p.runs[0].font.size = Pt(8.5)
                if row_idx == len(splits) - 1:
                    p.runs[0].font.bold = True
                    set_cell_background(row[col_idx], "CBD5E1")

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("Minimum Evidence to be Submitted:")
    run.font.bold = True
    run.font.size = Pt(9.5)

    bullets = [
        "Project repository URL and project README.",
        "Git commit history and branch/merge evidence.",
        "Jenkins job/pipeline configuration and successful build evidence.",
        "Dockerfile, image and running container evidence where Docker is used.",
        "Automation/configuration scripts where applicable.",
        "Application execution and testing evidence.",
        "Architecture/workflow diagram.",
        "Short technical report containing implementation steps, results and troubleshooting.",
        "Live demonstration of the complete DevOps workflow."
    ]
    for b in bullets:
        add_bullet_point(doc, b)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("Faculty Evaluation Record")
    run.font.bold = True
    run.font.size = Pt(10.5)

    rec_table = doc.add_table(rows=5, cols=4)
    rec_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    rec_data = [
        [("Student Name", True), ("Ishu Pathak", False), ("Register No.", True), ("2303717620521021", False)],
        [("Project Title", True), ("Campus Placement Management System", False), ("Date", True), ("October 2026", False)],
        [("Final Mark", True), ("/ 100", False), ("", False), ("", False)],
        [("Faculty Evaluator I", True), ("Dr. M. Sangeetha", False), ("Signature", True), ("", False)],
        [("Faculty Evaluator II", True), ("Dr. E. Arul", False), ("Signature", True), ("", False)]
    ]
    for r_idx, row in enumerate(rec_data):
        cells = rec_table.rows[r_idx].cells
        for c_idx, cell_info in enumerate(row):
            text, is_bold = cell_info
            cells[c_idx].text = text
            p = cells[c_idx].paragraphs[0]
            if len(p.runs) > 0:
                p.runs[0].font.size = Pt(8.5)
                p.runs[0].font.bold = is_bold
                if is_bold:
                    set_cell_background(cells[c_idx], "F1F5F9")

    doc.add_page_break()

    # =========================================================================
    # PAGES 5 & 6: TABLE OF CONTENTS
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(14)
    run = p.add_run("TABLE OF CONTENTS")
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True

    toc_table = doc.add_table(rows=1, cols=3)
    toc_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    toc_hdr = toc_table.rows[0].cells
    toc_hdr[0].text = "S. NO."
    toc_hdr[1].text = "CONTENT"
    toc_hdr[2].text = "PAGE NO."
    for c in toc_hdr:
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(c, "E2E8F0")

    toc_items = [
        ("1", "INTRODUCTION", "07"),
        ("2", "OBJECTIVES", "07"),
        ("3", "ABSTRACT", "08"),
        ("4", "TECHOLOGY STACK", "08"),
        ("5", "SYSTEM ARCHITECTURE", "09"),
        ("6", "MODULE 1 — USER INTERFACE & JOB APPLICATION", "10"),
        ("7", "MODULE 2 — FLASK BACKEND & DRIVE MANAGEMENT", "11"),
        ("8", "MODULE 3 — SQLITE DATABASE MANAGEMENT", "12"),
        ("9", "MODULE 4 — GIT & GITHUB SOURCE CONTROL", "14"),
        ("10", "MODULE 5 — DOCKER CONTAINERIZATION", "15"),
        ("11", "MODULE 6 — JENKINS CI/CD PIPELINE", "17"),
        ("12", "MODULE 7 — AUTOMATED TESTING", "19"),
        ("13", "MODULE 8 — ANSIBLE DEPLOYMENT", "20"),
        ("14", "MODULE 9 — PERSISTENT STORAGE", "21"),
        ("15", "MODULE 10 — ADMIN & PLACEMENT MANAGEMENT", "22"),
        ("16", "MODULE 11 — CI/CD INTEGRATION", "23"),
        ("17", "MODULE 12 — APPLICATION & DEPLOYMENT VERIFICATION", "24"),
        ("18", "RESULTS AND OUTPUT", "26"),
        ("19", "COMMANDS USED", "26"),
        ("20", "ADVANTAGES", "31"),
        ("21", "LIMITATIONS", "31"),
        ("22", "FUTURE ENHANCEMENTS", "32"),
        ("23", "CONCLUSION", "32")
    ]

    for item in toc_items:
        row = toc_table.add_row().cells
        row[0].text = item[0]
        row[1].text = item[1]
        row[2].text = item[2]
        for c in row:
            p = c.paragraphs[0]
            if len(p.runs) > 0:
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.name = "Times New Roman"

    doc.add_page_break()

    # =========================================================================
    # PAGE 7: 1. INTRODUCTION & 2. OBJECTIVES
    # =========================================================================
    add_heading_1(doc, "1. INTRODUCTION")
    add_body_paragraph(
        doc,
        "The Campus Placement Management System is a web-based recruitment and student application portal developed to "
        "simplify and automate the process of campus recruitment in an academic environment. The system allows students to "
        "browse available campus placement drives, search for job roles, select opportunities based on minimum eligibility cutoffs, "
        "and submit verified applications through a modern digital interface. An administrative dashboard is also provided for "
        "Training & Placement Officers (TPO) and faculty coordinators to view and manage candidate submissions. The application is "
        "developed using HTML, CSS, JavaScript, Python, Flask, and SQLite, with Flask handling backend operations and SQLite storing "
        "placement and candidate application data. The project also incorporates DevOps practices to automate the development, "
        "testing, and deployment process. Git and GitHub are used for source code management, while Jenkins automates the CI/CD "
        "pipeline. Docker provides application containerization, Pytest performs automated testing, and Ansible automates deployment "
        "and container configuration. A Docker Volume named placement_data is used to provide persistent storage for the SQLite database. "
        "The project combines a functional campus placement portal with DevOps automation to provide a structured and reliable approach "
        "to application development and deployment."
    )

    add_heading_1(doc, "2. OBJECTIVES")
    objectives = [
        "To develop a digital placement system that enables students to browse, search, and apply for campus recruitment drives conveniently.",
        "To implement an admin dashboard for viewing registered candidate submissions and maintaining placement records using SQLite.",
        "To organize placement drive data systematically and provide quick access to student application details through the admin dashboard.",
        "To implement DevOps practices throughout the application development and deployment process using Git, GitHub, and Jenkins.",
        "To automate the CI/CD workflow using Jenkins for building, testing, and deploying the application.",
        "To containerize the application using Docker to provide a consistent and portable execution environment.",
        "To integrate Pytest for automated testing to verify application functionality and reduce errors before deployment.",
        "To automate application deployment and container configuration using Ansible.",
        "To implement Docker Volume for persistent storage of the SQLite database and ensure that candidate application records are retained even when the container is recreated."
    ]
    for obj in objectives:
        add_bullet_point(doc, obj)

    doc.add_page_break()

    # =========================================================================
    # PAGE 8: 3. ABSTRACT & 4. TECHNOLOGY STACK
    # =========================================================================
    add_heading_1(doc, "3. ABSTRACT")
    add_body_paragraph(
        doc,
        "The Campus Placement Management System is a web-based placement application and recruitment portal designed to "
        "simplify the placement registration process in an institutional environment. Traditional placement operations may involve "
        "long notice-board delays, manual Google form processing, difficulty in tracking multiple eligibility criteria, and challenges "
        "in maintaining student application records. The proposed system provides a digital platform where students can browse available "
        "recruitment drives, search for software roles, select positions based on CGPA cutoffs, and submit applications conveniently. "
        "An administrative dashboard is also provided for viewing and managing candidate records. The application is developed using "
        "HTML, CSS, JavaScript, Python, Flask, and SQLite, with Flask handling backend operations and SQLite storing application data. "
        "The project also implements DevOps practices to automate the software development, testing, and deployment process. Git and "
        "GitHub are used for version control and source code management, while Jenkins automates the CI/CD pipeline. Docker is used to "
        "containerize the application and provide a consistent execution environment, Pytest performs automated testing, and Ansible "
        "automates application deployment and container configuration. A Docker Volume named placement_data is used to provide persistent "
        "storage for the SQLite database, ensuring that stored applicant information is retained even when the application container is "
        "recreated. The complete workflow follows GitHub → Jenkins → Docker Build → Pytest → Ansible → Docker Container → Flask → "
        "SQLite, demonstrating the integration of a functional web application with modern DevOps practices and persistent data management."
    )

    add_heading_1(doc, "4. TECHNOLOGY STACK")
    t_stack = doc.add_table(rows=1, cols=3)
    t_stack.alignment = WD_TABLE_ALIGNMENT.CENTER
    thdr = t_stack.rows[0].cells
    thdr[0].text = "Technology"
    thdr[1].text = "Version"
    thdr[2].text = "Purpose"
    for c in thdr:
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(c, "E2E8F0")

    stack_rows = [
        ("HTML", "HTML5", "Web page structure"),
        ("CSS", "CSS3", "User interface styling"),
        ("JavaScript", "ES6+", "Frontend interaction"),
        ("Python", "3.11", "Backend programming"),
        ("Flask", "3.1.3", "Backend web framework"),
        ("SQLite", "3.x", "Database management"),
        ("Git", "2.x", "Version control"),
        ("GitHub", "—", "Source code repository"),
        ("Jenkins", "2.508.2", "CI/CD automation"),
        ("Docker", "29.8.1", "Application containerization"),
        ("Pytest", "9.1.1", "Automated testing"),
        ("Ansible", "2.10.8", "Deployment automation"),
        ("Docker SDK / Community Docker", "community.docker 1.2.2", "Docker management through Ansible")
    ]
    for r in stack_rows:
        rc = t_stack.add_row().cells
        rc[0].text = r[0]
        rc[1].text = r[1]
        rc[2].text = r[2]
        for c in rc:
            p = c.paragraphs[0]
            if len(p.runs) > 0:
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.name = "Times New Roman"

    doc.add_page_break()

    # =========================================================================
    # PAGE 9: 5. SYSTEM ARCHITECTURE
    # =========================================================================
    add_heading_1(doc, "5. SYSTEM ARCHITECTURE")
    add_image_figure(doc, "screenshots/figures/fig_architecture.png", "Figure: Campus Placement System - End-to-End CI/CD Architecture with Persistent SQLite", width=Inches(5.7))

    steps_p9 = [
        "1. Development: Developer creates and updates the Campus Placement Management application.",
        "2. Source Code Management: The application source code and configuration files are maintained using Git.",
        "3. GitHub Repository: The updated code is pushed to the GitHub repository for centralized source code management.",
        "4. Jenkins Trigger: Jenkins retrieves the latest source code from the GitHub repository and starts the CI/CD pipeline.",
        "5. Docker Build: Jenkins builds the application into a Docker image containing the Flask application and required dependencies."
    ]
    for s in steps_p9:
        add_body_paragraph(doc, s)

    doc.add_page_break()

    # =========================================================================
    # PAGE 10: ARCHITECTURE STEPS 6-11 & MODULE 1
    # =========================================================================
    steps_p10 = [
        "6. Automated Testing: Jenkins runs Pytest to verify the application before deployment.",
        "7. Deployment Automation: After successful testing, Jenkins invokes Ansible to automate the deployment process.",
        "8. Container Configuration: Ansible creates and configures the Docker container with the required image, port mapping, restart policy, and volume configuration.",
        "9. Application Execution: The Docker container runs the Flask backend, HTML/CSS/JavaScript frontend, and SQLite database.",
        "10. User Interaction: Students can browse recruitment drives, check cutoffs, and submit applications through the portal.",
        "11. Admin Management: The TPO admin dashboard allows placement officers to view and monitor registered student records stored in the database."
    ]
    for s in steps_p10:
        add_body_paragraph(doc, s)

    add_heading_1(doc, "MODULE 1 — USER INTERFACE & JOB APPLICATION")
    add_body_paragraph(
        doc,
        "This module provides the user-facing interface of the Campus Placement Management application. It is designed to "
        "make company browsing and job application submission simple and convenient for students."
    )
    add_subheading(doc, "Main Features")
    mod1_feats = [
        "Displays available campus recruitment drives with relevant details.",
        "Provides a search option to find job roles or companies quickly.",
        "Organizes recruitment drives into different categories (Product, Services).",
        "Allows users to select individual placement drives.",
        "Allows student details to be filled in a clean modal dialog.",
        "Provides application tracking ID generation for submitted profiles.",
        "Displays the drive details, package CTC, and CGPA cutoffs before submission.",
        "Allows users to place the final application submission.",
        "Provides confirmation toast alerts after successful submission.",
        "Provides a simple and user-friendly interface for accessing campus placement drives.",
        "Uses responsive interface elements for better usability across all devices.",
        "Connects the user interface with the Flask backend for processing requests."
    ]
    for f in mod1_feats:
        add_bullet_point(doc, f)

    p = doc.add_paragraph()
    r = p.add_run("Technologies: HTML, CSS, JavaScript.")
    r.font.bold = True
    r.font.size = Pt(10)

    doc.add_page_break()

    # =========================================================================
    # PAGE 11: FIGURES 7.1, 7.2 & MODULE 2
    # =========================================================================
    add_image_figure(doc, "screenshots/figures/fig_7_1_home.png", "Figure 7.1: Campus Placement Home Page", width=Inches(5.4))
    add_image_figure(doc, "screenshots/figures/fig_7_2_apply.png", "Figure 7.2: Placement Drive Selection and Job Application Modal", width=Inches(5.4))

    add_heading_1(doc, "MODULE 2 — FLASK BACKEND & DRIVE MANAGEMENT")
    add_body_paragraph(
        doc,
        "This module handles the application logic and acts as the communication layer between the frontend and "
        "the SQLite database. Flask processes user requests and manages the complete application submission process."
    )
    add_subheading(doc, "Main Functions")
    add_bullet_point(doc, "Receives requests from the frontend.")
    add_bullet_point(doc, "Processes company drive selection and filter requests.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 12: MODULE 2 CONT., FIGURE 7.3 & MODULE 3
    # =========================================================================
    mod2_funcs = [
        "Handles student job application processing.",
        "Processes candidate submission payloads.",
        "Generates and manages application tracking identifiers.",
        "Communicates with the SQLite placement database.",
        "Stores submitted applicant information.",
        "Retrieves stored drive and applicant information.",
        "Handles requests related to the TPO admin dashboard.",
        "Connects the frontend interface with backend services.",
        "Processes application routes and REST API endpoints.",
        "Runs the Flask application inside the Docker container.",
        "Provides the backend services required by the Campus Placement application."
    ]
    for f in mod2_funcs:
        add_bullet_point(doc, f)

    p = doc.add_paragraph()
    r = p.add_run("Technology: Python with Flask.")
    r.font.bold = True
    r.font.size = Pt(10)

    add_image_figure(doc, "screenshots/figures/fig_7_3_backend.png", "Figure 7.3: Flask Backend Implementation", width=Inches(5.4))

    add_heading_1(doc, "MODULE 3 — SQLITE DATABASE MANAGEMENT")
    add_body_paragraph(
        doc,
        "This module manages the storage and retrieval of placement information using SQLite. The database provides "
        "persistent application data that can be accessed by the Flask backend."
    )
    add_subheading(doc, "Main Functions")
    add_bullet_point(doc, "Stores placed candidate applications and company drives.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 13: MODULE 3 CONT., FIGURE 7.4 & MODULE 4
    # =========================================================================
    mod3_funcs = [
        "Maintains candidate records and screening statuses.",
        "Stores placement drive information.",
        "Provides database access to the Flask backend.",
        "Allows stored candidate submissions to be retrieved.",
        "Makes stored applications available to the admin dashboard.",
        "Maintains the placement.db database file.",
        "Stores the database under the application data directory.",
        "Works with the Docker Volume for persistent storage.",
        "Provides structured relational storage for applicant information.",
        "Maintains application data even when the container is recreated, through the configured Docker Volume."
    ]
    for f in mod3_funcs:
        add_bullet_point(doc, f)

    add_subheading(doc, "Database Location")
    add_body_paragraph(doc, "data/placement.db\nInside the Docker container:\n/app/data/placement.db\nTechnology: SQLite.")

    add_image_figure(doc, "screenshots/figures/fig_7_4_sqlite.png", "Figure 7.4: SQLite Database Containing Student Applications", width=Inches(5.4))

    add_heading_1(doc, "MODULE 4 — GIT & GITHUB SOURCE CONTROL")

    doc.add_page_break()

    # =========================================================================
    # PAGE 14: MODULE 4 DETAILS
    # =========================================================================
    add_body_paragraph(
        doc,
        "This module manages the source code and maintains the development history of the Campus Placement "
        "project. Git is used locally for version control, while GitHub provides the remote repository."
    )
    add_subheading(doc, "Main Functions")
    mod4_funcs = [
        "Initializes the project as a Git repository.",
        "Tracks changes made to project files.",
        "Creates commits for project updates.",
        "Maintains the history of project development.",
        "Allows changes to be reviewed through Git history.",
        "Pushes project code to GitHub.",
        "Provides a centralized remote repository.",
        "Allows Jenkins to retrieve the latest source code.",
        "Maintains the important project files in one repository.",
        "Supports integration between source control and the Jenkins pipeline.",
        "Helps maintain different versions and feature branches of the project."
    ]
    for f in mod4_funcs:
        add_bullet_point(doc, f)

    add_subheading(doc, "Main Project Files")
    files_list = [
        "app.py",
        "Dockerfile",
        "Jenkinsfile",
        "test_app.py",
        "requirements.txt",
        "docker-compose.yml",
        "docker-deploy.yml",
        "inventory.ini",
        ".gitignore"
    ]
    for fn in files_list:
        add_body_paragraph(doc, fn)

    p = doc.add_paragraph()
    r = p.add_run("Technologies: Git and GitHub.")
    r.font.bold = True
    r.font.size = Pt(10)

    doc.add_page_break()

    # =========================================================================
    # PAGE 15: FIGURE 7.5 & MODULE 5
    # =========================================================================
    add_image_figure(doc, "screenshots/figures/fig_7_5_github.png", "Figure 7.5: Campus Placement GitHub Repository", width=Inches(5.4))

    add_heading_1(doc, "MODULE 5 — DOCKER CONTAINERIZATION")
    add_body_paragraph(
        doc,
        "Docker is used to package and run the Campus Placement application in an isolated and consistent "
        "environment. The application and its required dependencies are packaged into a Docker image."
    )
    add_subheading(doc, "Main Functions")
    mod5_funcs = [
        "Creates a Docker image from the application.",
        "Packages the application and required dependencies.",
        "Provides an isolated execution environment.",
        "Creates the application container from the Docker image.",
        "Runs the Flask application inside the container.",
        "Provides port mapping for application access.",
        "Provides a consistent environment for testing and deployment.",
        "Allows the application to run independently of the host environment.",
        "Works with Jenkins for automated image creation.",
        "Works with Ansible for automated deployment.",
        "Provides a repeatable application deployment environment."
    ]
    for f in mod5_funcs:
        add_bullet_point(doc, f)

    add_subheading(doc, "Docker Configuration")
    add_body_paragraph(doc, "Docker Image:\nplacement-system-ci")

    doc.add_page_break()

    # =========================================================================
    # PAGE 16: DOCKER FLOW & CONFIG
    # =========================================================================
    add_body_paragraph(
        doc,
        "Docker Container:\nplacement-system-ansible\n\n"
        "Port Mapping:\n5001 → 5000\n\n"
        "The application can be accessed through:\nhttp://localhost:5001\n\n"
        "Technology: Docker.\n\n"
        "Docker Flow:"
    )
    add_image_figure(doc, "screenshots/figures/fig_docker_flow.png", "Figure: Docker Flow - Campus Placement System", width=Inches(5.4))

    doc.add_page_break()

    # =========================================================================
    # PAGE 17: FIGURES 7.6, 7.7 & MODULE 6
    # =========================================================================
    add_image_figure(doc, "screenshots/figures/fig_7_6_docker_desktop.png", "Figure 7.6: Campus Placement Docker Image & Containers", width=Inches(5.4))
    add_image_figure(doc, "screenshots/figures/fig_7_7_docker_ps.png", "Figure 7.7: Running Campus Placement Docker Container", width=Inches(5.4))

    add_heading_1(doc, "MODULE 6 — JENKINS CI/CD PIPELINE")
    add_body_paragraph(
        doc,
        "Jenkins is used to automate the Continuous Integration and Continuous Deployment process. It connects "
        "the source code repository with the application build, testing, and deployment stages."
    )
    add_subheading(doc, "Main Functions")
    add_bullet_point(doc, "Retrieves the latest source code from GitHub.")
    add_bullet_point(doc, "Checks out the required project version.")
    add_bullet_point(doc, "Builds the Docker image.")
    add_bullet_point(doc, "Executes automated tests.")
    add_bullet_point(doc, "Provides a sequence of automated pipeline stages.")
    add_bullet_point(doc, "Prevents later stages from proceeding when an earlier stage fails.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 18: FIGURES 7.8, 7.9 & MODULE 7
    # =========================================================================
    add_bullet_point(doc, "Invokes the Ansible playbook after successful testing.")
    add_bullet_point(doc, "Provides pipeline execution logs.")
    add_bullet_point(doc, "Reports pipeline success or failure.")
    add_bullet_point(doc, "Automates the overall CI/CD process.")
    add_bullet_point(doc, "Reduces repetitive manual build and deployment activities.")

    add_image_figure(doc, "screenshots/figures/fig_7_8_jenkins_pipeline.png", "Figure 7.8: Jenkins CI/CD Pipeline", width=Inches(5.4))
    add_image_figure(doc, "screenshots/figures/fig_7_9_jenkins_success.png", "Figure 7.9: Successful Jenkins Pipeline Execution", width=Inches(5.4))

    add_heading_1(doc, "MODULE 7 — AUTOMATED TESTING")

    doc.add_page_break()

    # =========================================================================
    # PAGE 19: MODULE 7 DETAILS & FIGURE 7.10
    # =========================================================================
    add_body_paragraph(
        doc,
        "This module validates the application automatically before deployment. Pytest is integrated into the "
        "Jenkins pipeline so that the application is tested before the deployment stage."
    )
    add_subheading(doc, "Main Functions")
    mod7_funcs = [
        "Uses Pytest for automated testing.",
        "Maintains the test file test_app.py.",
        "Executes the test inside the Docker image.",
        "Verifies the configured application tests.",
        "Provides automated test execution.",
        "Prevents deployment from continuing when an earlier pipeline stage fails.",
        "Displays test results in Jenkins.",
        "Integrates testing directly into the CI/CD workflow.",
        "Reduces the need for repeated manual testing.",
        "Helps identify application issues before deployment."
    ]
    for f in mod7_funcs:
        add_bullet_point(doc, f)

    add_subheading(doc, "Test File")
    add_body_paragraph(doc, "test_app.py")
    add_subheading(doc, "Test Command")
    add_body_paragraph(doc, "python -m pytest test_app.py")
    add_subheading(doc, "Test Result")
    add_body_paragraph(doc, "collected 6 items\ntest_app.py ...... [100%]\n6 passed")

    add_image_figure(doc, "screenshots/figures/fig_7_10_pytest.png", "Figure 7.10: Successful Automated Test Execution", width=Inches(5.4))

    doc.add_page_break()

    # =========================================================================
    # PAGE 20: MODULE 8 — ANSIBLE DEPLOYMENT
    # =========================================================================
    add_heading_1(doc, "MODULE 8 — ANSIBLE DEPLOYMENT")
    add_body_paragraph(
        doc,
        "Ansible is used to automate the deployment and configuration of the Campus Placement Docker container. "
        "The deployment configuration is defined in the Ansible playbook."
    )
    add_subheading(doc, "Main Functions")
    mod8_funcs = [
        "Executes the deployment playbook.",
        "Specifies the Docker container name.",
        "Specifies the Docker image.",
        "Configures application port mapping.",
        "Configures persistent volume mounting.",
        "Defines the container state.",
        "Defines the restart policy.",
        "Uses Docker to apply the specified configuration.",
        "Automates container deployment.",
        "Allows deployment to be triggered through Jenkins.",
        "Provides a repeatable deployment configuration."
    ]
    for f in mod8_funcs:
        add_bullet_point(doc, f)

    add_subheading(doc, "Deployment Configuration")
    add_body_paragraph(
        doc,
        "name: placement-system-ansible\n"
        "image: placement-system-ci\n"
        "published_ports:\n"
        " - \"5001:5000\"\n"
        "volumes:\n"
        " - \"placement_data:/app/data\""
    )

    doc.add_page_break()

    # =========================================================================
    # PAGE 21: FIGURE 7.11 & MODULE 9
    # =========================================================================
    add_image_figure(doc, "screenshots/figures/fig_7_11_ansible.png", "Figure 7.11: Ansible Deployment Playbook & Execution", width=Inches(5.4))

    add_heading_1(doc, "MODULE 9 — PERSISTENT STORAGE")
    add_body_paragraph(
        doc,
        "This module ensures that database information remains available even when the application container is "
        "recreated. Docker Volume is used to separate persistent application data from the container lifecycle."
    )
    add_subheading(doc, "Main Functions")
    mod9_funcs = [
        "Creates persistent storage for application data.",
        "Uses the Docker Volume placement_data.",
        "Mounts the volume to /app/data.",
        "Stores the SQLite database in the mounted directory.",
        "Separates persistent data from the container lifecycle.",
        "Allows the database to remain available after container recreation.",
        "Preserves stored applicant information.",
        "Provides persistent storage for the SQLite database."
    ]
    for f in mod9_funcs:
        add_bullet_point(doc, f)

    doc.add_page_break()

    # =========================================================================
    # PAGE 22: STORAGE FLOW, FIGURE 7.12 & MODULE 10
    # =========================================================================
    add_bullet_point(doc, "Allows the application container to be recreated without losing stored application data.")
    add_subheading(doc, "Storage Configuration")
    add_body_paragraph(doc, "placement_data:/app/data\n\nStorage Flow")

    add_image_figure(doc, "screenshots/figures/fig_storage_flow.png", "Figure: Storage Flow - Campus Placement System", width=Inches(5.4))
    add_image_figure(doc, "screenshots/figures/fig_7_12_volume.png", "Figure 7.12: Placement Data Docker Volume", width=Inches(5.4))

    add_heading_1(doc, "MODULE 10 — ADMIN & PLACEMENT MANAGEMENT")
    add_body_paragraph(
        doc,
        "This module provides access to the student applications submitted by users. The Flask backend stores the application "
        "information in SQLite, while the admin dashboard provides access to the stored records."
    )
    add_subheading(doc, "Main Functions")
    add_bullet_point(doc, "Receives job applications submitted by students.")
    add_bullet_point(doc, "Processes applicant information through Flask.")
    add_bullet_point(doc, "Stores application details in SQLite.")
    add_bullet_point(doc, "Generates an application tracking ID.")
    add_bullet_point(doc, "Makes stored applicant profiles available to the placement officer.")
    add_bullet_point(doc, "Provides access to candidate records through the admin dashboard.")
    add_bullet_point(doc, "Allows the administrator to view and shortlist candidates.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 23: APPLICATION FLOW, FIGURE 7.13 & MODULE 11
    # =========================================================================
    add_bullet_point(doc, "Connects the application workflow with database records.")
    add_bullet_point(doc, "Provides a centralized view of submitted student applications.")

    add_subheading(doc, "Application Flow")
    add_image_figure(doc, "screenshots/figures/fig_order_flow.png", "Figure: Application Flow - Campus Placement System", width=Inches(5.4))

    add_subheading(doc, "Admin Dashboard")
    add_body_paragraph(doc, "http://localhost:5001/admin")
    add_image_figure(doc, "screenshots/figures/fig_7_13_admin.png", "Figure 7.13: TPO Placement Admin Dashboard", width=Inches(5.4))

    add_heading_1(doc, "MODULE 11 — CI/CD INTEGRATION")
    add_body_paragraph(
        doc,
        "This module integrates the different DevOps tools into a single automated workflow. GitHub, Jenkins, "
        "Docker, Pytest, and Ansible work together to automate the build, testing, and deployment process."
    )

    doc.add_page_break()

    # =========================================================================
    # PAGE 24: FIGURE 7.14 & MODULE 12
    # =========================================================================
    add_subheading(doc, "Main Functions")
    mod11_funcs = [
        "Integrates GitHub with Jenkins.",
        "Retrieves the latest project code.",
        "Checks out the required project version.",
        "Builds the Docker image automatically.",
        "Runs Pytest automatically.",
        "Triggers Ansible deployment after successful testing.",
        "Creates and manages the Docker container.",
        "Provides a repeatable deployment process.",
        "Produces execution results for each pipeline stage.",
        "Reduces repetitive manual deployment activities.",
        "Connects source control, testing, containerization, and deployment into one workflow."
    ]
    for f in mod11_funcs:
        add_bullet_point(doc, f)

    add_image_figure(doc, "screenshots/figures/fig_7_14_pipeline_complete.png", "Figure 7.14: Complete CI/CD Pipeline Execution", width=Inches(5.4))

    add_heading_1(doc, "MODULE 12 — APPLICATION & DEPLOYMENT VERIFICATION")
    add_body_paragraph(
        doc,
        "This module verifies that the complete Campus Placement system is functioning correctly after deployment. "
        "Verification is performed across the application, Docker container, database, storage, Ansible deployment, "
        "and Jenkins pipeline."
    )
    add_subheading(doc, "Verification Activities")
    ver_acts = [
        "Checking the running Docker container.",
        "Checking the application port.",
        "Opening the Campus Placement application.",
        "Browsing available recruitment drives.",
        "Submitting a verified student job application.",
        "Checking the generated application tracking ID.",
        "Checking the TPO admin dashboard.",
        "Checking stored SQLite applications."
    ]
    for v in ver_acts:
        add_bullet_point(doc, v)

    doc.add_page_break()

    # =========================================================================
    # PAGE 25: VERIFICATION CONT. & FIGURE 7.15
    # =========================================================================
    ver_cont = [
        "Checking the Docker Volume.",
        "Checking Ansible execution.",
        "Checking Jenkins pipeline results.",
        "Confirming successful application deployment.",
        "Verifying that candidate data remains available after container recreation."
    ]
    for v in ver_cont:
        add_bullet_point(doc, v)

    add_subheading(doc, "Important Outputs")
    add_body_paragraph(
        doc,
        "Docker Build → SUCCESS\n"
        "Pytest → 6 PASSED\n"
        "Ansible → failed=0\n"
        "Pipeline → SUCCESS"
    )

    add_image_figure(doc, "screenshots/figures/fig_7_15_live_app.png", "Figure 7.15: Successfully Deployed Campus Placement Application", width=Inches(5.4))

    doc.add_page_break()

    # =========================================================================
    # PAGE 26: 19. RESULTS AND OUTPUT & COMMANDS USED
    # =========================================================================
    add_heading_1(doc, "19. RESULTS AND OUTPUT")
    add_body_paragraph(doc, "The implemented system successfully provides:")
    res_list = [
        "Digital placement drive browsing",
        "Company and role search",
        "Category-based selection (Product / Services)",
        "Minimum CGPA cutoff verification",
        "Student application registration",
        "Application tracking ID generation",
        "TPO admin screening dashboard",
        "SQLite database storage",
        "Docker containerization",
        "Automated Pytest testing",
        "Jenkins CI/CD automation",
        "Ansible deployment",
        "Persistent Docker Volume storage"
    ]
    for r in res_list:
        add_bullet_point(doc, r)

    add_heading_1(doc, "COMMANDS USED")
    add_subheading(doc, "1. Docker Environment")
    add_body_paragraph(doc, "Check running containers\ndocker ps\n\nCheck all containers\ndocker ps -a\n\nStart Ansible container\ndocker start ansible-docker-lab\n\nStart Jenkins\ndocker start jenkins")

    add_subheading(doc, "2. Jenkins Commands")

    doc.add_page_break()

    # =========================================================================
    # PAGE 27: COMMANDS CONT.
    # =========================================================================
    add_body_paragraph(
        doc,
        "Fix Docker socket permission for Jenkins\n"
        "docker exec -u root jenkins chmod 666 /var/run/docker.sock\n\n"
        "Verify Jenkins can access Docker\n"
        "docker exec jenkins docker info\n\n"
        "Check Jenkins port\n"
        "docker port jenkins\n\n"
        "Jenkins was accessed using:\n"
        "http://localhost:8080\n\n"
        "3. Docker Image Build\n\n"
        "Jenkins executes:\n"
        "docker build -t placement-system-ci .\n\n"
        "This creates the Docker image:\n"
        "placement-system-ci\n\n"
        "4. Automated Testing\n\n"
        "Jenkins executes:\n"
        "docker run --rm placement-system-ci python -m pytest test_app.py\n\n"
        "Expected result:\n"
        "6 passed\n\n"
        "5. Ansible Deployment\n\n"
        "Jenkins executes:\n"
        "docker exec ansible-docker-lab ansible-playbook -i /inventory.ini /docker-deploy.yml\n\n"
        "This runs the Ansible playbook.\n\n"
        "Run Ansible manually"
    )

    doc.add_page_break()

    # =========================================================================
    # PAGE 28: COMMANDS CONT.
    # =========================================================================
    add_body_paragraph(
        doc,
        "docker exec ansible-docker-lab ansible-playbook -i /inventory.ini /docker-deploy.yml\n\n"
        "View Ansible playbook\n"
        "docker exec ansible-docker-lab cat /docker-deploy.yml\n\n"
        "6. Docker Container Verification\n\n"
        "Check deployed container\n"
        "docker ps\n\n"
        "The Campus Placement container:\n"
        "placement-system-ansible\n\n"
        "Port mapping:\n"
        "5001:5000\n\n"
        "Application:\n"
        "http://localhost:5001\n\n"
        "7. Docker Volume Commands\n\n"
        "List Docker volumes\n"
        "docker volume ls\n\n"
        "Our volume:\n"
        "placement_data\n\n"
        "Inspect the volume\n"
        "docker volume inspect placement_data\n\n"
        "8. SQLite Database Commands\n\n"
        "Display stored applications\n"
        "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); "
        "[print(row) for row in c.execute('SELECT * FROM applications')]; c.close()\"\n\n"
        "Display database tables"
    )

    doc.add_page_break()

    # =========================================================================
    # PAGE 29: COMMANDS CONT.
    # =========================================================================
    add_body_paragraph(
        doc,
        "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); "
        "print(c.execute(\\\"SELECT name FROM sqlite_master WHERE type='table'\\\").fetchall()); c.close()\"\n\n"
        "Display all applications as a list\n"
        "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); "
        "print(c.execute('SELECT * FROM applications').fetchall()); c.close()\"\n\n"
        "9. Docker Volume + Database Verification\n\n"
        "To verify that the database exists inside the running container:\n"
        "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); "
        "print(c.execute('SELECT * FROM applications').fetchall()); c.close()\"\n\n"
        "The database location is:\n"
        "data/placement.db\n\n"
        "and inside the container:\n"
        "/app/data/placement.db\n\n"
        "10. Git Commands Used\n\n"
        "Initialize Git\n"
        "git init\n\n"
        "Check status\n"
        "git status\n\n"
        "Add files\n"
        "git add .\n\n"
        "Commit changes\n"
        "git commit -m \"Finalize Campus Placement CI/CD project\"\n\n"
        "Check branches\n"
        "git branch\n\n"
        "Connect GitHub repository"
    )

    doc.add_page_break()

    # =========================================================================
    # PAGE 30: COMMANDS CONT.
    # =========================================================================
    add_body_paragraph(
        doc,
        "git remote add origin https://github.com/ishuvspathak/CampusPlacementManagementSystem.git\n\n"
        "Push to GitHub\n"
        "git push -u origin main\n\n"
        "Pull latest code\n"
        "git pull origin main\n\n"
        "11. Useful Docker Commands Used During Implementation\n\n"
        "List Docker images\n"
        "docker images\n\n"
        "Stop container\n"
        "docker stop placement-system-ansible\n\n"
        "Start container\n"
        "docker start placement-system-ansible\n\n"
        "View container logs\n"
        "docker logs placement-system-ansible\n\n"
        "Execute a command inside the container\n"
        "docker exec placement-system-ansible ...\n\n"
        "12. Main Commands for Your Report\n\n"
        "If your report doesn't need every troubleshooting command, these are the most important ones to include:\n\n"
        "docker build -t placement-system-ci .\n"
        "docker run --rm placement-system-ci python -m pytest test_app.py\n"
        "docker exec ansible-docker-lab ansible-playbook -i /inventory.ini /docker-deploy.yml\n"
        "docker ps\n"
        "docker volume ls\n"
        "docker volume inspect placement_data\n"
        "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); "
        "print(c.execute('SELECT * FROM applications').fetchall()); c.close()\""
    )

    doc.add_page_break()

    # =========================================================================
    # PAGE 31: ADVANTAGES & LIMITATIONS
    # =========================================================================
    add_body_paragraph(
        doc,
        "And the Git commands:\n\n"
        "git add .\n"
        "git commit -m \"Finalize Campus Placement CI/CD project\"\n"
        "git push -u origin main"
    )

    add_heading_1(doc, "21. ADVANTAGES")
    advs = [
        "Reduces manual placement drive coordination effort.",
        "Provides a user-friendly recruitment portal for students.",
        "Provides centralized placement application information.",
        "Automates application testing with Pytest.",
        "Reduces manual deployment effort.",
        "Provides consistent application execution through Docker.",
        "Provides persistent database storage using Docker Volume.",
        "Integrates source control with CI/CD.",
        "Demonstrates automated deployment using Ansible."
    ]
    for a in advs:
        add_bullet_point(doc, a)

    add_heading_1(doc, "22. LIMITATIONS")
    lims = [
        "The current system uses SQLite for database storage.",
        "Online test or assessment integration is not currently included.",
        "User authentication and institutional SSO are not currently included.",
        "Real-time interview slot booking is not implemented.",
        "The deployment is demonstrated in a local Docker environment.",
        "Monitoring and centralized logging are not implemented."
    ]
    for l in lims:
        add_bullet_point(doc, l)

    doc.add_page_break()

    # =========================================================================
    # PAGE 32: CONCLUSION & FUTURE ENHANCEMENTS
    # =========================================================================
    add_heading_1(doc, "23. CONCLUSION")
    add_body_paragraph(
        doc,
        "The Campus Placement Management System successfully demonstrates the integration of a web-based recruitment "
        "portal with modern DevOps practices to provide an efficient and automated application environment. The system enables "
        "students to browse available recruitment drives, search for roles, filter by cutoffs, and submit applications through a "
        "simple and user-friendly interface. The admin dashboard provides a centralized platform for viewing and managing "
        "candidate applications placed by users. Flask is used to handle the backend operations, while SQLite is used to store "
        "placement information in the placement.db database. The project also demonstrates the complete implementation of a "
        "Continuous Integration and Continuous Deployment (CI/CD) workflow. Git and GitHub are used for version control and source "
        "code management, allowing the project files to be maintained in a centralized repository. Jenkins automates the CI/CD "
        "pipeline by retrieving the latest source code, building the Docker image, executing automated tests, and initiating the "
        "deployment process. Pytest is integrated into the pipeline to verify the application before deployment, helping ensure "
        "that the application passes the defined automated tests. Docker provides containerization for the Campus Placement "
        "application, allowing the Flask application and its required dependencies to run in a consistent environment. Ansible is "
        "used to automate the deployment and configuration of the Docker container through an Ansible playbook. The playbook defines "
        "important deployment configurations such as the container name, Docker image, port mapping, and volume mounting. A Docker "
        "Volume, placement_data, is used to provide persistent storage for the SQLite database. The volume is mounted to /app/data, "
        "ensuring that applicant records remain available even when the application container is recreated or updated. Overall, the "
        "project demonstrates how application development, version control, automated testing, containerization, deployment automation, "
        "and persistent storage can be integrated into a single DevOps workflow. The successful execution of the pipeline confirms the "
        "practical implementation of GitHub → Jenkins → Docker → Pytest → Ansible → Flask → SQLite, providing a complete automated "
        "approach to deploying and maintaining the Campus Placement Management System."
    )

    add_heading_1(doc, "24. FUTURE ENHANCEMENTS")
    add_body_paragraph(doc, "The system can be extended with:")
    futs = [
        "1. Online assessment & coding round integration.",
        "2. Student Single Sign-On (SSO) authentication.",
        "3. Real-time application tracking and interview scheduling.",
        "4. Automated email & SMS shortlist notifications.",
        "5. Resume parsing & AI keyword matching.",
        "6. Multi-college and department support.",
        "7. Cloud deployment on AWS / GCP.",
        "8. PostgreSQL or MySQL database integration.",
        "9. GitHub webhook-based automatic triggering.",
        "10. Application monitoring with Prometheus and Grafana logging."
    ]
    for f in futs:
        add_body_paragraph(doc, f)

    # Save final document
    out_path = "Campus_Placement_Management_System_DevOps_Report_Final.docx"
    doc.save(out_path)
    print(f"Full 32-page Word document successfully generated with all screenshots and exact formatting at {out_path}!")

if __name__ == '__main__':
    generate_full_document()
