import pytest
from unittest.mock import AsyncMock
from app.services.location import LocationService
from common.api.exceptions import ValidationError

@pytest.fixture
def mock_provider():
    return AsyncMock()

@pytest.fixture
def location_service(mock_provider):
    return LocationService(mock_provider)

@pytest.mark.asyncio
async def test_get_location_data_valid(location_service, mock_provider):
    mock_provider.get_coordinates.return_value = [{"lat": 1.0, "lon": 2.0}]
    result = await location_service.get_location_data("New York")
    assert result == [{"lat": 1.0, "lon": 2.0}]
    mock_provider.get_coordinates.assert_called_once_with("New York")

@pytest.mark.asyncio
async def test_get_location_data_invalid_empty(location_service):
    with pytest.raises(ValidationError) as excinfo:
        await location_service.get_location_data("")
    assert "cannot be empty" in str(excinfo.value)

@pytest.mark.asyncio
async def test_get_location_data_invalid_whitespace(location_service):
    with pytest.raises(ValidationError) as excinfo:
        await location_service.get_location_data("   ")
    assert "cannot be empty" in str(excinfo.value)
