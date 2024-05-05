import sys
from PySide6.QtWidgets import QApplication

from models.books_model import BooksModel
from presenters.books_presenter import BookPresenter
from views.books_view import BooksView, BookDetailsView, AddBookView


def main():
    app = QApplication(sys.argv)

    model = BooksModel()

    books_view = BooksView()
    book_details_view = BookDetailsView()
    add_book_view = AddBookView()

    _ = BookPresenter(model, books_view, book_details_view, add_book_view)

    books_view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
