from typing import Dict
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from ui.add_book_ui import Ui_add_book_window


class AddBookView(QDialog, Ui_add_book_window):
    add_book = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.close_btn.clicked.connect(self.close)

    def sendAddBookEvent(self):
        self.add_book.emit(self.get_book_info())
        self.close()

    def get_book_info(self) -> Dict[str, str]:
        book_dict = {
            "title": self.title_line.text(),
            "author": self.author_line.text(),
            "pages": self.pages_line.text(),
            "publishYear": self.year_line.text(),
            "comments": self.comment_edit.toPlainText(),
            "cover": self.image_url_line.text(),
        }
        return book_dict
