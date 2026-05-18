from config.configurations import (     
    MINIMUM_POST_INDEX
)

class InputHandler:
    
    def __init__(self):
        self.range_separator = "-"
        self.minimum_post_index = MINIMUM_POST_INDEX

    def get_blog_name_from_user(self)->str:
        return input("Enter then tumblr blog name : ").strip()
    
    def get_post_range_from_user(self)->str:
        range_string = input("\nEnter the range: ").strip()
        return self.parse_post_range(range_string)
    
    def parse_post_range(self, range_string:str)->tuple:
        try:
            start_str, end_str = range_string.split(self.range_separator)
            start = int(start_str.strip())
            end = int(end_str.strip())
            if start < self.minimum_post_index or end < start:
                raise Exception
            return (start, end)
        except Exception as e:
            raise