import os
import logging
import time
import schedule
from datetime import datetime, timedelta
from instagram_client import InstagramClient
from scheduler import generate_daily_schedule, schedule_posts, run_scheduled_jobs
from image_handler import get_image_list, get_next_image, remove_image, generate_caption
from exceptions import LoginError, UploadError, NoImagesError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def post_image():
    try:
        client = InstagramClient()
        client.login()

        image_path = get_next_image()
        if not image_path:
            raise NoImagesError("No images left to post")

        image_name = os.path.basename(image_path)
        caption = generate_caption(image_name)
        
        client.post_image(image_path, caption)
        remove_image(image_path)
        
        client.save_session()
        return True

    except (LoginError, UploadError, NoImagesError) as e:
        logger.error(f"Error during posting: {str(e)}")
        return False

def main():
    start_time = datetime.now() + timedelta(minutes=1)
    images = get_image_list()
    image_count = len(images)

    if image_count == 0:
        logger.info("No images to post. Exiting.")
        return

    daily_schedule = generate_daily_schedule(image_count, start_time)
    schedule_posts(post_image, daily_schedule)

    logger.info(f"Scheduled {len(daily_schedule)} posts starting at: {daily_schedule[0]}")
    logger.info(f"Full schedule: {', '.join(daily_schedule)}")

    while image_count > 0:
        run_scheduled_jobs()
        if schedule.jobs:
            time.sleep(60)
        else:
            break
        image_count = len(get_image_list())

    logger.info("All images have been posted. Script is ending.")

if __name__ == "__main__":
    main()