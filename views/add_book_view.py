from typing import Dict
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.add_book_ui import Ui_add_book_window


class AddBookView(QDialog, Ui_add_book_window):
    add_book = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.add_btn.clicked.connect(lambda: self.add_book.emit(self.get_book_info()))
        # self.cancel_btn.clicked.connect(self.close)

    def get_book_info(self) -> Dict[str, str]:
        book_dict = {
            "title": self.book_title.text(),
            "author": self.book_author.text(),
            "genre": self.book_genre.text(),
            "year": self.book_year.text(),
            "comments": self.book_comments.toPlainText(),
            "picture_url": self.picture_url.text(),
        }
        return book_dict
