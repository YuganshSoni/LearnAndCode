from config.configurations import ARRAY_OFFSET_FOR_ONE_BASED_INDEX

class TumblrResponseParser:
    
    def __init__(self):
        self.array_offset = ARRAY_OFFSET_FOR_ONE_BASED_INDEX

    def parse_blog_response(self, json_response:dict)->dict:
        blog_info = json_response.get("tumblelog", {})
        return {
            "title" : blog_info.get("title", ""),
            "description" : blog_info.get("description", ""),
            "name": blog_info.get("name", ""),
            "total_posts": int(json_response.get("posts-total"))
        }
    
    def extract_posts_from_response(self, json_response:dict)->list:
        posts = json_response.get("posts", [])
        if not isinstance(posts, list):
            posts = [posts] if posts else []
        return posts
    
    def filter_posts_by_range(self, posts, start_index, end_index)->str:
        '''filter out posts based on range. Range was taken as input from user'''
        if not posts:
            return []
        zero_based_start = start_index - self.array_offset
        zero_based_end = end_index
        return posts[zero_based_start:zero_based_end]
    