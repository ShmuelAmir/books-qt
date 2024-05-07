import requests
from typing import Dict

BASE_URL = "http://bookmanagementapi.somee.com/api/openlibrarybook/"


def get_books_by_title_or_author(search_term) -> list:
    response = requests.get(f"{BASE_URL}{search_term}")
    return response.json()
