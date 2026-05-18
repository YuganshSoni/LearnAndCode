import pytest
from services.input_handler import InputHandler

@pytest.fixture
def input_handler():
    return InputHandler()

def test_parse_post_range_valid(input_handler):
    assert input_handler.parse_post_range("1-10") == (1, 10)
    assert input_handler.parse_post_range(" 5 - 15 ") == (5, 15)

def test_parse_post_range_invalid_format(input_handler):
    with pytest.raises(Exception):
        input_handler.parse_post_range("1:10")
    with pytest.raises(Exception):
        input_handler.parse_post_range("abc-def")

def test_parse_post_range_invalid_logic(input_handler):
    with pytest.raises(Exception):
        input_handler.parse_post_range("10-5")
    with pytest.raises(Exception):
        input_handler.parse_post_range("0-10")
