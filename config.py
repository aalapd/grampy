import os
from dotenv import load_dotenv

load_dotenv()

# Instagram credentials
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

# Paths
IMAGE_FOLDER = 'images'
SESSION_FILE = 'session.json'

# Hashtags
HASHTAGS = "#midjourney #aiart #promptengineering #chaos #midjourneychaos"

# Scheduling
MIN_INTERVAL = 30  # minutes
MAX_INTERVAL = 120  # minutes

# Retry settings
MAX_LOGIN_ATTEMPTS = 5
MAX_UPLOAD_ATTEMPTS = 3
MAX_BACKOFF_DELAY = 3600  # seconds