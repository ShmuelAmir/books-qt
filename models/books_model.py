from typing import Dict
from dal import books_dal


class BooksModel:
    def __init__(self):
        self._load()

    def add_book(self, book_dict: Dict[str, str]) -> None:
        books_dal.add(book_dict)
        self._load()

    def update_book(self, book_dict: Dict[str, str]) -> None:
        books_dal.update(book_dict)
        self._load()

    def delete_book(self, book_id: int) -> None:
        books_dal.delete(book_id)
        self._load()

    def _load(self) -> None:
        self.books = books_dal.get_all()
        # for book in self.books:
        #     if book["cover"]:
        #         print(book["cover"])
        #         book["cover"] = books_dal.get_image(book["cover"])

    def get_books(self) -> list:
        return self.books

    def get_book(self, book_id: int) -> Dict[str, str]:
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None
