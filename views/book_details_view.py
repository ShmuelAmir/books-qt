from typing import Dict
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap, QIntValidator

from ui.book_details_ui import Ui_Form


class BookDetailsView(QDialog, Ui_Form):
    delete_book = Signal(int)
    update_book = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Book Details")

        self.Id_line.setReadOnly(True)
        self.year_line.setValidator(QIntValidator())
        self.pages_line.setValidator(QIntValidator())

        self.close_btn.clicked.connect(self.close)

    def get_book_info(self) -> Dict[str, str]:
        book_dict = {
            "id": self.Id_line.text(),
            "author": self.author_line.text(),
            "pages": self.pages_line.text(),
            "publishYear": self.year_line.text(),
            "comments": self.comments_edit.toPlainText(),
        }
        return book_dict

    def set_book_info(self, book_dict: Dict[str, str]) -> None:
        self.title_label.setText(book_dict["title"])
        self.Id_line.setText(str(book_dict["id"]))
        self.author_line.setText(book_dict["author"])
        self.pages_line.setText(str(book_dict["pages"]))
        self.year_line.setText(str(book_dict["publishYear"]))

        self.comments_edit.setPlainText(
            book_dict["comments"][0]["text"] if book_dict["comments"] else ""
        )

        for i in range(5):
            tag = book_dict["imaggaTags"][i]["tag"]
            confidence = book_dict["imaggaTags"][i]["confidence"]
            self.__dict__[f"tag{i+1}_label"].setText(tag)
            # i want only 3 decimal places and add "%" to the confidence:
            self.__dict__[f"tag{i+1}_value_label"].setText(f"{confidence:.3f}%")

        pixmap = QPixmap()
        pixmap.loadFromData(book_dict["cover_bytes"])

        self.image_view.setPixmap(pixmap)
        self.image_view.setScaledContents(True)
