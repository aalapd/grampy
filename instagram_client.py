import os
import time
import random
import logging
from instagrapi import Client
from exceptions import LoginError, UploadError
from config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, SESSION_FILE, MAX_LOGIN_ATTEMPTS, MAX_UPLOAD_ATTEMPTS

logger = logging.getLogger(__name__)

class InstagramClient:
    def __init__(self):
        self.client = Client()
        self.client.delay_range = [10, 30]

    def login(self):
        for attempt in range(MAX_LOGIN_ATTEMPTS):
            try:
                if os.path.exists(SESSION_FILE):
                    session = self.client.load_settings(SESSION_FILE)
                    self.client.set_settings(session)
                    self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
                    self.client.get_timeline_feed()
                else:
                    self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
                
                logger.info("Successfully logged in")
                return
            except Exception as e:
                logger.warning(f"Login attempt {attempt + 1} failed: {str(e)}")
                if "Please wait a few minutes before you try again" in str(e):
                    self._exponential_backoff(attempt)
                elif attempt == MAX_LOGIN_ATTEMPTS - 1:
                    raise LoginError("Max login attempts reached")
        
        raise LoginError("Couldn't login user")

    def post_image(self, image_path, caption):
        for attempt in range(MAX_UPLOAD_ATTEMPTS):
            try:
                self.client.photo_upload(path=image_path, caption=caption)
                logger.info(f"Posted image: {image_path}")
                return
            except Exception as e:
                logger.error(f"Error uploading image (attempt {attempt + 1}): {str(e)}")
                if "Please wait a few minutes before you try again" in str(e):
                    self._exponential_backoff(attempt)
                elif attempt == MAX_UPLOAD_ATTEMPTS - 1:
                    raise UploadError(f"Failed to upload image after {MAX_UPLOAD_ATTEMPTS} attempts")

    def save_session(self):
        self.client.dump_settings(SESSION_FILE)

    @staticmethod
    def _exponential_backoff(attempt, max_delay=3600):
        delay = min(30 * (2 ** attempt), max_delay)
        time.sleep(delay + random.uniform(0, 10))