from services.service_manager import get_input_handler
from services.service_manager import get_tumblr_api_handler
from services.service_manager import get_tumblr_api_response_parser
from services.service_manager import get_image_handler
from utils.display_utils import display_blog_information, display_post_images

def main():
    '''
        main orchestration function which coordinates with all functions.
        Tumblr Blog Data Fetcher

        This module handles fetching and parsing blog data
        from Tumblr's legacy JSON API.
    '''
    try:
        input_manager = get_input_handler()
        blog_name = input_manager.get_blog_name_from_user()
        start_index, end_index = input_manager.get_post_range_from_user()

        api_manager = get_tumblr_api_handler(blog_name)
        json_response = api_manager.fetch_blog_data()

        response_manager = get_tumblr_api_response_parser()
        blog_metadata = response_manager.parse_blog_response(json_response)
        display_blog_information(blog_metadata)

        all_posts = response_manager.extract_posts_from_response(json_response)
        total_available_posts = len(all_posts)

        if start_index > total_available_posts:
            return
        end_index = min(end_index, total_available_posts)
        posts = response_manager.filter_posts_by_range(all_posts, start_index, end_index)

        image_handler = get_image_handler()
        for post_number, post in enumerate(posts, start=start_index):
            image_urls = image_handler.get_image_urls_for_post(post)
            display_post_images(post_number, image_urls)

    except Exception as error:
        print(f"Unexpected error: {error}")
    
if __name__ == "__main__":
    main()