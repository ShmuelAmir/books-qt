from typing import Dict
from models.books_model import BooksModel
from views.books_view import BooksView


class BookPresenter:
    def __init__(self, model: BooksModel, booksView: BooksView) -> None:
        self.model = model
        self.booksView = booksView

        self.booksView.book_double_clicked.connect(self.handle_double_click)
        self.booksView.add_book.connect(self.handle_add_book)
        self.booksView.delete_book.connect(self.handle_delete_book)
        self.booksView.update_book.connect(self.handle_update_book)

        self.booksView.search_signal.connect(self.search_books)
        self.booksView.add_from_search.connect(self.handle_add_book_search)

        self.update_books()

    def update_books(self) -> None:
        books = self.model.get_books()
        self.booksView.update_book_table(books)

    def handle_double_click(self, book_id: int) -> None:
        book = self.model.get_book(book_id)
        self.booksView.show_book_details_dialog(book)

    def handle_add_book(self, book_dict: Dict[str, str]) -> None:
        self.model.add_book(book_dict)
        self.update_books()

    def handle_delete_book(self, book_id: int) -> None:
        self.model.delete_book(book_id)
        self.update_books()

    def handle_update_book(self, book_dict: Dict[str, str]) -> None:
        self.model.update_book(book_dict)
        self.update_books()

    def search_books(self, query: str) -> None:
        books = self.model.get_books_by_title_or_author(query)
        self.booksView.update_book_search_table(books)

    def handle_add_book_search(self, book_title: str) -> None:
        self.booksView.dialog.close()
        for book in self.model.search_books:
            if book["title"] == book_title:
                self.handle_add_book(book)
                break
