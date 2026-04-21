import pytest
import json
from unittest.mock import patch, MagicMock
from services.tumblr_api_handler import TumblrApiHandler

@pytest.fixture
def api_handler():
    return TumblrApiHandler("testblog")

def test_get_api_url(api_handler):
    url = api_handler.get_api_url("testblog")
    assert "testblog.tumblr.com/api/read/json" in url
    assert "type=photo" in url

def test_extract_json_from_response_wrapped(api_handler):
    response_text = 'var tumblr_api_read = {"title": "Test"};'
    extracted = api_handler.extract_json_from_response(response_text)
    assert json.loads(extracted) == {"title": "Test"}

def test_extract_json_from_response_unwrapped(api_handler):
    response_text = '{"title": "Test"}'
    extracted = api_handler.extract_json_from_response(response_text)
    assert json.loads(extracted) == {"title": "Test"}

def test_fetch_blog_data_success(api_handler):
    mock_response = MagicMock()
    mock_response.text = 'var tumblr_api_read = {"posts-total": 10};'
    mock_response.status_code = 200
    
    with patch('requests.get', return_value=mock_response):
        data = api_handler.fetch_blog_data()
        assert data["posts-total"] == 10

def test_fetch_blog_data_error(api_handler):
    with patch('requests.get', side_effect=Exception("Network Error")):
        with pytest.raises(Exception):
            api_handler.fetch_blog_data()
