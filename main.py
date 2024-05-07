import sys
from PySide6.QtWidgets import QApplication

from models.books_model import BooksModel
from models.open_library_model import OpenLibraryModel

from presenters.books_presenter import BookPresenter
from presenters.search_presenter import SearchPresenter

from views.books_view import BooksView
from views.search_view import SearchView


def main():
    app = QApplication(sys.argv)

    model = BooksModel()
    books_view = BooksView()
    _book_presenter = BookPresenter(model, books_view)

    search_model = OpenLibraryModel()
    search_view = SearchView()
    _search_presenter = SearchPresenter(search_model, search_view)

    books_view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
