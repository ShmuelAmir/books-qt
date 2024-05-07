# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_book.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_add_book_window(object):
    def setupUi(self, add_book_window):
        if not add_book_window.objectName():
            add_book_window.setObjectName(u"add_book_window")
        add_book_window.resize(388, 581)
        add_book_window.setStyleSheet(u"#function_frame QPushButton{\n"
"	font-size: 14px;\n"
"	padding: 5px 10px;\n"
"	border: 2px solid #f0f0f0;\n"
"	border-radius: 5px;\n"
"	background-color: #84e8f7;\n"
"}\n"
"\n"
"#function_frame #delete_btn{\n"
"	background-color: #ff8183;\n"
"}\n"
"\n"
"#function_frame QPushButton::hover{\n"
"	border-color: #4c96f7;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"\n"
"#function_frame #delete_button::hover{\n"
"	border-color: #dc0004;\n"
"}\n"
"\n"
"\n"
"\n"
"#image_frame QLabel{\n"
"	background-color: white;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(add_book_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(add_book_window)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.header_label = QLabel(self.header_frame)
        self.header_label.setObjectName(u"header_label")
        self.header_label.setGeometry(QRect(80, 10, 191, 48))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(30)
        font.setItalic(False)
        self.header_label.setFont(font)
        self.header_label.setScaledContents(False)
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setWordWrap(False)

        self.verticalLayout.addWidget(self.header_frame)

        self.info_frame = QFrame(add_book_window)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.info_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 261, 201))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.author_line = QLineEdit(self.layoutWidget)
        self.author_line.setObjectName(u"author_line")
        font1 = QFont()
        font1.setPointSize(11)
        self.author_line.setFont(font1)

        self.gridLayout_3.addWidget(self.author_line, 1, 2, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)

        self.title_line = QLineEdit(self.layoutWidget)
        self.title_line.setObjectName(u"title_line")
        self.title_line.setFont(font1)

        self.gridLayout_3.addWidget(self.title_line, 0, 2, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 1)

        self.image_url_line = QLineEdit(self.layoutWidget)
        self.image_url_line.setObjectName(u"image_url_line")
        self.image_url_line.setFont(font1)

        self.gridLayout_3.addWidget(self.image_url_line, 3, 2, 1, 1)

        self.year_line = QLineEdit(self.layoutWidget)
        self.year_line.setObjectName(u"year_line")
        self.year_line.setFont(font1)

        self.gridLayout_3.addWidget(self.year_line, 2, 2, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 2)

        self.pages_line = QLineEdit(self.layoutWidget)
        self.pages_line.setObjectName(u"pages_line")
        self.pages_line.setFont(font1)

        self.gridLayout_3.addWidget(self.pages_line, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.info_frame)

        self.frame_2 = QFrame(add_book_window)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comment_edit = QTextEdit(self.frame_2)
        self.comment_edit.setObjectName(u"comment_edit")
        self.comment_edit.setGeometry(QRect(10, 30, 341, 101))
        self.comment_edit.setFont(font1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 0, 111, 21))
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)

        self.verticalLayout.addWidget(self.frame_2)

        self.function_frame = QFrame(add_book_window)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setFrameShape(QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.function_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.close_btn = QPushButton(self.function_frame)
        self.close_btn.setObjectName(u"close_btn")
        icon = QIcon()
        icon.addFile(u"../.designer/.designer/backup/icons/published_with_changes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.close_btn)

        self.add_btn = QPushButton(self.function_frame)
        self.add_btn.setObjectName(u"add_btn")
        icon1 = QIcon()
        icon1.addFile(u"../.designer/.designer/backup/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.add_btn)


        self.verticalLayout.addWidget(self.function_frame)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(add_book_window)

        QMetaObject.connectSlotsByName(add_book_window)
    # setupUi

    def retranslateUi(self, add_book_window):
        add_book_window.setWindowTitle(QCoreApplication.translate("add_book_window", u"Form", None))
        self.header_label.setText(QCoreApplication.translate("add_book_window", u"Add Book", None))
        self.label_7.setText(QCoreApplication.translate("add_book_window", u"Author", None))
        self.label_6.setText(QCoreApplication.translate("add_book_window", u"Title", None))
        self.label_10.setText(QCoreApplication.translate("add_book_window", u"Pages", None))
        self.image_url_line.setText("")
        self.label_8.setText(QCoreApplication.translate("add_book_window", u"Year", None))
        self.label_9.setText(QCoreApplication.translate("add_book_window", u"Image url", None))
        self.label.setText(QCoreApplication.translate("add_book_window", u"Comments", None))
        self.close_btn.setText(QCoreApplication.translate("add_book_window", u"Close", None))
        self.add_btn.setText(QCoreApplication.translate("add_book_window", u"Add", None))
    # retranslateUi

