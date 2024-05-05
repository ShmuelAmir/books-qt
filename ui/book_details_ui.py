# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_details.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 766)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"#function_frame QPushButton{\n"
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
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.title_label = QLabel(self.frame_4)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(210, 10, 191, 48))
        font = QFont()
        font.setFamilies([u"Sitka"])
        font.setPointSize(30)
        font.setItalic(False)
        self.title_label.setFont(font)
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.info_frame = QFrame(Form)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.info_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 20, 30, 20)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.label_2 = QLabel(self.info_frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.Id_line = QLineEdit(self.info_frame)
        self.Id_line.setObjectName(u"Id_line")

        self.gridLayout.addWidget(self.Id_line, 0, 1, 1, 1)

        self.author_line = QLineEdit(self.info_frame)
        self.author_line.setObjectName(u"author_line")

        self.gridLayout.addWidget(self.author_line, 1, 1, 1, 1)

        self.label_3 = QLabel(self.info_frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.label_5 = QLabel(self.info_frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.year_line = QLineEdit(self.info_frame)
        self.year_line.setObjectName(u"year_line")

        self.gridLayout_2.addWidget(self.year_line, 0, 1, 1, 1)

        self.genre_combo = QComboBox(self.info_frame)
        self.genre_combo.setObjectName(u"genre_combo")

        self.gridLayout_2.addWidget(self.genre_combo, 1, 1, 1, 1)

        self.label_4 = QLabel(self.info_frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.info_frame)

        self.image_frame = QFrame(Form)
        self.image_frame.setObjectName(u"image_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_frame.sizePolicy().hasHeightForWidth())
        self.image_frame.setSizePolicy(sizePolicy1)
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.image_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 10, 381, 241))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.image_view = QGraphicsView(self.layoutWidget)
        self.image_view.setObjectName(u"image_view")
        self.image_view.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_3.addWidget(self.image_view)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tag1_label = QLabel(self.layoutWidget)
        self.tag1_label.setObjectName(u"tag1_label")
        self.tag1_label.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.tag1_label)

        self.tag2_label = QLabel(self.layoutWidget)
        self.tag2_label.setObjectName(u"tag2_label")
        self.tag2_label.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.tag2_label)

        self.tag3_label = QLabel(self.layoutWidget)
        self.tag3_label.setObjectName(u"tag3_label")
        self.tag3_label.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.tag3_label)

        self.tag4_label = QLabel(self.layoutWidget)
        self.tag4_label.setObjectName(u"tag4_label")
        self.tag4_label.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.tag4_label)

        self.tag5_label = QLabel(self.layoutWidget)
        self.tag5_label.setObjectName(u"tag5_label")
        self.tag5_label.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.tag5_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tag1_value_label = QLabel(self.layoutWidget)
        self.tag1_value_label.setObjectName(u"tag1_value_label")
        self.tag1_value_label.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.tag1_value_label)

        self.tag2_value_label = QLabel(self.layoutWidget)
        self.tag2_value_label.setObjectName(u"tag2_value_label")
        self.tag2_value_label.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.tag2_value_label)

        self.tag3_value_label = QLabel(self.layoutWidget)
        self.tag3_value_label.setObjectName(u"tag3_value_label")
        self.tag3_value_label.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.tag3_value_label)

        self.tag4_value_label = QLabel(self.layoutWidget)
        self.tag4_value_label.setObjectName(u"tag4_value_label")
        self.tag4_value_label.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.tag4_value_label)

        self.tag5_value_label = QLabel(self.layoutWidget)
        self.tag5_value_label.setObjectName(u"tag5_value_label")
        self.tag5_value_label.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_2.addWidget(self.tag5_value_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.image_frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comments_edit = QTextEdit(self.frame_2)
        self.comments_edit.setObjectName(u"comments_edit")
        self.comments_edit.setGeometry(QRect(40, 10, 521, 131))

        self.verticalLayout_3.addWidget(self.frame_2)

        self.function_frame = QFrame(Form)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setFrameShape(QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.function_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.close_btn = QPushButton(self.function_frame)
        self.close_btn.setObjectName(u"close_btn")
        icon = QIcon()
        icon.addFile(u"icons/published_with_changes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.close_btn)

        self.update_btn = QPushButton(self.function_frame)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.update_btn)

        self.delete_btn = QPushButton(self.function_frame)
        self.delete_btn.setObjectName(u"delete_btn")
        icon1 = QIcon()
        icon1.addFile(u"icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_btn)


        self.verticalLayout_3.addWidget(self.function_frame)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.setStretch(2, 7)
        self.verticalLayout_3.setStretch(3, 4)
        self.verticalLayout_3.setStretch(4, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Id", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Author", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Genre", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Year", None))
        self.tag1_label.setText(QCoreApplication.translate("Form", u"tag1", None))
        self.tag2_label.setText(QCoreApplication.translate("Form", u"tag2", None))
        self.tag3_label.setText(QCoreApplication.translate("Form", u"tag3", None))
        self.tag4_label.setText(QCoreApplication.translate("Form", u"tag4", None))
        self.tag5_label.setText(QCoreApplication.translate("Form", u"tag5", None))
        self.tag1_value_label.setText(QCoreApplication.translate("Form", u"value", None))
        self.tag2_value_label.setText(QCoreApplication.translate("Form", u"value", None))
        self.tag3_value_label.setText(QCoreApplication.translate("Form", u"value", None))
        self.tag4_value_label.setText(QCoreApplication.translate("Form", u"value", None))
        self.tag5_value_label.setText(QCoreApplication.translate("Form", u"value", None))
        self.close_btn.setText(QCoreApplication.translate("Form", u"Close", None))
        self.update_btn.setText(QCoreApplication.translate("Form", u"Update", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

