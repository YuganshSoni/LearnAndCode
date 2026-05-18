import pytest
import httpx
from unittest.mock import patch, MagicMock, AsyncMock
from app.infra.location.location_iq_service import LocationIQService
from common.api.exceptions import ExternalServiceError

@pytest.fixture
def api_response_mock():
    return {
        "display_name": "Test Location",
        "lat": "40.7128",
        "lon": "-74.0060"
    }

@pytest.mark.asyncio
async def test_get_coordinates_success(api_response_mock):
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = [api_response_mock]
    
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_response
        service = LocationIQService()
        result = await service.get_coordinates("test")
        
        assert len(result) == 1
        assert result[0]["formatted_address"] == "Test Location"
        assert result[0]["latitude"] == 40.7128

@pytest.mark.asyncio
async def test_get_coordinates_404():
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 404
    
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_response
        service = LocationIQService()
        result = await service.get_coordinates("nonexistent")
        assert result == []

@pytest.mark.asyncio
async def test_get_coordinates_error():
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
        "Error", request=MagicMock(), response=mock_response
    )
    
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_response
        service = LocationIQService()
        with pytest.raises(ExternalServiceError):
            await service.get_coordinates("error")
