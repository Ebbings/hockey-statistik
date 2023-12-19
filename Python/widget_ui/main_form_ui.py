# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLayout,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1170, 859)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 228, 763))
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents.setStyleSheet(u"QPushButton { min-height: 40px; }")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pb_TeamStat = QPushButton(self.scrollAreaWidgetContents)
        self.pb_TeamStat.setObjectName(u"pb_TeamStat")
        sizePolicy3.setHeightForWidth(self.pb_TeamStat.sizePolicy().hasHeightForWidth())
        self.pb_TeamStat.setSizePolicy(sizePolicy3)
        self.pb_TeamStat.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pb_TeamStat)

        self.pb_PlayerStat = QPushButton(self.scrollAreaWidgetContents)
        self.pb_PlayerStat.setObjectName(u"pb_PlayerStat")
        sizePolicy3.setHeightForWidth(self.pb_PlayerStat.sizePolicy().hasHeightForWidth())
        self.pb_PlayerStat.setSizePolicy(sizePolicy3)
        self.pb_PlayerStat.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pb_PlayerStat)

        self.pb_EventStat = QPushButton(self.scrollAreaWidgetContents)
        self.pb_EventStat.setObjectName(u"pb_EventStat")
        sizePolicy3.setHeightForWidth(self.pb_EventStat.sizePolicy().hasHeightForWidth())
        self.pb_EventStat.setSizePolicy(sizePolicy3)
        self.pb_EventStat.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pb_EventStat)

        self.pb_AddData = QPushButton(self.scrollAreaWidgetContents)
        self.pb_AddData.setObjectName(u"pb_AddData")
        sizePolicy3.setHeightForWidth(self.pb_AddData.sizePolicy().hasHeightForWidth())
        self.pb_AddData.setSizePolicy(sizePolicy3)
        self.pb_AddData.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pb_AddData)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.pb_ConnectToDb = QPushButton(self.groupBox)
        self.pb_ConnectToDb.setObjectName(u"pb_ConnectToDb")
        sizePolicy3.setHeightForWidth(self.pb_ConnectToDb.sizePolicy().hasHeightForWidth())
        self.pb_ConnectToDb.setSizePolicy(sizePolicy3)
        self.pb_ConnectToDb.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.pb_ConnectToDb)

        self.pb_ConnectToDb.raise_()
        self.scrollArea.raise_()

        self.horizontalLayout.addWidget(self.groupBox)

        self.gb_Content = QGroupBox(self.centralwidget)
        self.gb_Content.setObjectName(u"gb_Content")
        self.gb_Content.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.gb_Content)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sw_Content = QStackedWidget(self.gb_Content)
        self.sw_Content.setObjectName(u"sw_Content")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sw_Content.sizePolicy().hasHeightForWidth())
        self.sw_Content.setSizePolicy(sizePolicy4)
        self.sw_Content.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.sw_Content)

        self.textEdit = QTextEdit(self.gb_Content)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy4.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy4)
        self.textEdit.setMinimumSize(QSize(0, 130))
        self.textEdit.setMaximumSize(QSize(16777215, 130))
        self.textEdit.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.textEdit)


        self.horizontalLayout.addWidget(self.gb_Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sw_Content.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.pb_TeamStat.setText(QCoreApplication.translate("MainWindow", u"Team statistics", None))
        self.pb_PlayerStat.setText(QCoreApplication.translate("MainWindow", u"Player statistics", None))
        self.pb_EventStat.setText(QCoreApplication.translate("MainWindow", u"Event statistics", None))
        self.pb_AddData.setText(QCoreApplication.translate("MainWindow", u"Add Data", None))
        self.pb_ConnectToDb.setText(QCoreApplication.translate("MainWindow", u"Connect to DB", None))
        self.gb_Content.setTitle("")
    # retranslateUi

