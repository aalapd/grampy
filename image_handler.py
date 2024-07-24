import os
from config import IMAGE_FOLDER, HASHTAGS

def get_image_list():
    if not os.path.exists(IMAGE_FOLDER):
        os.makedirs(IMAGE_FOLDER)
    return os.listdir(IMAGE_FOLDER)

def get_next_image():
    images = get_image_list()
    if images:
        return os.path.join(IMAGE_FOLDER, images[0])
    return None

def remove_image(image_path):
    os.remove(image_path)

def generate_caption(image_name):
    base_name = os.path.splitext(image_name)[0]
    return f"{base_name}\n {HASHTAGS}"