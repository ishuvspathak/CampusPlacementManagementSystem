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
    assert b'Ishu Pathak' in response.data
    assert b'Information Technology' in response.data

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
    import time
    unique_suffix = str(int(time.time() * 1000) % 100000)
    payload = {
        'drive_id': 1,
        'student_name': 'Automated Test Candidate',
        'roll_no': f'23037176{unique_suffix}',
        'department': 'Information Technology',
        'cgpa': 9.2,
        'email': f'autotest_{unique_suffix}@cit.edu.in',
        'phone': '+91 9999988888'
    }
    response = client.post('/api/apply', 
                           data=json.dumps(payload),
                           content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['success'] is True
    assert 'application_id' in data

def test_duplicate_application_blocked(client):
    """Test that duplicate application by same student for same drive is blocked."""
    import time
    unique_suffix = str(int(time.time() * 1000) % 100000)
    payload = {
        'drive_id': 2,
        'student_name': 'Duplicate Test Student',
        'roll_no': f'23037176{unique_suffix}',
        'department': 'Information Technology',
        'cgpa': 8.5,
        'email': f'dup_{unique_suffix}@cit.edu.in',
        'phone': '+91 9888877777'
    }
    # First submission should succeed
    res1 = client.post('/api/apply', data=json.dumps(payload), content_type='application/json')
    assert res1.status_code == 201

    # Second submission with same roll number and drive must be blocked
    res2 = client.post('/api/apply', data=json.dumps(payload), content_type='application/json')
    assert res2.status_code == 400
    assert 'already registered' in res2.get_json()['message'].lower()

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
