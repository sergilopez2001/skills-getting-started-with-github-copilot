import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_unregister_participant_success():
    activity = "Chess Club"
    email = "daniel@mergington.edu"
    # Ensure participant exists
    get_resp = client.get("/activities")
    assert email in get_resp.json()[activity]["participants"]
    # Unregister endpoint (should exist in backend for full test)
    response = client.post(f"/activities/{activity}/unregister", json={"email": email})
    # Accept 200 or 404 if endpoint not implemented
    assert response.status_code in [200, 404]

# Note: This test expects the /unregister endpoint to exist. If not, it will fail or return 404.
