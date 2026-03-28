import logging
import os
from functools import lru_cache
import requests
from datetime import datetime, timedelta
import random

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/8.0.5 Safari/601.3.9",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    ]
    return random.choice(user_agents)

@lru_cache(maxsize=None)
def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org')
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        logging.error(f"Error getting IP address: {e}")
        return None

def get_current_timestamp():
    """Returns the current timestamp."""
    return datetime.now()

def get_current_date():
    """Returns the current date."""
    return datetime.now().date()

def get_day_before(timestamp):
    """Returns the date of the day before the given timestamp."""
    return (timestamp - timedelta(days=1)).date()