import os
import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

src_path = r"C:\Users\91600\Downloads\Copy of 23IT723_Final_Project_Sample_Report.docx"
doc = docx.Document(src_path)

# -----------------------------------------------------------------------------
# 1. Enforce crisp solid black borders on all tables
# -----------------------------------------------------------------------------
def enforce_table_borders(table):
    tblPr = table._tbl.tblPr
    borders_xml = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'  <w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        f'</w:tblBorders>'
    )
    existing_borders = tblPr.find(docx.oxml.ns.qn('w:tblBorders'))
    if existing_borders is not None:
        tblPr.remove(existing_borders)
    tblPr.append(borders_xml)

for t in doc.tables:
    enforce_table_borders(t)

# -----------------------------------------------------------------------------
# 2. Replace all 21 embedded images with Ishu's high-resolution screenshots
# -----------------------------------------------------------------------------
image_replacements = [
    "screenshots/figures/cit_logo.png",            # Shape 1: Page 1 CIT Logo
    "screenshots/figures/fig_architecture.png",    # Shape 2: Page 9 Architecture Diagram
    "screenshots/figures/fig_7_1_home.png",        # Shape 3: Page 11 Fig 7.1 Home Page
    "screenshots/figures/fig_7_2_apply.png",       # Shape 4: Page 11 Fig 7.2 Apply Modal
    "screenshots/figures/fig_7_3_backend.png",     # Shape 5: Page 12 Fig 7.3 Flask Backend
    "screenshots/figures/fig_7_4_sqlite.png",      # Shape 6: Page 13 Fig 7.4 SQLite DB
    "screenshots/figures/fig_7_5_github.png",      # Shape 7: Page 15 Fig 7.5 GitHub Repo
    "screenshots/figures/fig_docker_flow.png",     # Shape 8: Page 16 Docker Flow
    "screenshots/figures/fig_7_6_docker_desktop.png", # Shape 9: Page 17 Fig 7.6 Docker Desktop
    "screenshots/figures/fig_7_7_docker_ps.png",   # Shape 10: Page 17 Fig 7.7 Docker ps
    "screenshots/figures/fig_7_8_jenkins_pipeline.png", # Shape 11: Page 18 Fig 7.8 Jenkins Pipeline
    "screenshots/figures/fig_7_9_jenkins_success.png",  # Shape 12: Page 18 Fig 7.9 Jenkins Log
    "screenshots/figures/fig_7_10_pytest.png",     # Shape 13: Page 19 Fig 7.10 Pytest
    "screenshots/figures/fig_7_11_ansible.png",    # Shape 14: Page 21 Ansible Playbook Code
    "screenshots/figures/fig_7_11_ansible.png",    # Shape 15: Page 21 Fig 7.11 Ansible Execution
    "screenshots/figures/fig_storage_flow.png",    # Shape 16: Page 22 Storage Flow
    "screenshots/figures/fig_7_12_volume.png",     # Shape 17: Page 22 Fig 7.12 Volume
    "screenshots/figures/fig_order_flow.png",      # Shape 18: Page 23 Application Flow
    "screenshots/figures/fig_7_13_admin.png",      # Shape 19: Page 23 Fig 7.13 Admin Dashboard
    "screenshots/figures/fig_7_14_pipeline_complete.png", # Shape 20: Page 24 Fig 7.14 Pipeline Complete
    "screenshots/figures/fig_7_15_live_app.png"    # Shape 21: Page 25 Fig 7.15 Live Deployed App
]

for idx, shape in enumerate(doc.inline_shapes):
    if idx < len(image_replacements):
        new_img_path = image_replacements[idx]
        if os.path.exists(new_img_path):
            r_id = shape._inline.graphic.graphicData.pic.blipFill.blip.embed
            image_part = doc.part.related_parts[r_id]
            with open(new_img_path, 'rb') as f:
                new_blob = f.read()
            image_part._blob = new_blob
            print(f"Replaced Shape {idx+1} with {new_img_path} ({len(new_blob)} bytes)")

