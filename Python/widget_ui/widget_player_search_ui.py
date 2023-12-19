# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_player_search.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form_PlayerStatistics(object):
    def setupUi(self, Form_PlayerStatistics):
        if not Form_PlayerStatistics.objectName():
            Form_PlayerStatistics.setObjectName(u"Form_PlayerStatistics")
        Form_PlayerStatistics.resize(1129, 623)
        self.verticalLayout = QVBoxLayout(Form_PlayerStatistics)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_PlayerStatistics = QLabel(Form_PlayerStatistics)
        self.label_PlayerStatistics.setObjectName(u"label_PlayerStatistics")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_PlayerStatistics.setFont(font)
        self.label_PlayerStatistics.setLayoutDirection(Qt.LeftToRight)
        self.label_PlayerStatistics.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_PlayerStatistics)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.tw_TeamsAndPlayers = QTreeWidget(Form_PlayerStatistics)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tw_TeamsAndPlayers.setHeaderItem(__qtreewidgetitem)
        self.tw_TeamsAndPlayers.setObjectName(u"tw_TeamsAndPlayers")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_TeamsAndPlayers.sizePolicy().hasHeightForWidth())
        self.tw_TeamsAndPlayers.setSizePolicy(sizePolicy)
        self.tw_TeamsAndPlayers.setRootIsDecorated(True)
        self.tw_TeamsAndPlayers.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.tw_TeamsAndPlayers)

        self.chart_area = QWidget(Form_PlayerStatistics)
        self.chart_area.setObjectName(u"chart_area")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chart_area.sizePolicy().hasHeightForWidth())
        self.chart_area.setSizePolicy(sizePolicy1)
        self.chart_area_layout = QVBoxLayout(self.chart_area)
        self.chart_area_layout.setObjectName(u"chart_area_layout")

        self.horizontalLayout.addWidget(self.chart_area)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form_PlayerStatistics)

        QMetaObject.connectSlotsByName(Form_PlayerStatistics)
    # setupUi

    def retranslateUi(self, Form_PlayerStatistics):
        Form_PlayerStatistics.setWindowTitle(QCoreApplication.translate("Form_PlayerStatistics", u"Form", None))
        self.label_PlayerStatistics.setText(QCoreApplication.translate("Form_PlayerStatistics", u"Player statistics", None))
#if QT_CONFIG(tooltip)
        self.chart_area.setToolTip(QCoreApplication.translate("Form_PlayerStatistics", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

