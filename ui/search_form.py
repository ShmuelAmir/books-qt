# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_search_form(object):
    def setupUi(self, search_form):
        if not search_form.objectName():
            search_form.setObjectName(u"search_form")
        search_form.resize(600, 600)
        self.layoutWidget = QWidget(search_form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 601, 601))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(26, 0, 20, 0)
        self.function_frame = QFrame(self.layoutWidget)
        self.function_frame.setObjectName(u"function_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.function_frame.sizePolicy().hasHeightForWidth())
        self.function_frame.setSizePolicy(sizePolicy)
        self.function_frame.setMinimumSize(QSize(550, 0))
        self.function_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.function_frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_line = QLineEdit(self.function_frame)
        self.search_line.setObjectName(u"search_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy1)
        self.search_line.setMinimumSize(QSize(250, 30))

        self.horizontalLayout.addWidget(self.search_line)

        self.search_btn = QPushButton(self.function_frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(150, 30))
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon(QIcon.fromTheme(u"search"))
        self.search_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.search_btn)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.function_frame)

        self.books_table = QTableWidget(self.layoutWidget)
        if (self.books_table.columnCount() < 4):
            self.books_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.books_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.books_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.books_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.books_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.books_table.setObjectName(u"books_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.books_table.sizePolicy().hasHeightForWidth())
        self.books_table.setSizePolicy(sizePolicy2)
        self.books_table.setMinimumSize(QSize(550, 500))
        self.books_table.setMaximumSize(QSize(550, 500))
        self.books_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.books_table.setShowGrid(False)
        self.books_table.horizontalHeader().setCascadingSectionResizes(False)
        self.books_table.horizontalHeader().setMinimumSectionSize(0)
        self.books_table.horizontalHeader().setDefaultSectionSize(125)
        self.books_table.horizontalHeader().setStretchLastSection(True)
        self.books_table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.books_table)


        self.retranslateUi(search_form)

        QMetaObject.connectSlotsByName(search_form)
    # setupUi

    def retranslateUi(self, search_form):
        search_form.setWindowTitle(QCoreApplication.translate("search_form", u"Search Form", None))
        self.search_line.setText("")
        self.search_line.setPlaceholderText(QCoreApplication.translate("search_form", u"Search a book by name or author", None))
        self.search_btn.setText(QCoreApplication.translate("search_form", u"Search", None))
        ___qtablewidgetitem = self.books_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("search_form", u"Title", None));
        ___qtablewidgetitem1 = self.books_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("search_form", u"Author", None));
        ___qtablewidgetitem2 = self.books_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("search_form", u"Pages", None));
        ___qtablewidgetitem3 = self.books_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("search_form", u"Rating", None));
    # retranslateUi

