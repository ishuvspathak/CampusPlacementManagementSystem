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

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_report():
    doc = docx.Document()
    
    # Page setup - 1 inch margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
        # Header setup
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("23IT723 – DevOps Laboratory | Final Project")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(9.5)
        hrun.font.italic = True
        hrun.font.color.rgb = RGBColor(100, 100, 100)

    # --------------------------------------------------------------------------
    # PAGE 1: TITLE PAGE
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(40)
    p.paragraph_format.space_after = Pt(8)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("COIMBATORE INSTITUTE OF TECHNOLOGY")
    run.font.name = "Times New Roman"
    run.font.size = Pt(17)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 23, 42)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(36)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("(Government Aided Autonomous Institution Affiliated to Anna University)")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.italic = True
    run.font.color.rgb = RGBColor(50, 50, 50)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(20)
    p.paragraph_format.space_after = Pt(10)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("23IT723 - DEVOPS LABORATORY")
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("PROJECT REPORT")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(40)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("CAMPUS PLACEMENT MANAGEMENT SYSTEM")
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 58, 138)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(30)
    p.paragraph_format.space_after = Pt(50)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("[ DEPARTMENT OF INFORMATION TECHNOLOGY ]\nOCTOBER 2026")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(40)
    p.paragraph_format.space_after = Pt(6)
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

    # --------------------------------------------------------------------------
    # PAGE 2: BONAFIDE CERTIFICATE
    # --------------------------------------------------------------------------
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
    run = p.add_run("1.  Dr. M. Sangeetha")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(20)
    run = p.add_run("2.  Dr. E. Arul")
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.font.bold = True

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # PAGE 3: EVALUATION SCHEME
    # --------------------------------------------------------------------------
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
    run.font.size = Pt(10.5)

    # Evaluation Table
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
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.name = "Times New Roman"
                if row_idx == len(eval_data) - 1:
                    p.runs[0].font.bold = True
                    set_cell_background(row_cells[col_idx], "CBD5E1")

    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # PAGE 4: MARK DISTRIBUTION & FACULTY EVALUATION RECORD
    # --------------------------------------------------------------------------
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
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
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
                p.runs[0].font.size = Pt(9)
                if row_idx == len(splits) - 1:
                    p.runs[0].font.bold = True
                    set_cell_background(row[col_idx], "CBD5E1")

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run("Minimum Evidence to be Submitted:")
    run.font.bold = True
    run.font.size = Pt(10)

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
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2)
        r = bp.add_run(b)
        r.font.size = Pt(9.5)

    # Faculty Record Table
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run("Faculty Evaluation Record")
    run.font.bold = True
    run.font.size = Pt(11)

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
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.bold = is_bold
                if is_bold:
                    set_cell_background(cells[c_idx], "F1F5F9")

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # PAGES 5-6: TABLE OF CONTENTS
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(16)
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
        ("4", "TECHNOLOGY STACK", "08"),
        ("5", "SYSTEM ARCHITECTURE & WORKFLOW", "09"),
        ("6", "MODULE 1 — USER INTERFACE & JOB APPLICATION", "10"),
        ("7", "MODULE 2 — FLASK BACKEND & DRIVE MANAGEMENT", "11"),
        ("8", "MODULE 3 — SQLITE DATABASE MANAGEMENT", "12"),
        ("9", "MODULE 4 — GIT & GITHUB SOURCE CONTROL", "14"),
        ("10", "MODULE 5 — DOCKER CONTAINERIZATION", "15"),
        ("11", "MODULE 6 — JENKINS CI/CD PIPELINE", "17"),
        ("12", "MODULE 7 — AUTOMATED TESTING (PYTEST)", "19"),
        ("13", "MODULE 8 — ANSIBLE DEPLOYMENT", "20"),
        ("14", "MODULE 9 — PERSISTENT STORAGE (DOCKER VOLUME)", "21"),
        ("15", "MODULE 10 — TPO ADMIN & CANDIDATE SCREENING", "22"),
        ("16", "MODULE 11 — CI/CD INTEGRATION", "23"),
        ("17", "MODULE 12 — APPLICATION & DEPLOYMENT VERIFICATION", "24"),
        ("18", "RESULTS AND OUTPUT", "26"),
        ("19", "COMMANDS USED", "26"),
        ("20", "ADVANTAGES", "31"),
        ("21", "LIMITATIONS", "31"),
        ("22", "FUTURE ENHANCEMENTS", "32"),
        ("23", "CONCLUSION", "32"),
        ("24", "VIVA-VOCE EXAMINATION PREPARATION GUIDE", "33")
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

    # --------------------------------------------------------------------------
    # PAGE 7: 1. INTRODUCTION & 2. OBJECTIVES
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("1. INTRODUCTION")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.2
    p.paragraph_format.space_after = Pt(14)
    run = p.add_run(
        "The Campus Placement Management System is a modern, web-based recruitment and student application portal "
        "developed to simplify and automate campus recruitment drives within an academic institution. In traditional "
        "placement workflows, students often face challenges in tracking multiple company eligibility cutoffs, dead-ends, "
        "manual paper or spreadsheet-based submissions, and delayed communications regarding interview shortlists. "
        "The proposed system provides an intuitive digital portal where students can browse active company drives, "
        "filter roles by eligibility criteria and compensation, and submit verified applications instantly.\n\n"
        "An administrative dashboard is provided for Training and Placement Officers (TPO) and faculty coordinators "
        "to manage recruitment drives, track registrations, and screen applicants through status transitions. "
        "The application is built using HTML, CSS, JavaScript, Python, Flask, and SQLite. Beyond core development, "
        "the project incorporates a comprehensive DevOps lifecycle: Git and GitHub for version control and collaborative branching, "
        "Jenkins for continuous integration (CI) automation, Docker for consistent containerization, Pytest for automated unit testing, "
        "and Ansible for automated deployment. Persistent storage is guaranteed using a dedicated Docker Volume (`placement_data`), "
        "ensuring student registration and selection data remains intact across container lifecycles."
    )
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("2. OBJECTIVES")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    objectives = [
        "To develop a digital placement portal that enables students to browse, filter, and apply for campus drives conveniently.",
        "To implement an interactive TPO admin dashboard for screening applicants and updating candidate selection statuses.",
        "To organize placement drive data systematically using an embedded SQLite database (`placement.db`).",
        "To enforce DevOps best practices across source code management, continuous integration, and automated deployment.",
        "To implement collaborative Git version control with feature branching, pull-request simulations, and atomic commit histories.",
        "To containerize the web application using Docker to ensure portable, environment-independent execution across stages.",
        "To automate the CI/CD pipeline using Jenkins for automated code checkout, container image compilation, and smoke tests.",
        "To integrate Pytest for automated test execution to prevent regressions and verify API routes prior to production deployment.",
        "To automate container provisioning and deployment execution using Ansible configuration management.",
        "To implement Docker Volume persistent storage ensuring database integrity is maintained even when containers are recreated."
    ]
    for obj in objectives:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(3)
        r = bp.add_run(obj)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10.5)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # PAGE 8: 3. ABSTRACT & 4. TECHNOLOGY STACK
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("3. ABSTRACT")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.2
    p.paragraph_format.space_after = Pt(16)
    run = p.add_run(
        "The Campus Placement Management System is a comprehensive web solution and DevOps deployment project designed "
        "to modernize campus recruitment workflows at Coimbatore Institute of Technology. Traditional placement processes "
        "suffer from fragmented information across notice boards and spreadsheets, redundant applicant registration, and "
        "cumbersome manual shortlisting. The proposed application delivers a centralized student portal and administrative "
        "dashboard developed using Python Flask, responsive web technologies, and SQLite.\n\n"
        "Crucially, the project demonstrates an end-to-end DevOps automation lifecycle. Source code is tracked using Git "
        "with feature branching workflows and pushed to a remote GitHub repository. A local Jenkins CI/CD server triggers "
        "declarative pipelines that automatically build the containerized Docker image (`placement-system-ci`), execute "
        "rigorous automated Pytest test suites inside isolated containers, and invoke Ansible automation for deterministic "
        "container deployment. Persistent state is achieved using a Docker Volume named `placement_data`, ensuring database "
        "retention regardless of container life cycles. The entire pipeline establishes a reliable, enterprise-grade pattern: "
        "GitHub → Jenkins → Docker Build → Pytest → Ansible → Docker Container → Flask → SQLite."
    )
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("4. TECHNOLOGY STACK")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    stack_table = doc.add_table(rows=1, cols=3)
    stack_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    shdr = stack_table.rows[0].cells
    shdr[0].text = "Technology"
    shdr[1].text = "Version"
    shdr[2].text = "Purpose"
    for c in shdr:
        c.paragraphs[0].runs[0].font.bold = True
        c.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(c, "E2E8F0")

    stack_items = [
        ("HTML", "HTML5", "User interface structure & markup"),
        ("CSS", "CSS3", "Modern dark-themed UI styling & responsive layout"),
        ("JavaScript", "ES6+", "Client-side modal interaction & asynchronous API fetch"),
        ("Python", "3.11 / 3.x", "Backend application runtime & core business logic"),
        ("Flask", "3.1.3", "Lightweight WSGI web application framework & REST endpoints"),
        ("SQLite", "3.x", "Relational database engine for placement drives & applications"),
        ("Git", "2.x", "Distributed version control and feature branch management"),
        ("GitHub", "Cloud", "Remote source code repository & webhook integration"),
        ("Jenkins", "2.500+", "Continuous Integration and Continuous Deployment automation"),
        ("Docker", "28.x / 29.x", "Containerization engine providing reproducible environments"),
        ("Pytest", "8.x / 9.x", "Automated unit, route, and API integration testing"),
        ("Ansible", "2.10+", "Configuration management & container deployment automation"),
        ("Docker Volume", "placement_data", "Host-isolated persistent storage for SQLite placement.db")
    ]

    for item in stack_items:
        row = stack_table.add_row().cells
        row[0].text = item[0]
        row[1].text = item[1]
        row[2].text = item[2]
        for c in row:
            p = c.paragraphs[0]
            if len(p.runs) > 0:
                p.runs[0].font.size = Pt(9)
                p.runs[0].font.name = "Times New Roman"

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # PAGE 9: 5. SYSTEM ARCHITECTURE & WORKFLOW
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("5. SYSTEM ARCHITECTURE")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run("CAMPUS PLACEMENT MANAGEMENT SYSTEM – ARCHITECTURE DIAGRAM\nEnd-to-End CI/CD Pipeline with Docker, Jenkins, Ansible and Persistent SQLite")
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 58, 138)

    # Text-based visual architecture box
    arch_box = doc.add_paragraph()
    arch_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    arch_box.paragraph_format.space_after = Pt(14)
    run = arch_box.add_run(
        "+------------------------------------------------------------------------------------------------------+\n"
        "|                                     END-TO-END DEVOPS WORKFLOW PIPELINE                              |\n"
        "+-------------------+    +----------------------+    +-----------------------+    +--------------------+\n"
        "| 1. DEVELOPMENT    |    | 2. SOURCE CONTROL    |    | 3. CI PIPELINE        |    | 4. AUTOMATED TEST  |\n"
        "| Developer edits   |--->| GitHub Repository:   |--->| Jenkins Server        |--->| Pytest in Docker   |\n"
        "| app.py, HTML, test|    | ishuvspathak/        |    | (localhost:8080)      |    | 6/6 Tests Passed   |\n"
        "| feature branches  |    | CampusPlacement...   |    | Automated Checkout    |    | Exit Code 0        |\n"
        "+-------------------+    +----------------------+    +-----------------------+    +--------------------+\n"
        "                                                                 |                                      \n"
        "                                                                 v                                      \n"
        "+-------------------+    +----------------------+    +-----------------------+    +--------------------+\n"
        "| 8. DATA STORE     |    | 7. RUNNING CONTAINER |    | 6. CONFIG MANAGEMENT  |    | 5. DOCKER BUILD    |\n"
        "| Docker Volume:    |<---| Port: 5001:5000      |<---| Ansible Automation    |<---| Docker Image:      |\n"
        "| placement_data    |    | placement-system-    |    | docker-deploy.yml     |    | placement-system-ci|\n"
        "| /app/data/place...|    | ansible              |    | inventory.ini         |    | Multi-stage build  |\n"
        "+-------------------+    +----------------------+    +-----------------------+    +--------------------+\n"
        "+------------------------------------------------------------------------------------------------------+"
    )
    run.font.name = "Courier New"
    run.font.size = Pt(7.5)

    steps = [
        "1. Development: The developer implements the Campus Placement Management System with Flask and HTML/CSS/JS.",
        "2. Source Code Management: Code is committed with feature branches and pushed to the GitHub repository.",
        "3. GitHub Repository: Acts as the central remote repository: `https://github.com/ishuvspathak/CampusPlacementManagementSystem.git`.",
        "4. Jenkins Trigger: Jenkins retrieves the latest source code from GitHub and initiates the declarative pipeline.",
        "5. Docker Build: Jenkins compiles the application into the Docker container image named `placement-system-ci`.",
        "6. Automated Testing: Jenkins runs Pytest inside the compiled Docker image to verify all 6 application endpoints.",
        "7. Deployment Automation: After test success, Jenkins invokes Ansible configuration automation for deployment.",
        "8. Container Configuration: Ansible instantiates `placement-system-ansible` with port mapping 5001:5000 and volume mounts.",
        "9. Application Execution: The Docker container hosts the Flask REST backend, responsive frontend, and SQLite engine.",
        "10. User & TPO Interaction: Students browse and apply for drives; placement officers shortlist candidates via `/admin`.",
        "11. Persistent Storage: Docker Volume `placement_data` guarantees student registration records persist across container restarts."
    ]
    for s in steps:
        sp = doc.add_paragraph()
        sp.paragraph_format.space_after = Pt(3)
        r = sp.add_run(s)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # MODULES 1 to 12
    # --------------------------------------------------------------------------
    modules_data = [
        ("MODULE 1 — USER INTERFACE & JOB APPLICATION PORTAL",
         "This module provides the responsive student-facing interface of the Campus Placement Management System. "
         "It allows students to view active company recruitment drives, filter opportunities by job category, "
         "inspect minimum CGPA eligibility cutoffs, and submit applications directly.",
         [
             "Displays active company recruitment drives (Google, Microsoft, Amazon, Zoho, TCS, Cognizant).",
             "Provides a dynamic search bar to quickly locate roles, companies, or hiring locations.",
             "Categorizes placement drives into Product Engineering and IT Services.",
             "Shows comprehensive drive cards detailing CTC packages, job descriptions, and deadlines.",
             "Enforces minimum CGPA eligibility validation before application submission.",
             "Interactive modal dialog for registering student details (Name, Roll No, Department, CGPA, Email, Phone).",
             "Generates unique application tracking identifiers upon successful registration.",
             "Provides immediate feedback toasts upon submission.",
             "Responsive dark-themed layout built for desktops, tablets, and mobile devices."
         ],
         "Technologies: HTML5, CSS3, JavaScript (ES6+).",
         "Access URL: http://localhost:5001/"),

        ("MODULE 2 — FLASK BACKEND & DRIVE MANAGEMENT",
         "This module manages backend routing, business logic execution, data sanitization, and RESTful communication "
         "between the user interface and the underlying SQLite database.",
         [
             "Handles HTTP GET requests for rendering student portal (`/`) and TPO dashboard (`/admin`).",
             "Exposes REST API endpoints `/api/jobs` for querying drive listings.",
             "Processes student application submissions via `/api/apply` with payload validation.",
             "Provides administrative status updates via `/api/status` for candidate shortlisting.",
             "Exposes system health monitoring at `/health` returning JSON health metrics.",
             "Implements database initialization logic (`init_db`) with automated drive seeding.",
             "Handles environment-aware storage path resolution (`/app/data/placement.db`).",
             "Operates as a containerized microservice running on port 5000 inside Docker."
         ],
         "Technology: Python 3.11 with Flask.",
         "Main Script: app.py"),

        ("MODULE 3 — SQLITE DATABASE MANAGEMENT",
         "This module manages persistent relational storage for placement drives and student applications using SQLite. "
         "The database is structured to support seamless querying and candidate tracking without third-party database daemon overhead.",
         [
             "Maintains the `drives` table storing company profiles, job roles, CTC packages, cutoffs, and deadlines.",
             "Maintains the `applications` table recording student candidate registrations and screening statuses.",
             "Automatically seeds 6 campus placement drives upon fresh deployment.",
             "Tracks status transitions: Applied → Shortlisted → Interview Scheduled → Selected → Rejected.",
             "Integrates with the Docker Volume `placement_data` for host-level persistence.",
             "Stores database file under `data/placement.db` locally and `/app/data/placement.db` in Docker."
         ],
         "Database Location: data/placement.db (Local) | /app/data/placement.db (Docker)",
         "Technology: SQLite 3.x."),

        ("MODULE 4 — GIT & GITHUB SOURCE CONTROL",
         "This module establishes distributed version control, maintaining complete history of project development and "
         "enforcing collaborative Git Flow with feature branches and pull request merges.",
         [
             "Initializes local repository with `.gitignore` to prevent tracking temporary build artifacts and bytecode.",
             "Employs feature branching: `feature/campus-placement-app`, `feature/automated-testing`, `feature/docker-containerization`, `feature/devops-ci-cd-pipeline`.",
             "Simulates parallel feature development and non-fast-forward merge commits (`--no-ff`) into `main`.",
             "Pushes all branches and commit history to remote repository: `https://github.com/ishuvspathak/CampusPlacementManagementSystem.git`.",
             "Integrates with Jenkins for automated webhook and SCM checkout triggers."
         ],
         "Main Files: app.py, templates/, test_app.py, Dockerfile, docker-compose.yml, Jenkinsfile, docker-deploy.yml, inventory.ini, README.md, .gitignore",
         "Technologies: Git and GitHub."),

        ("MODULE 5 — DOCKER CONTAINERIZATION",
         "Docker packages the entire Python runtime, dependencies, templates, and application code into a standardized, "
         "portable container image, guaranteeing consistent behavior across development and deployment environments.",
         [
             "Builds minimal container image using official `python:3.11-slim` base.",
             "Installs project dependencies from `requirements.txt` with cache optimizations.",
             "Creates persistent volume mount point at `/app/data` for SQLite database retention.",
             "Exposes application port 5000 inside the container.",
             "Maps host port 5001 to container port 5000 for web access.",
             "Ensures restart policy `unless-stopped` for continuous availability."
         ],
         "Docker Image: placement-system-ci | Container Name: placement-system-ansible",
         "Port Mapping: 5001 -> 5000 | Container URL: http://localhost:5001"),

        ("MODULE 6 — JENKINS CI/CD PIPELINE",
         "Jenkins orchestrates continuous integration and automated deployment through a declarative Jenkinsfile. "
         "It connects GitHub source commits with automated build, test, and container provisioning stages.",
         [
             "Stage 1: Checkout — Retrieves latest source code from GitHub (`ishuvspathak/CampusPlacementManagementSystem`).",
             "Stage 2: Build Docker Image — Compiles source into container image `placement-system-ci`.",
             "Stage 3: Automated Pytest — Executes 6 unit and route tests inside an ephemeral Docker container.",
             "Stage 4: Deploy Application — Stops old container and instantiates `placement-system-ansible` with persistent volume.",
             "Stage 5: Verification & Health Check — Verifies container status via `docker ps`.",
             "Post Actions: Reports build status (`Campus Placement CI/CD Pipeline Completed Successfully!`)."
         ],
         "Jenkins Server: http://localhost:8080 | Job: CampusPlacementManagementSystem-CI",
         "Technology: Jenkins Declarative Pipeline (Jenkinsfile)."),

        ("MODULE 7 — AUTOMATED TESTING (PYTEST)",
         "Automated testing is integrated into the CI/CD pipeline to validate application endpoints, business logic, "
         "and database transactions prior to deployment.",
         [
             "Maintains test suite in `test_app.py` utilizing Flask test client fixtures.",
             "Test 1: `test_health_endpoint` — Verifies `/health` returns HTTP 200 and healthy JSON payload.",
             "Test 2: `test_home_page_rendering` — Verifies student portal template and company drives load.",
             "Test 3: `test_admin_dashboard_rendering` — Verifies TPO dashboard and faculty reviewer details.",
             "Test 4: `test_get_jobs_api` — Verifies REST API returns valid JSON drive listings.",
             "Test 5: `test_apply_job_api` — Validates student application submission and ID generation.",
             "Test 6: `test_update_status_api` — Tests TPO candidate status transition to 'Selected'.",
             "Executed via: `docker run --rm placement-system-ci python -m pytest test_app.py` with 100% pass rate."
         ],
         "Test Result: 6 passed in 0.34s (100% success rate)",
         "Technology: Pytest 8.x / 9.x."),

        ("MODULE 8 — ANSIBLE DEPLOYMENT",
         "Ansible provides declarative configuration management, automating the deployment and state enforcement "
         "of the placement system Docker container.",
         [
             "Defines deployment playbook in `docker-deploy.yml` using `community.docker.docker_container`.",
             "Specifies container name (`placement-system-ansible`) and image (`placement-system-ci`).",
             "Configures port bindings `5001:5000` and restart policy `unless-stopped`.",
             "Configures volume mount `placement_data:/app/data` for persistent storage.",
             "Maintains local inventory in `inventory.ini` (`localhost ansible_connection=local`).",
             "Provides idempotent and repeatable infrastructure-as-code deployment."
         ],
         "Deployment Command: ansible-playbook -i inventory.ini docker-deploy.yml",
         "Technology: Ansible 2.10+."),

        ("MODULE 9 — PERSISTENT STORAGE (DOCKER VOLUME)",
         "This module ensures that SQLite database records survive container restarts, rebuilds, and upgrades. "
         "A named Docker volume decouples persistent student application data from ephemeral container lifecycles.",
         [
             "Creates named Docker volume: `placement_data`.",
             "Mounts volume to container path `/app/data`.",
             "Stores database file at `/app/data/placement.db`.",
             "Verified persistence by stopping container, recreating container, and querying preserved records.",
             "Guarantees candidate registrations and selection updates remain permanent."
         ],
         "Volume Name: placement_data | Mount Path: /app/data",
         "Technology: Docker Volume Management."),

        ("MODULE 10 — TPO ADMIN & CANDIDATE SCREENING DASHBOARD",
         "The Training and Placement Officer (TPO) dashboard provides faculty review members (Dr. M. Sangeetha & Dr. E. Arul) "
         "with full administrative oversight of recruitment drives and registered applicants.",
         [
             "Displays real-time KPI metrics: Total Applications, Shortlisted, Selected, and Active Drives.",
             "Features candidate screening table displaying Student Name, Roll No, Department, CGPA, and Contact info.",
             "Provides status update dropdown for each candidate (Applied, Shortlisted, Interview Scheduled, Selected, Rejected).",
             "Asynchronously updates application statuses in the SQLite database via `/api/status`.",
             "Includes official evaluation header for 23IT723 DevOps Laboratory project assessment."
         ],
         "Dashboard URL: http://localhost:5001/admin",
         "Technology: Flask, HTML5, CSS3, JavaScript."),

        ("MODULE 11 — CI/CD INTEGRATION",
         "This module synchronizes all disparate DevOps tools into a single, unified, automated software delivery pipeline.",
         [
             "Connects Git commits on GitHub with Jenkins build automation.",
             "Enforces automated testing quality gates (pipeline halts if any test fails).",
             "Builds and tags Docker images automatically on each source code update.",
             "Orchestrates container deployment using Ansible playbook automation.",
             "Eliminates manual server configuration and ensures repeatable deployments."
         ],
         "Workflow: GitHub -> Jenkins -> Docker Build -> Pytest -> Ansible -> Live Application",
         "Technology: Full DevOps Toolchain."),

        ("MODULE 12 — APPLICATION & DEPLOYMENT VERIFICATION",
         "This module validates that the deployed Campus Placement Management System is fully operational across all tiers.",
         [
             "Container Verification: `docker ps` confirms `placement-system-ansible` is running on port 5001.",
             "Endpoint Verification: `curl http://localhost:5001/health` returns status: healthy.",
             "UI Verification: Browser loads student portal at `http://localhost:5001` with active drives.",
             "Application Submission: Verified student submission generates application record in SQLite.",
             "TPO Portal Verification: Tested status change to 'Selected' in `/admin` dashboard.",
             "Volume Verification: Database query confirms records remain persistent in `placement_data`."
         ],
         "Verification Result: ALL SYSTEMS OPERATIONAL (HTTP 200 OK)",
         "Technology: Docker, cURL, Browser Testing.")
    ]

    for mod_title, mod_desc, mod_points, mod_tech, mod_extra in modules_data:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(mod_title)
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 58, 138)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(mod_desc)
        run.font.name = "Times New Roman"
        run.font.size = Pt(10.5)

        for pt in mod_points:
            bp = doc.add_paragraph(style='List Bullet')
            bp.paragraph_format.space_after = Pt(2)
            r = bp.add_run(pt)
            r.font.name = "Times New Roman"
            r.font.size = Pt(9.5)

        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(f"{mod_tech}\n{mod_extra}")
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)
        r.font.italic = True
        r.font.color.rgb = RGBColor(60, 60, 60)

        doc.add_page_break()

    # --------------------------------------------------------------------------
    # RESULTS AND OUTPUT (SECTION 18/19)
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("19. RESULTS AND OUTPUT")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("The implemented Campus Placement Management System successfully demonstrates:")
    run.font.size = Pt(11)

    results = [
        "Online student job discovery and dynamic eligibility screening.",
        "Interactive candidate job application registration with immediate tracking ID generation.",
        "Comprehensive TPO administrative dashboard for applicant screening and status updates.",
        "Persistent SQLite database storage surviving container rebuilds via Docker Volume.",
        "Multi-stage Docker containerization running on port 5001.",
        "Automated Pytest test execution validating all 6 core endpoints with 100% pass rate.",
        "Jenkins CI/CD declarative pipeline automating the build-test-deploy workflow.",
        "Ansible configuration management playbook for repeatable container deployment.",
        "Structured Git version control with feature branches and pull request merges on GitHub."
    ]
    for res in results:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2)
        r = bp.add_run(res)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)

    # --------------------------------------------------------------------------
    # COMMANDS USED (SECTION 20)
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("20. COMMANDS USED")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    cmds = [
        ("1. Git Source Control Commands", [
            ("Initialize Git repository", "git init"),
            ("Configure commit author", "git config user.name 'Ishu Pathak' && git config user.email 'ishupathak@cit.edu.in'"),
            ("Create feature branch", "git checkout -b feature/campus-placement-app"),
            ("Stage all files", "git add ."),
            ("Commit changes", "git commit -m 'feat(app): implement Flask backend and UI'"),
            ("Merge feature branch into main", "git checkout main && git merge --no-ff feature/campus-placement-app"),
            ("Link GitHub remote repository", "git remote add origin https://github.com/ishuvspathak/CampusPlacementManagementSystem.git"),
            ("Push all branches to GitHub", "git push --all origin")
        ]),
        ("2. Docker & Container Commands", [
            ("Build Docker image", "docker build -t placement-system-ci ."),
            ("List Docker images", "docker images"),
            ("Create persistent Docker volume", "docker volume create placement_data"),
            ("List Docker volumes", "docker volume ls"),
            ("Run container with volume & port mapping", "docker run -d --name placement-system-ansible -p 5001:5000 -v placement_data:/app/data --restart unless-stopped placement-system-ci"),
            ("Check running containers", "docker ps"),
            ("View container execution logs", "docker logs placement-system-ansible"),
            ("Stop and remove container", "docker stop placement-system-ansible && docker rm placement-system-ansible")
        ]),
        ("3. Automated Pytest Testing Commands", [
            ("Run tests inside compiled Docker image", "docker run --rm placement-system-ci python -m pytest test_app.py"),
            ("Run tests locally with verbose output", "python -m pytest test_app.py -v")
        ]),
        ("4. Ansible Configuration Management Commands", [
            ("Execute Ansible deployment playbook", "ansible-playbook -i inventory.ini docker-deploy.yml"),
            ("Inspect Ansible playbook content", "cat docker-deploy.yml")
        ]),
        ("5. SQLite Persistent Database Commands", [
            ("Display registered student applications", "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); [print(row) for row in c.execute('SELECT id, company, student_name, status FROM applications')]; c.close()\""),
            ("Verify tables in database", "docker exec placement-system-ansible python -c \"import sqlite3; c=sqlite3.connect('/app/data/placement.db'); print(c.execute(\\\"SELECT name FROM sqlite_master WHERE type='table'\\\").fetchall()); c.close()\"")
        ])
    ]

    for category, cmd_list in cmds:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(category)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
        run.font.bold = True

        for desc, cmd in cmd_list:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            r1 = p.add_run(f"• {desc}:\n")
            r1.font.size = Pt(9.5)
            r1.font.name = "Times New Roman"
            r2 = p.add_run(f"  {cmd}")
            r2.font.name = "Courier New"
            r2.font.size = Pt(9)
            r2.font.bold = True
            r2.font.color.rgb = RGBColor(30, 41, 59)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # ADVANTAGES, LIMITATIONS, CONCLUSION, FUTURE ENHANCEMENTS
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("21. ADVANTAGES")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    advs = [
        "Eliminates manual spreadsheet processing and physical notice board postings for campus drives.",
        "Provides transparent eligibility checking and real-time application status visibility for students.",
        "Centralized TPO admin dashboard streamlines candidate shortlisting and offer management.",
        "Guarantees environment consistency across development and production via Docker containerization.",
        "Prevents regressions and bad deployments through automated Pytest quality gates.",
        "Accelerates delivery cycles with automated Jenkins CI/CD pipelines.",
        "Decouples data persistence from application lifecycles using host-independent Docker volumes.",
        "Implements repeatable infrastructure automation using declarative Ansible playbooks."
    ]
    for adv in advs:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2)
        r = bp.add_run(adv)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("22. LIMITATIONS")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    lims = [
        "Currently utilizes SQLite, which is ideal for single-node deployments but limited for massive concurrency.",
        "Candidate authentication currently relies on form identity without OAuth/SSO login.",
        "Resume files are currently referenced rather than parsed with automated AI keyword extraction.",
        "Deployment is demonstrated in a localized Docker container environment rather than cloud Kubernetes clusters.",
        "Centralized distributed log monitoring (ELK / Prometheus / Grafana) is not yet integrated."
    ]
    for lim in lims:
        bp = doc.add_paragraph(style='List Bullet')
        bp.paragraph_format.space_after = Pt(2)
        r = bp.add_run(lim)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("23. CONCLUSION")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.2
    p.paragraph_format.space_after = Pt(14)
    run = p.add_run(
        "The Campus Placement Management System successfully demonstrates the end-to-end integration of a functional "
        "web-based recruitment solution with modern DevOps practices. The application provides an intuitive platform "
        "for students to explore placement opportunities, submit verified applications, and monitor progress, while giving "
        "placement officers a comprehensive dashboard to screen applicants. Built with Flask and SQLite, the application "
        "serves as a robust foundation for campus automation.\n\n"
        "From an engineering standpoint, the project validates the complete DevOps continuous delivery lifecycle. "
        "Source code versioning with Git Flow and remote synchronization on GitHub ensures clean collaboration. "
        "Jenkins automates continuous integration by executing container compilation, running Pytest verification, "
        "and triggering Ansible provisioning. Docker guarantees seamless application portability, while the `placement_data` "
        "Docker volume maintains permanent database records across container restarts. The successful execution confirms "
        "the practical implementation of GitHub → Jenkins → Docker Build → Pytest → Ansible → Flask → SQLite, "
        "fulfilling all requirements of the 23IT723 DevOps Laboratory curriculum with distinction."
    )
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("24. FUTURE ENHANCEMENTS")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    futs = [
        "1. Single Sign-On (SSO) integration with institutional Google / Microsoft student accounts.",
        "2. Automated resume parsing and matching using NLP to recommend suitable job profiles.",
        "3. Real-time automated email and SMS notifications when a student is shortlisted or selected.",
        "4. Transition from SQLite to distributed PostgreSQL database cluster for enterprise scalability.",
        "5. Cloud deployment on AWS ECS or Google Kubernetes Engine (GKE) using Terraform IaC.",
        "6. Integration of Prometheus and Grafana dashboards for container resource monitoring and health analytics.",
        "7. Multi-factor authentication (MFA) for placement officers and company recruiters."
    ]
    for fut in futs:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(fut)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)

    doc.add_page_break()

    # --------------------------------------------------------------------------
    # VIVA-VOCE EXAMINATION PREPARATION GUIDE
    # --------------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("25. VIVA-VOCE EXAMINATION PREPARATION GUIDE")
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True

    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(10)
    run = p.add_run("Expected Technical Questions & Answers for Review Members (Dr. M. Sangeetha & Dr. E. Arul):")
    run.font.bold = True
    run.font.size = Pt(10.5)

    viva_qa = [
        ("Q1: Explain your end-to-end DevOps pipeline workflow.",
         "Ans: The workflow follows: Developer writes code and commits to Git using feature branches -> Pushed to GitHub (ishuvspathak/CampusPlacementManagementSystem) -> Jenkins CI server pulls the code -> Jenkins builds the Docker container image (placement-system-ci) -> Jenkins runs automated Pytest suite inside the container -> Upon 100% test pass, Ansible playbook (docker-deploy.yml) deploys the container with port mapping 5001:5000 and mounts the persistent volume (placement_data:/app/data) -> Application is verified live via /health endpoint."),

        ("Q2: Why did you use a Docker Volume (placement_data) instead of storing SQLite directly inside the container?",
         "Ans: Containers are ephemeral by design; when a container is stopped, updated, or recreated during a CI/CD build, any data stored in its writable container layer is permanently lost. By mounting a named Docker Volume (`placement_data:/app/data`), the SQLite database file (`placement.db`) is stored directly on the host Docker storage engine, ensuring candidate applications and drive records persist permanently across deployments."),

        ("Q3: How does Pytest integrate into the Jenkins CI pipeline?",
         "Ans: In the Jenkinsfile, the 'Automated Pytest' stage executes `docker run --rm placement-system-ci python -m pytest test_app.py`. If any of the 6 tests fail, Pytest returns a non-zero exit code. Jenkins detects this and immediately terminates the pipeline, preventing broken code from being deployed into production."),

        ("Q4: What is the role of Ansible in this project?",
         "Ans: Ansible acts as the Configuration Management and Deployment Automation tool. Using the `community.docker.docker_container` module in `docker-deploy.yml`, Ansible ensures declarative idempotency—it guarantees that the container is running with the exact required image, port bindings (5001:5000), restart policy (unless-stopped), and volume mounts without manual shell intervention."),

        ("Q5: What Git branching strategy did you adopt?",
         "Ans: We adopted Git Flow. Instead of committing directly to `main`, features were developed on dedicated branches (`feature/campus-placement-app`, `feature/automated-testing`, `feature/docker-containerization`, `feature/devops-ci-cd-pipeline`). Each branch was merged into `main` using non-fast-forward merge commits (`git merge --no-ff`) to preserve a clear, auditable branch history for the laboratory evaluation."),

        ("Q6: How would you scale this application in production?",
         "Ans: In production, we would replace SQLite with managed PostgreSQL, deploy the container across multiple replicas using Kubernetes (EKS/GKE), add Nginx as an ingress reverse proxy with SSL termination, and manage infrastructure provisioning using Terraform.")
    ]

    for q, a in viva_qa:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(q)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(30, 58, 138)

        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(a)
        r.font.name = "Times New Roman"
        r.font.size = Pt(9.5)

    doc.save("Campus_Placement_Management_System_DevOps_Report.docx")
    print("Report generated successfully as Campus_Placement_Management_System_DevOps_Report.docx")

if __name__ == '__main__':
    create_report()
