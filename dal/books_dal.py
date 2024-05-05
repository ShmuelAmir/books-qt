import requests
from typing import Dict

BASE_URL = "http://bookmanagementapi.somee.com/api/book/"


def get_all() -> list:
    response = requests.get(BASE_URL)
    return response.json()


def get_one(book_id: int) -> Dict[str, str]:
    response = requests.get(f"{BASE_URL}{book_id}")
    return response.json()


def get_image(url: str):
    response = requests.get(url)
    return response.content


def add(book_dict: Dict[str, str]) -> None:
    response = requests.post(BASE_URL, json=book_dict)
    return response.json()


def update(book_dict: Dict[str, str]) -> None:
    response = requests.put(f"{BASE_URL}{book_dict['id']}", json=book_dict)
    return response.json()


def delete(book_id: int) -> None:
    response = requests.delete(f"{BASE_URL}{book_id}")
    return response.json()
