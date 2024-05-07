from typing import Dict
from PySide6.QtCore import Signal, QUrl
from PySide6.QtWidgets import QDialog, QPushButton
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtGui import QPixmap

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
            lambda: self.delete_book.emit(int(self.Id_line.text()))
        )
        self.update_btn.clicked.connect(
            lambda: self.update_book.emit(self.get_book_info())
        )
        self.close_btn.clicked.connect(self.close)

    def get_book_info(self) -> Dict[str, str]:
        book_dict = {
            "id": self.Id_line.text(),
            # "title": self.title_edit.text(),
            "author": self.author_line.text(),
            "pages": self.pages_line.text(),
            "publishYear": self.year_line.text(),
            "comments": self.comments_edit.toPlainText(),
            # "picture_url": self.picture_url.text()
        }
        return book_dict

    def set_book_info(self, book_dict: Dict[str, str]) -> None:
        # self.title_edit.setText(book_dict["title"])
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

        self.download_and_display_cover(book_dict["cover"])

    def download_and_display_cover(self, url):
        # Create a network access manager
        network_manager = QNetworkAccessManager(self)

        # Send a request to download the image
        url = QUrl(url)
        request = QNetworkRequest(url)
        reply = network_manager.get(request)

        # When the reply is finished, display the image
        reply.finished.connect(lambda: self.display_cover(reply))

    def display_cover(self, reply):
        # Check if the request was successful
        if reply.error() == QNetworkReply.NetworkError.NoError:
            # Read the image data from the reply
            image_data = reply.readAll()

            # Create a pixmap from the image data
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            # Set the pixmap to the QLabel
            self.image_view.setPixmap(pixmap)
            self.image_view.setScaledContents(True)