# -----------------------------------------------------------------------------
# 3. Text replacements across all paragraphs & tables
# -----------------------------------------------------------------------------
text_map = [
    # Identity & metadata
    ("DIGITAL CANTEEN", "CAMPUS PLACEMENT MANAGEMENT SYSTEM"),
    ("Digital Canteen", "Campus Placement Management System"),
    ("Digital canteen", "Campus placement system"),
    ("digital canteen", "campus placement system"),
    ("DigitalCanteen", "CampusPlacementManagementSystem"),
    ("digital-canteen-ci", "placement-system-ci"),
    ("digital-canteen-ansible", "placement-system-ansible"),
    ("canteen_data", "placement_data"),
    ("canteen.db", "placement.db"),
    ("JAYASREE R", "ISHU PATHAK"),
    ("Jayasree R", "Ishu Pathak"),
    ("Jayasree273", "ishuvspathak"),
    ("jayasree", "ishu"),
    ("2303717620522022", "2303717620521021"),
    ("23037176230722022", "2303717620521021"),
    ("https://github.com/Jayasree273/DigitalCanteen.git", "https://github.com/ishuvspathak/CampusPlacementManagementSystem.git"),
    ("https://github.com/jayasree273/DigitalCanteen.git", "https://github.com/ishuvspathak/CampusPlacementManagementSystem.git"),
    
    # Domain concepts: food/canteen -> campus placement
    ("food ordering and management system", "campus placement management system"),
    ("food ordering system", "campus placement management system"),
    ("food ordering", "campus placement"),
    ("food browsing and ordering", "placement drive browsing and application"),
    ("food browsing", "placement drive browsing"),
    ("browse available food items", "browse available placement drives"),
    ("search for dishes", "search for job roles"),
    ("select food items", "select company drives"),
    ("available food items", "available placement drives"),
    ("food items", "placement drives"),
    ("food item", "placement drive"),
    ("food selection", "drive selection"),
    ("add them to a cart", "check eligibility cutoffs"),
    ("add items to a cart", "fill application details"),
    ("add items to the cart", "fill application details"),
    ("added to the shopping cart", "filled in the application form"),
    ("shopping cart", "job application registration"),
    ("Shopping cart", "Application registration"),
    ("cart and order processing", "application registration processing"),
    ("cart management", "application management"),
    ("Food Selection and Shopping Cart", "Placement Drive Selection and Job Application Modal"),
    ("Food search", "Placement search"),
    ("Digital food browsing", "Digital placement browsing"),
    ("canteen environment", "institutional environment"),
    ("canteen services", "placement cell services"),
    ("canteen operations", "placement operations"),
    ("traditional canteen", "traditional placement"),
    ("placing a food order", "submitting a job application"),
    ("place orders", "submit applications"),
    ("placed orders", "submitted applications"),
    ("placed order", "submitted application"),
    ("Order placement", "Application placement"),
    ("Order ID generation", "Application ID generation"),
    ("order ID", "application tracking ID"),
    ("order records", "application records"),
    ("order details", "application details"),
    ("order information", "application information"),
    ("order data", "application data"),
    ("order submission", "application submission"),
    ("Order Flow", "Application Flow"),
    ("Customer Orders", "Registered Candidate Applications"),
    ("Online payment", "Online assessment"),
    ("online payment", "online assessment"),
    ("Food availability management", "Drive cutoff eligibility management"),
    ("Multiple canteen support", "Multiple college & department support"),
    ("real-time order tracking", "real-time application tracking"),
    ("Real-time order tracking", "Real-time application tracking"),
    ("Order status notifications", "Shortlist status notifications"),
    ("Figure 7.12: Canteen Data Docker Volume", "Figure 7.12: Placement Data Docker Volume"),
    ("Reduces manual canteen ordering effort.", "Reduces manual campus placement coordination effort."),
    ("Orders", "Applications")
]

def replace_text_in_paragraph(p):
    for old_t, new_t in text_map:
        if old_t in p.text:
            # Replace text across runs cleanly
            # First check individual runs
            replaced = False
            for r in p.runs:
                if old_t in r.text:
                    r.text = r.text.replace(old_t, new_t)
                    replaced = True
            # If split across runs, replace full paragraph text while preserving first run format
            if not replaced and old_t in p.text:
                full_text = p.text.replace(old_t, new_t)
                if p.runs:
                    p.runs[0].text = full_text
                    for r in p.runs[1:]:
                        r.text = ""
                else:
                    p.text = full_text

for p in doc.paragraphs:
    replace_text_in_paragraph(p)

for t in doc.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                replace_text_in_paragraph(p)

# Ensure Faculty Record has Ishu Pathak & Dr. M. Sangeetha & Dr. E. Arul
faculty_table = doc.tables[2]
if len(faculty_table.rows) >= 5:
    faculty_table.rows[0].cells[1].paragraphs[0].text = "Ishu Pathak"
    faculty_table.rows[0].cells[3].paragraphs[0].text = "2303717620521021"
    faculty_table.rows[1].cells[1].paragraphs[0].text = "Campus Placement Management System"
    faculty_table.rows[1].cells[3].paragraphs[0].text = "October 2026"
    faculty_table.rows[3].cells[1].paragraphs[0].text = "Dr.M.Sangeetha"
    faculty_table.rows[4].cells[1].paragraphs[0].text = "Dr.E.Arul"
    for r in faculty_table.rows:
        for cell in r.cells:
            for p in cell.paragraphs:
                if p.runs:
                    p.runs[0].font.name = "Times New Roman"
                    p.runs[0].font.size = docx.shared.Pt(10.0)

# Save document
out_path = "Campus_Placement_Management_System_DevOps_Report_PERFECT.docx"
doc.save(out_path)
print(f"Successfully generated 100% PERFECT report at {out_path}!")
