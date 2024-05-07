from PySide6.QtWidgets import (
    QPushButton,
    QTableWidgetItem,
    QMainWindow,
)
from PySide6.QtCore import Signal
from PySide6.QtGui import QIntValidator
from typing import Dict

from ui.books_ui import Ui_MainWindow as Books_UI
from views.add_book_view import AddBookView
from views.book_details_view import BookDetailsView
from views.search_view import SearchView


class BooksView(QMainWindow, Books_UI):
    delete_book = Signal(int)
    update_book = Signal(dict)
    add_book = Signal(dict)
    local_search_signal = Signal(str)

    search_signal = Signal(str)
    book_double_clicked = Signal(int)
    add_from_search = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.books_table.setSortingEnabled(False)

        self.search_line.textChanged.connect(self.handle_text_changed)
        self.add_btn.clicked.connect(self.show_add_dialog)
        self.actionSearch.triggered.connect(self.show_search_dialog)
        self.books_table.doubleClicked.connect(self.handle_double_click)


    def update_book_table(self, books: list) -> None:
        self.books_table.setRowCount(0)
        for row, book in enumerate(books):
            self.books_table.insertRow(row)
            self.books_table.setItem(row, 0, QTableWidgetItem(str(book["id"])))
            self.books_table.setItem(row, 1, QTableWidgetItem(book["title"]))
            self.books_table.setItem(row, 2, QTableWidgetItem(book["author"]))
            self.books_table.setItem(row, 3, QTableWidgetItem(str(book["publishYear"])))
            self.books_table.setItem(row, 4, QTableWidgetItem(str(book["pages"])))
        
    def handle_double_click(self, index):
        row = index.row()
        book_id = int(self.books_table.item(row, 0).text())
        self.book_double_clicked.emit(book_id)

    def handle_text_changed(self, text: str) -> None:
        self.local_search_signal.emit(text)

    # Dialogs
    def show_add_dialog(self) -> None:
        dialog = AddBookView()
        dialog.add_btn.clicked.connect(
            lambda: self.add_book.emit(dialog.get_book_info())
        )
        dialog.add_btn.clicked.connect(dialog.close)
        dialog.show()    # not blocking
        #dialog.exec()    # blocking

    def show_book_details_dialog(self, book_details) -> None:
        dialog = BookDetailsView()
        dialog.set_book_info(book_details)

        dialog.update_btn.clicked.connect(
            lambda: self.update_book.emit(dialog.get_book_info())
        )
        dialog.update_btn.clicked.connect(dialog.close)

        dialog.delete_btn.clicked.connect(dialog.close)
        dialog.delete_btn.clicked.connect(
            lambda: self.delete_book.emit(int(dialog.Id_line.text()))
        )

        dialog.show()

    # Search Dialog
    def show_search_dialog(self) -> None:
        self.dialog = SearchView()
        self.dialog.search_btn.clicked.connect(
            lambda: self.search_signal.emit(self.dialog.search_line.text())
        )
        self.dialog.books_table.doubleClicked.connect(self.handle_search_double_click)
        dialog.show()    # not blocking
        #dialog.exec()    # blocking

    def update_book_search_table(self, books: list) -> None:
        self.dialog.set_table(books)

    def handle_search_double_click(self, index):
        row = index.row()
        book_title = self.dialog.books_table.item(row, 0).text()
        self.add_from_search.emit(book_title)
