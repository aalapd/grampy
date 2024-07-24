import schedule
from datetime import datetime, timedelta
import random
from config import MIN_INTERVAL, MAX_INTERVAL

def generate_daily_schedule(image_count, start_time):
    schedule_times = []
    current_time = start_time

    for _ in range(image_count):
        schedule_times.append(current_time.strftime("%H:%M"))
        
        interval = random.randint(MIN_INTERVAL, MAX_INTERVAL)
        current_time += timedelta(minutes=interval)
        
        if current_time.day != start_time.day:
            break

    return schedule_times

def schedule_posts(post_function, schedule_times):
    for post_time in schedule_times:
        schedule.every().day.at(post_time).do(post_function)

def run_scheduled_jobs():
    schedule.run_pending()