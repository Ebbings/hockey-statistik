# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_data.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1237, 848)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_Headder = QLabel(Form)
        self.label_Headder.setObjectName(u"label_Headder")

        self.horizontalLayout_2.addWidget(self.label_Headder)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cb_SqlTables = QComboBox(Form)
        self.cb_SqlTables.addItem("")
        self.cb_SqlTables.setObjectName(u"cb_SqlTables")
        self.cb_SqlTables.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_3.addWidget(self.cb_SqlTables)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.pb_PreviousPage = QPushButton(Form)
        self.pb_PreviousPage.setObjectName(u"pb_PreviousPage")

        self.horizontalLayout_4.addWidget(self.pb_PreviousPage)

        self.sb_CurrentPage = QSpinBox(Form)
        self.sb_CurrentPage.setObjectName(u"sb_CurrentPage")
        self.sb_CurrentPage.setMinimum(1)
        self.sb_CurrentPage.setMaximum(1)

        self.horizontalLayout_4.addWidget(self.sb_CurrentPage)

        self.label_MaxNumberOfPages = QLabel(Form)
        self.label_MaxNumberOfPages.setObjectName(u"label_MaxNumberOfPages")

        self.horizontalLayout_4.addWidget(self.label_MaxNumberOfPages)

        self.pb_NextPage = QPushButton(Form)
        self.pb_NextPage.setObjectName(u"pb_NextPage")

        self.horizontalLayout_4.addWidget(self.pb_NextPage)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_RowsPerPage = QLabel(Form)
        self.label_RowsPerPage.setObjectName(u"label_RowsPerPage")

        self.horizontalLayout_5.addWidget(self.label_RowsPerPage)

        self.sb_RowsPerPage = QSpinBox(Form)
        self.sb_RowsPerPage.setObjectName(u"sb_RowsPerPage")
        self.sb_RowsPerPage.setMinimum(1)
        self.sb_RowsPerPage.setMaximum(10000)
        self.sb_RowsPerPage.setValue(100)

        self.horizontalLayout_5.addWidget(self.sb_RowsPerPage)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tw_DataToInsert = QTableWidget(Form)
        self.tw_DataToInsert.setObjectName(u"tw_DataToInsert")

        self.verticalLayout.addWidget(self.tw_DataToInsert)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_AddRow = QPushButton(Form)
        self.pb_AddRow.setObjectName(u"pb_AddRow")

        self.horizontalLayout.addWidget(self.pb_AddRow)

        self.pb_SaveRow = QPushButton(Form)
        self.pb_SaveRow.setObjectName(u"pb_SaveRow")

        self.horizontalLayout.addWidget(self.pb_SaveRow)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_AddNewColumn = QPushButton(Form)
        self.pb_AddNewColumn.setObjectName(u"pb_AddNewColumn")

        self.horizontalLayout.addWidget(self.pb_AddNewColumn)

        self.pb_DeleteColumn = QPushButton(Form)
        self.pb_DeleteColumn.setObjectName(u"pb_DeleteColumn")

        self.horizontalLayout.addWidget(self.pb_DeleteColumn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_Headder.setText(QCoreApplication.translate("Form", u"Edit Data", None))
        self.cb_SqlTables.setItemText(0, QCoreApplication.translate("Form", u"Chose a table", None))

        self.pb_PreviousPage.setText(QCoreApplication.translate("Form", u"Previous page", None))
        self.label_MaxNumberOfPages.setText(QCoreApplication.translate("Form", u"/ 1", None))
        self.pb_NextPage.setText(QCoreApplication.translate("Form", u"Next page", None))
        self.label_RowsPerPage.setText(QCoreApplication.translate("Form", u"Rows per page", None))
        self.pb_AddRow.setText(QCoreApplication.translate("Form", u"Add new row to database", None))
        self.pb_SaveRow.setText(QCoreApplication.translate("Form", u"Save new row to database", None))
        self.pb_AddNewColumn.setText(QCoreApplication.translate("Form", u"Add new column", None))
        self.pb_DeleteColumn.setText(QCoreApplication.translate("Form", u"Delete column", None))
    # retranslateUi

