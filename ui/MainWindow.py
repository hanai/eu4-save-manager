# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 300)
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(55, 0))
        self.label.setStyleSheet(u"margin-right:20;")

        self.horizontalLayout.addWidget(self.label)

        self.label_saveDir = QLabel(self.centralwidget)
        self.label_saveDir.setObjectName(u"label_saveDir")
        self.label_saveDir.setMargin(0)

        self.horizontalLayout.addWidget(self.label_saveDir)

        self.pushButton_selectSaveDir = QPushButton(self.centralwidget)
        self.pushButton_selectSaveDir.setObjectName(u"pushButton_selectSaveDir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_selectSaveDir.sizePolicy().hasHeightForWidth())
        self.pushButton_selectSaveDir.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.pushButton_selectSaveDir)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, -1)
        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")
        sizePolicy1.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.pushButton_run, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 600, 23))
        self.menu_help = QMenu(self.menuBar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_file = QMenu(self.menuBar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_help)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.action_about)
        self.menu_file.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6b27\u9646\u98ce\u4e914 \u5b58\u6863\u7ba1\u7406\u5668", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b58\u6863\u6587\u4ef6\u6240\u5728\u76ee\u5f55", None))
        self.label_saveDir.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_selectSaveDir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

