import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app

client = TestClient(app, raise_server_exceptions=False)

def test_health_check_endpoint():
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Health check"}

def test_get_location_success():
    mock_data = [{
        "formatted_address": "Test City",
        "latitude": 10.0,
        "longitude": 20.0
    }]
    
    with patch("app.services.location.LocationService.get_location_data", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_data
        response = client.get("/api/v1/geo-location/?user_location_query=Test")
        
        assert response.status_code == 200
        assert response.json() == mock_data

def test_get_location_validation_error():
    response = client.get("/api/v1/geo-location/?user_location_query= ")
    assert response.status_code == 400
    assert response.json()["code"] == "VALIDATION_ERROR"

def test_get_location_external_error():
    with patch("app.services.location.LocationService.get_location_data", new_callable=AsyncMock) as mock_get:
        mock_get.side_effect = Exception("Internal Error")
        response = client.get("/api/v1/geo-location/?user_location_query=Test")
        
        assert response.status_code == 500
        assert "unexpected error" in response.json()["detail"].lower()
