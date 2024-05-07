from typing import Dict

from models.open_library_model import OpenLibraryModel
from models.books_model import BooksModel
from views.books_view import BooksView


class BookPresenter:
    def __init__(
        self, model: BooksModel, booksView: BooksView, search_model: OpenLibraryModel
    ) -> None:
        self.model = model
        self.booksView = booksView
        self.search_model = search_model

        self.booksView.book_double_clicked.connect(self.handle_double_click)
        self.booksView.add_book.connect(self.handle_add_book)
        self.booksView.delete_book.connect(self.handle_delete_book)
        self.booksView.update_book.connect(self.handle_update_book)
        self.booksView.local_search_signal.connect(self.local_search_books)

        # Search signals
        self.booksView.search_signal.connect(self.search_books)
        self.booksView.add_from_search.connect(self.handle_add_book_search)

        self.update_books()

    def update_books(self) -> None:
        books = self.model.get_books()
        self.booksView.update_book_table(books)

    def handle_double_click(self, book_id: int) -> None:
        book = self.model.get_book(book_id)
        if book["cover"]:
            book["cover_bytes"] = self.model.get_image(book["cover"])
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

    def local_search_books(self, query: str) -> None:
        books = []
        for book in self.model.books:
            if (
                query.lower() in book["title"].lower()
                or query.lower() in book["author"].lower()
            ):
                books.append(book)
        self.booksView.update_book_table(books)

    # Search methods
    def search_books(self, query: str) -> None:
        books = self.search_model.get_books_by_title_or_author(query)
        self.booksView.update_book_search_table(books)

    def handle_add_book_search(self, book_title: str) -> None:
        for book in self.search_model.books:
            if book["title"] == book_title:
                self.handle_add_book(book)
                break
        self.booksView.dialog.close()
