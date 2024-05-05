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


class BooksView(QMainWindow):

    book_double_clicked = Signal(int)
    refresh_list = Signal()
    # add_book = Signal(dict)

    def __init__(self):
        super().__init__()
        self.ui = Books_UI()
        self.ui.setupUi(self)

        self.add_butn = self.ui.add_btn
        self.refresh_btn = self.ui.refresh_btn
        self.clear_btn = self.ui.clear_btn

        self.search_line = self.ui.search_line

        self.result_table = self.ui.books_table
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.ui.function_frame.findChildren(QPushButton)

        self.add_butn.clicked.connect(self.show_add_dialog)
        # self.refresh_btn.clicked.emit(self.refresh_list)

    def update_book_table(self, books: list) -> None:
        self.result_table.setRowCount(0)
        for row, book in enumerate(books):
            self.result_table.insertRow(row)
            self.result_table.setItem(row, 0, QTableWidgetItem(str(book["id"])))
            self.result_table.setItem(row, 1, QTableWidgetItem(book["title"]))
            self.result_table.setItem(row, 2, QTableWidgetItem(book["author"]))
            self.result_table.setItem(row, 3, QTableWidgetItem(book["publishYear"]))
            self.result_table.setItem(row, 4, QTableWidgetItem(str(book["pages"])))
        self.result_table.doubleClicked.connect(self.handle_double_click)

    def handle_double_click(self, index):
        row = index.row()
        book_id = int(self.result_table.item(row, 0).text())
        self.book_double_clicked.emit(book_id)

    def show_add_dialog(self) -> None:
        dialog = AddBookView()
        dialog.setWindowTitle("Add Book")
        # if dialog.exec() == QDialog.DialogCode.Accepted:
        #     book_dict = dialog.get_book_info()
        #     self.add_book.emit(book_dict)

    def show_book_details_dialog(self, book_details) -> None:
        dialog = BookDetailsView()
        dialog.setWindowTitle("Update Book")
        dialog.set_book_info(book_details)
        # if dialog.exec() == QDialog.DialogCode.Accepted:
        #     book_dict = dialog.get_book_info()
        #     self.update_book.emit(book_dict)
