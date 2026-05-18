import requests
import json
from config.configurations import (
    REQUEST_TIMEOUT_SECONDS,
    INITIAL_START_OFFSET,
    MAX_POSTS_PER_REQUEST
)

class TumblrApiHandler():
    
    def __init__(self, blog_name:str):
        self.blog_name = blog_name
        self.time_out = REQUEST_TIMEOUT_SECONDS
        self.tumblr_api_prefix = "var tumblr_api_read = "
        self.start_offset = INITIAL_START_OFFSET,
        self.post_count = MAX_POSTS_PER_REQUEST
        self.api_url = self.get_api_url(blog_name)

    def get_api_url(self, blog_name:str)->str:
        '''api url for tumblr'''
        base_url =  f"https://{blog_name}.tumblr.com/api/read/json"
        return f"{base_url}?type=photo&num={self.post_count}&start={self.start_offset}"
    
    def extract_json_from_response(self, response_text :str)->dict:
        '''This Function will extract json text from response of tumblr which we can use to extract details'''
        json_text = response_text.replace(self.tumblr_api_prefix, "")
        brace_count = 0
        start_index = -1
        for i, char in enumerate(json_text):
            if char == "{":
                if start_index == -1:
                    start_index = i
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0 and start_index != -1:
                    return json_text[start_index:i+1]
        
        json_text = json_text.rstrip().rstrip(";")
        return json_text
    
    def fetch_blog_data(self)->dict:
        try:
            response = requests.get(self.api_url, timeout=self.time_out)
            response.raise_for_status()

            # we manually extract the JSON block from Tumblr response
            json_response = self.extract_json_from_response(response.text)

            return json.loads(json_response)
        except Exception as error:
            raise