import sys
from PySide6.QtWidgets import QApplication

from models.books_model import BooksModel
from models.open_library_model import OpenLibraryModel
from presenters.books_presenter import BookPresenter
from views.books_view import BooksView


def main():
    app = QApplication(sys.argv)

    model = BooksModel()
    search_model = OpenLibraryModel()
    view = BooksView()
    _book_presenter = BookPresenter(model, view, search_model)

    view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
