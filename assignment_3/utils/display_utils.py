def display_blog_information(blog_metadata:dict):
    """Prints blog title, name, description, and total post count."""
    title = blog_metadata.get("title", "")
    print(f"\ntitle: {title}")
    print(f"name: {blog_metadata['name']}")
    print(f"description: {blog_metadata['description']}")
    print(f"no of post: {blog_metadata['total_posts']}\n")

def display_post_images(post_number, image_urls):
    """Prints post number with its associated image URLs."""
    if not image_urls:
        return

    print(f"{post_number}. {image_urls[0]}")
    for url in image_urls[1:]:
        print(f"   {url}")