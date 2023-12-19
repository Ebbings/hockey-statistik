# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_event_search.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1238, 633)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.cb_TeamName = QComboBox(Form)
        self.cb_TeamName.addItem("")
        self.cb_TeamName.setObjectName(u"cb_TeamName")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_TeamName.sizePolicy().hasHeightForWidth())
        self.cb_TeamName.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.cb_TeamName)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.cb_Season = QComboBox(Form)
        self.cb_Season.setObjectName(u"cb_Season")
        sizePolicy.setHeightForWidth(self.cb_Season.sizePolicy().hasHeightForWidth())
        self.cb_Season.setSizePolicy(sizePolicy)

        self.verticalLayout_4.addWidget(self.cb_Season)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.tb_HideColumns = QToolButton(Form)
        self.tb_HideColumns.setObjectName(u"tb_HideColumns")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_HideColumns.sizePolicy().hasHeightForWidth())
        self.tb_HideColumns.setSizePolicy(sizePolicy2)
        self.tb_HideColumns.setLayoutDirection(Qt.LeftToRight)
        self.tb_HideColumns.setCheckable(False)
        self.tb_HideColumns.setAutoRepeat(False)

        self.verticalLayout_2.addWidget(self.tb_HideColumns)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tw_Team_Season = QTableWidget(Form)
        self.tw_Team_Season.setObjectName(u"tw_Team_Season")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tw_Team_Season.sizePolicy().hasHeightForWidth())
        self.tw_Team_Season.setSizePolicy(sizePolicy3)
        self.tw_Team_Season.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_Team_Season.setSortingEnabled(True)

        self.verticalLayout_5.addWidget(self.tw_Team_Season)


        self.verticalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Team", None))
        self.cb_TeamName.setItemText(0, "")

        self.label_2.setText(QCoreApplication.translate("Form", u"Season", None))
        self.label_3.setText("")
        self.tb_HideColumns.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi

