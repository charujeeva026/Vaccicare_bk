import requests
import json
from datetime import date, time

# Test URL (assuming the app is running locally on 8000)
BASE_URL = "http://127.0.0.1:8000"

def test_booking():
    # Use IDs we know exist from Neon
    # Client ID 1 exist (from earlier migration check)
    # Doctor ID 5 exist (it has hospital_id 6)
    
    payload = {
        "client_id": 16, # From my check earlier, client had 18 rows. ID 16 should be safe.
        "doctor_id": 5,
        "appointment_date": "2026-03-20",
        "appointment_time": "10:00:00"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/appointment/create", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Note: This requires the FastAPI app to be running.
    # Since I cannot easily run it and keep it alive, I will instead 
    # use a script that uses SQLAlchemy directly to simulate the router logic.
    pass
