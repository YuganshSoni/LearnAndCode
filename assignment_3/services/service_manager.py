from services.input_handler import InputHandler
from services.tumblr_api_handler import TumblrApiHandler
from services.api_reponse_parser import TumblrResponseParser
from services.image_extractor import ImageHandler

def get_input_handler()->InputHandler:
    return InputHandler()

def get_tumblr_api_handler(blog_name:str)->TumblrApiHandler:
    return TumblrApiHandler(blog_name)

def get_tumblr_api_response_parser()->TumblrResponseParser:
    return TumblrResponseParser()

def get_image_handler()->ImageHandler:
    return ImageHandler()