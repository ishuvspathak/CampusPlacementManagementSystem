# Campus Placement Management System
### 23IT723 – DevOps Laboratory | Final Mini Project

**Institution:** Coimbatore Institute of Technology (Autonomous Institution Affiliated to Anna University)  
**Department:** Department of Information Technology (Semester VII, 2025–2026)  
**Candidate Name:** Ishu Pathak  
**Register / Roll No:** 2303717620521021  
**Faculty Review Members:**  
1. Dr. M. Sangeetha  
2. Dr. E. Arul  

---

## 1. Project Overview

The **Campus Placement Management System** is an automated, web-based recruitment and student application portal developed to modernize campus placement drives in college environments.

- **Student Portal:** Enables students to browse active placement drives, filter companies by CTC/sector, check minimum CGPA eligibility, and submit verified job applications.
- **TPO Admin Dashboard:** Provides Training & Placement Officers (TPO) with an interactive control panel to review applications, shortlist candidates, schedule interviews, and issue selections.
- **Full DevOps Lifecycle:** Complete automated CI/CD pipeline incorporating Git/GitHub version control, Jenkins build automation, Pytest verification, Docker containerization with persistent volume storage (`placement_data`), and Ansible deployment automation.

---

## 2. Technology Stack

| Component | Technology | Version | Purpose |
|---|---|---|---|
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) | Modern | Responsive user interface & application portal |
| **Backend** | Python & Flask | 3.11 / 3.x | RESTful API routing, data validation & business logic |
| **Database** | SQLite3 | 3.x | Persistent student applications & drive records |
| **Version Control** | Git & GitHub | 2.x | Source code management, branching & collaborative merges |
| **CI/CD Automation**| Jenkins | 2.500+ | Automated build, test, containerization & deployment pipeline |
| **Containerization**| Docker & Docker Compose | 28.x / 29.x | Containerized execution environment & isolation |
| **Testing** | Pytest | 8.x | Automated unit, route & integration test verification |
| **Configuration** | Ansible | 2.10+ | Automated container provisioning & configuration management |
| **Persistent Storage**| Docker Volume (`placement_data`) | - | Retains SQLite database across container restarts |

---

## 3. DevOps Architecture & Workflow

```
[Developer] 
     │
     ▼ (git commit & push)
[GitHub Repository: ishuvspathak/CampusPlacementManagementSystem]
     │
     ▼ (Webhook / SCM Polling)
[Jenkins CI/CD Pipeline (localhost:8080)]
     │
     ├─ Stage 1: Checkout Source SCM
     ├─ Stage 2: Build Docker Image (placement-system-ci)
     ├─ Stage 3: Automated Pytest Execution (docker run --rm ...)
     ├─ Stage 4: Ansible / Docker Container Deployment
     └─ Stage 5: Health Check & Verification
     │
     ▼
[Docker Container: placement-system-ansible] ── Mounted to ──► [Docker Volume: placement_data]
     │                                                               (Stores placement.db)
     ▼ (Port 5001:5000)
[Campus Placement Management System Live Web App]
```

---

## 4. Key Project Files

- `app.py`: Core Flask application with REST API endpoints, routing, and SQLite storage logic.
- `templates/index.html`: Responsive student portal with drive filters, search, and application modal.
- `templates/admin.html`: Placement Officer dashboard with KPI cards and live status update controls.
- `test_app.py`: Automated Pytest test suite covering health, UI routes, and API endpoints.
- `Dockerfile`: Multi-stage Docker container specification.
- `docker-compose.yml`: Multi-container configuration with persistent volume mapping.
- `Jenkinsfile`: Declarative Jenkins pipeline automating build, test, and deployment.
- `docker-deploy.yml`: Ansible playbook for automated container lifecycle management.
- `inventory.ini`: Ansible inventory specification.

---

## 5. Execution & Verification Commands

### A. Local Execution
```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```
App will be accessible at: `http://localhost:5000`

### B. Run Automated Pytest
```bash
python -m pytest test_app.py -v
```

### C. Docker Commands
```bash
# 1. Build Docker image
docker build -t placement-system-ci .

# 2. Run automated test inside Docker container
docker run --rm placement-system-ci python -m pytest test_app.py

# 3. Create persistent Docker volume
docker volume create placement_data

# 4. Run application container with persistent volume
docker run -d --name placement-system-ansible -p 5001:5000 -v placement_data:/app/data --restart unless-stopped placement-system-ci

# 5. Check container status
docker ps
```
App will be accessible at: `http://localhost:5001`  
Admin dashboard: `http://localhost:5001/admin`  
Health check endpoint: `http://localhost:5001/health`

### D. Verify SQLite Database in Container
```bash
# Query stored student applications
docker exec placement-system-ansible python -c "import sqlite3; c=sqlite3.connect('data/placement.db'); [print(row) for row in c.execute('SELECT id, company, student_name, status FROM applications')]; c.close()"
```

### E. Ansible Deployment
```bash
ansible-playbook -i inventory.ini docker-deploy.yml
```

---

## 6. Access Endpoints

- **Student Portal:** `http://localhost:5001/`
- **TPO Admin Dashboard:** `http://localhost:5001/admin`
- **System Health Check API:** `http://localhost:5001/health`
- **Jenkins CI/CD Server:** `http://localhost:8080/`
