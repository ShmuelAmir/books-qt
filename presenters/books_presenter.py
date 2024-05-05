from typing import Dict
from models.books_model import BooksModel
from views.books_view import BooksView
from views.book_details_view import BookDetailsView
from views.add_book_view import AddBookView


class BookPresenter:
    def __init__(
        self,
        model: BooksModel,
        booksView: BooksView,
        bookDetailsView: BookDetailsView,
        addBookView: AddBookView,
    ) -> None:
        self.model = model
        self.booksView = booksView
        self.bookDetailsView = bookDetailsView
        self.addBookView = addBookView

        self.booksView.book_double_clicked.connect(self.handle_double_click)
        self.booksView.refresh_list.connect(self.update_books)
        self.addBookView.add_book.connect(self.handle_add_book)
        self.bookDetailsView.delete_book.connect(self.handle_delete_book)
        self.bookDetailsView.update_book.connect(self.handle_update_book)
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
