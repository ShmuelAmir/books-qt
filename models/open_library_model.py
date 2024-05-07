from typing import Dict
from dal import openlibrary


class OpenLibraryModel:
    books = []

    def get_books_by_title_or_author(self, search_text: str) -> list:
        self.books = openlibrary.get_books_by_title_or_author(search_text)
        return self.books
