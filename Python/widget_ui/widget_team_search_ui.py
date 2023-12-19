# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_team_search.ui'
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

class Ui_Form_TeamStatistics(object):
    def setupUi(self, Form_TeamStatistics):
        if not Form_TeamStatistics.objectName():
            Form_TeamStatistics.setObjectName(u"Form_TeamStatistics")
        Form_TeamStatistics.resize(1129, 623)
        self.verticalLayout = QVBoxLayout(Form_TeamStatistics)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_TeamStatistics = QLabel(Form_TeamStatistics)
        self.label_TeamStatistics.setObjectName(u"label_TeamStatistics")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_TeamStatistics.setFont(font)
        self.label_TeamStatistics.setLayoutDirection(Qt.LeftToRight)
        self.label_TeamStatistics.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_TeamStatistics)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.tw_Teams = QTreeWidget(Form_TeamStatistics)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tw_Teams.setHeaderItem(__qtreewidgetitem)
        self.tw_Teams.setObjectName(u"tw_Teams")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_Teams.sizePolicy().hasHeightForWidth())
        self.tw_Teams.setSizePolicy(sizePolicy)
        self.tw_Teams.setRootIsDecorated(True)
        self.tw_Teams.setHeaderHidden(True)

        self.horizontalLayout.addWidget(self.tw_Teams)

        self.chart_area = QWidget(Form_TeamStatistics)
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


        self.retranslateUi(Form_TeamStatistics)

        QMetaObject.connectSlotsByName(Form_TeamStatistics)
    # setupUi

    def retranslateUi(self, Form_TeamStatistics):
        Form_TeamStatistics.setWindowTitle(QCoreApplication.translate("Form_TeamStatistics", u"Form", None))
        self.label_TeamStatistics.setText(QCoreApplication.translate("Form_TeamStatistics", u"Team statistics", None))
#if QT_CONFIG(tooltip)
        self.chart_area.setToolTip(QCoreApplication.translate("Form_TeamStatistics", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

