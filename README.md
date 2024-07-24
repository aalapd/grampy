# Instagram Auto Poster

## Description
This project is an automated Instagram posting system that schedules and uploads images to an Instagram account at specified intervals. It's designed to maintain a consistent posting schedule while adhering to Instagram's rate limits and best practices.

## Features
- Automated login to Instagram
- Scheduled posting of images
- Random intervals between posts to mimic human behavior
- Exponential backoff for error handling
- Session persistence to reduce login frequency
- Configurable through environment variables
- Logging for monitoring and debugging

## Prerequisites
- Python 3.7+
- pip (Python package manager)

## Running the Program
- In the project directory, execute the command `python ./main.py`.