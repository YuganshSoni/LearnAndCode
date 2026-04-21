import pytest
from services.api_reponse_parser import TumblrResponseParser

@pytest.fixture
def parser():
    return TumblrResponseParser()

def test_parse_blog_response_valid_data(parser):
    json_response = {
        "tumblelog": {
            "title": "Test Title",
            "description": "Test Description",
            "name": "testblog"
        },
        "posts-total": "100"
    }
    expected = {
        "title": "Test Title",
        "description": "Test Description",
        "name": "testblog",
        "total_posts": 100
    }
    assert parser.parse_blog_response(json_response) == expected

def test_parse_blog_response_missing_keys(parser):
    json_response = {
        "tumblelog": {},
        "posts-total": "0"
    }
    expected = {
        "title": "",
        "description": "",
        "name": "",
        "total_posts": 0
    }
    assert parser.parse_blog_response(json_response) == expected

def test_extract_posts_from_response_list(parser):
    json_response = {"posts": [{"id": 1}, {"id": 2}]}
    assert parser.extract_posts_from_response(json_response) == [{"id": 1}, {"id": 2}]

def test_extract_posts_from_response_single_dict(parser):
    json_response = {"posts": {"id": 1}}
    assert parser.extract_posts_from_response(json_response) == [{"id": 1}]

def test_extract_posts_from_response_empty(parser):
    json_response = {}
    assert parser.extract_posts_from_response(json_response) == []

def test_filter_posts_by_range_valid(parser):
    posts = [{"id": i} for i in range(1, 11)]
    start, end = 2, 5
    filtered = parser.filter_posts_by_range(posts, start, end)
    assert len(filtered) == 4
    assert filtered[0]["id"] == 2
    assert filtered[-1]["id"] == 5

def test_filter_posts_by_range_empty(parser):
    assert parser.filter_posts_by_range([], 1, 5) == []
