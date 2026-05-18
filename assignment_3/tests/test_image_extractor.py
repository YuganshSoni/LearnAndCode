import pytest
from services.image_extractor import ImageHandler

@pytest.fixture
def image_handler():
    return ImageHandler()

def test_extract_all_image_urls_from_post_photos_list(image_handler):
    post = {
        "photos": [
            {"photo-url-1280": "http://example.com/1.jpg"},
            {"photo-url-500": "http://example.com/2.jpg"}
        ]
    }
    assert image_handler.extract_all_image_urls_from_post(post) == [
        "http://example.com/1.jpg",
        "http://example.com/2.jpg"
    ]

def test_extract_all_image_urls_from_post_single_photo(image_handler):
    post = {
        "photo-url-1280": "http://example.com/single.jpg"
    }
    assert image_handler.extract_all_image_urls_from_post(post) == ["http://example.com/single.jpg"]

def test_extract_all_image_urls_from_post_fallback(image_handler):
    post = {
        "photo-url-500": "http://example.com/fallback.jpg"
    }
    assert image_handler.extract_all_image_urls_from_post(post) == ["http://example.com/fallback.jpg"]

def test_extract_all_image_urls_from_post_invalid_protocol(image_handler):
    post = {
        "photo-url-1280": "ftp://example.com/invalid.jpg"
    }
    assert image_handler.extract_all_image_urls_from_post(post) == []

def test_extract_all_image_urls_from_post_empty(image_handler):
    assert image_handler.extract_all_image_urls_from_post({}) == []
