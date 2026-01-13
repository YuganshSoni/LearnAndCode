from config.configurations import (
    PHOTO_URL_KEY_1280,
    PHOTO_URL_KEY_500,
    PHOTO_URL_KEY_400,
    PHOTO_URL_KEY_250,
)

class ImageHandler:

    def __init__(self):
        self.http_protocol_prefix = "http"

    def extract_all_image_urls_from_post(self, post)->list:
        image_urls = [] 
        photos = post.get("photos", [])
        if photos and isinstance(photos, list):
            for photo in photos:
                if isinstance(photo, dict):
                    url_1280 = photo.get(PHOTO_URL_KEY_1280, "")
                    url_500 = photo.get(PHOTO_URL_KEY_500, "")
                    url_400 = photo.get(PHOTO_URL_KEY_400, "")
                    url_250 = photo.get(PHOTO_URL_KEY_250, "")
                    url = url_1280 or url_500 or url_400 or url_250
                    if url and url.startswith(self.http_protocol_prefix):
                        image_urls.append(url)
        else:
            url_1280 = post.get(PHOTO_URL_KEY_1280, "")
            url_500 = post.get(PHOTO_URL_KEY_500, "")
            url_400 = post.get(PHOTO_URL_KEY_400, "")
            url_250 = post.get(PHOTO_URL_KEY_250, "")
            
            url = url_1280 or url_500 or url_400 or url_250
            if url and url.startswith(self.http_protocol_prefix):
                image_urls.append(url)
        return image_urls

    def get_image_urls_for_post(self, post)->list:
        return self.extract_all_image_urls_from_post(post)

