# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'books.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(958, 752)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#info_frame{\n"
"	background-color: #fff;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#info_frame Qlabel,\n"
"#info_frame QLineEdit,\n"
"#info_frame QcomboBox,\n"
"#function_frame QPushButton,\n"
"QHeaderView::section{\n"
"	font-family: Segoe  UI Semibold;\n"
"	font-size: 12px;\n"
"}\n"
"\n"
"\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox{\n"
"	padding: 4px 5px;\n"
"	border: 1px solid #838383;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#info_frame QlineEdit:focus,\n"
"#info_frame QComboBox:focus{\n"
"	border-color: #0055ff;\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down{\n"
"	background: transparent;\n"
"	border: none;\n"
"	margin-right: 5px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(/icons/expand_more.svg);\n"
"}\n"
"\n"
"\n"
"#result_frame{\n"
"	border-radius: 5px;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	border-radius: 3px;\n"
"	border: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"	border: none;\n"
"	border-bottom: 1px solid #"
                        "d0c6ff;\n"
"	text-align: left;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-bottom: 1px solid #d0c6ff;\n"
"	color: #000;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"#function_frame QPushButton{\n"
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
"}")
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(20, 10, 20, 10)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.header_label = QLabel(self.frame)
        self.header_label.setObjectName(u"header_label")
        font1 = QFont()
        font1.setFamilies([u"Sitka"])
        font1.setPointSize(30)
        font1.setItalic(False)
        self.header_label.setFont(font1)
        self.header_label.setScaledContents(False)
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.header_label)

        self.splitter.addWidget(self.frame)
        self.function_frame = QFrame(self.splitter)
        self.function_frame.setObjectName(u"function_frame")
        self.function_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.function_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.function_frame)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 10, 30, 10)
        self.add_btn = QPushButton(self.function_frame)
        self.add_btn.setObjectName(u"add_btn")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        self.add_btn.setFont(font2)
        icon = QIcon()
        icon.addFile(u"../.designer/.designer/backup/icons/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.add_btn)

        self.search_line = QLineEdit(self.function_frame)
        self.search_line.setObjectName(u"search_line")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setMinimumSize(QSize(250, 30))
        font3 = QFont()
        font3.setPointSize(11)
        self.search_line.setFont(font3)

        self.horizontalLayout_3.addWidget(self.search_line)

        self.splitter.addWidget(self.function_frame)
        self.result_frame = QFrame(self.splitter)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.result_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.books_table = QTableWidget(self.result_frame)
        if (self.books_table.columnCount() < 5):
            self.books_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font3);
        self.books_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font3);
        self.books_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font3);
        self.books_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font3);
        self.books_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font3);
        self.books_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.books_table.setObjectName(u"books_table")
        self.books_table.setMinimumSize(QSize(900, 0))
        self.books_table.setMaximumSize(QSize(1131, 451))
        self.books_table.setFont(font3)
        self.books_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.books_table.setShowGrid(False)
        self.books_table.horizontalHeader().setCascadingSectionResizes(False)
        self.books_table.horizontalHeader().setMinimumSectionSize(50)
        self.books_table.horizontalHeader().setDefaultSectionSize(180)
        self.books_table.horizontalHeader().setStretchLastSection(True)
        self.books_table.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.books_table)

        self.splitter.addWidget(self.result_frame)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 958, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSearch)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.header_label.setText(QCoreApplication.translate("MainWindow", u"Books Information System", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        ___qtablewidgetitem = self.books_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.books_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.books_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Author", None));
        ___qtablewidgetitem3 = self.books_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Year", None));
        ___qtablewidgetitem4 = self.books_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pages", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

