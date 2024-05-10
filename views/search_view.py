from PySide6.QtWidgets import QDialog, QTableWidgetItem
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

from ui.search_form import Ui_search_form


class SearchView(QDialog, Ui_search_form):
    search_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def set_table(self, books):
        self.books_table.setRowCount(0)
        for row, book in enumerate(books):
            self.books_table.insertRow(row)
            self.books_table.setItem(row, 0, QTableWidgetItem(book["title"]))
            self.books_table.setItem(row, 1, QTableWidgetItem(book["author"]))
            self.books_table.setItem(row, 2, QTableWidgetItem(str(book["pages"])))
            self.books_table.setItem(row, 3, QTableWidgetItem(str(book["rating"])))
