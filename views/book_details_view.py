from typing import Dict
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QPushButton

from ui.book_details_ui import Ui_Form


class BookDetailsView(QDialog, Ui_Form):
    delete_book = Signal(int)
    update_book = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.book_id.setValidator(QIntValidator())  # Restrict input to integers
        self.buttons_list = self.function_frame.findChildren(QPushButton)

        self.delete_btn.clicked.connect(
            lambda: self.delete_book.emit(int(self.book_id.text()))
        )
        self.update_btn.clicked.connect(
            lambda: self.update_book.emit(self.get_book_info())
        )
        self.close_btn.clicked.connect(self.close)

    def get_book_info(self) -> Dict[str, str]:
        book_dict = {
            "id": self.book_id.text(),
            # "title": self.title_edit.text(),
            "author": self.author_edit.text(),
            "genre": self.genre_edit.text(),
            "year": self.year_edit.text(),
            "comments": self.comments_edit.toPlainText(),
            # "picture_url": self.picture_url.text()
        }
        return book_dict

    def set_book_info(self, book_dict: Dict[str, str]) -> None:
        # self.title_edit.setText(book_dict["title"])
        self.book_id.setText(str(book_dict["id"]))
        self.author_edit.setText(book_dict["author"])
        self.genre_edit.setText(book_dict["genre"])
        self.year_edit.setText(book_dict["year"])
        self.comments_edit.setPlainText(book_dict["comments"])
        self.tag1_name.setText(book_dict["tag1_name"])
        self.tag2_name.setText(book_dict["tag2_name"])
        self.tag3_name.setText(book_dict["tag3_name"])
        self.tag4_name.setText(book_dict["tag4_name"])
        self.tag5_name.setText(book_dict["tag5_name"])
        self.tag1_value.setText(book_dict["tag1_value"])
        self.tag2_value.setText(book_dict["tag2_value"])
        self.tag3_value.setText(book_dict["tag3_value"])
        self.tag4_value.setText(book_dict["tag4_value"])
        self.tag5_value.setText(book_dict["tag5_value"])
        self.picture_url.setPixmap(book_dict["picture_url"])
