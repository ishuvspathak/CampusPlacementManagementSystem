import pytest
import json
import os
import sqlite3

# Configure test environment
os.environ['DATA_DIR'] = 'data'
from app import app, init_db, get_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_health_endpoint(client):
    """Test system health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'Coimbatore Institute of Technology' in data['institution']
    assert data['database'] == 'Connected'

def test_home_page_rendering(client):
    """Test student home page renders successfully with drives."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Campus Placement Management System' in response.data
    assert b'Google Cloud' in response.data

def test_admin_dashboard_rendering(client):
    """Test TPO admin dashboard renders successfully."""
    response = client.get('/admin')
    assert response.status_code == 200
    assert b'Training &amp; Placement Officer Portal' in response.data or b'Placement Officer' in response.data
    assert b'Dr. M. Sangeetha' in response.data
    assert b'Dr. E. Arul' in response.data

def test_get_jobs_api(client):
    """Test REST API returning active placement drives."""
    response = client.get('/api/jobs')
    assert response.status_code == 200
    jobs = response.get_json()
    assert isinstance(jobs, list)
    assert len(jobs) >= 1
    assert any(j['company'] == 'Google Cloud' for j in jobs)

def test_apply_job_api(client):
    """Test submitting an application for a drive."""
    payload = {
        'drive_id': 1,
        'student_name': 'Automated Test Candidate',
        'roll_no': '2303717620521999',
        'department': 'Information Technology',
        'cgpa': 9.2,
        'email': 'autotest@cit.edu.in',
        'phone': '+91 9999988888'
    }
    response = client.post('/api/apply', 
                           data=json.dumps(payload),
                           content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] is True
    assert 'application_id' in data

def test_update_status_api(client):
    """Test updating application status from admin portal."""
    payload = {
        'application_id': 1,
        'status': 'Selected'
    }
    response = client.post('/api/status',
                           data=json.dumps(payload),
                           content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert data['success'] is True
