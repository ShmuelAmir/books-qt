from models.open_library_model import OpenLibraryModel
from views.search_view import SearchView


class SearchPresenter:
    def __init__(self, searchModel: OpenLibraryModel, searchView: SearchView) -> None:
        self.model = searchModel
        self.view = searchView

        self.view.search_signal.connect(self.search)

    def search(self, query: str) -> None:
        self.model.get_books_by_title_or_author(query)
        self.view.set_table(self.model.books)
