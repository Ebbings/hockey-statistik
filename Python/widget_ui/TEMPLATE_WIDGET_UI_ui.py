# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TEMPLATE_WIDGET_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_TEMPLATE(object):
    def setupUi(self, TEMPLATE):
        if not TEMPLATE.objectName():
            TEMPLATE.setObjectName(u"TEMPLATE")
        TEMPLATE.resize(391, 307)
        self.verticalLayout = QVBoxLayout(TEMPLATE)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tl_ChangeLabel = QLabel(TEMPLATE)
        self.tl_ChangeLabel.setObjectName(u"tl_ChangeLabel")

        self.horizontalLayout.addWidget(self.tl_ChangeLabel)

        self.le_ChangeText = QLineEdit(TEMPLATE)
        self.le_ChangeText.setObjectName(u"le_ChangeText")

        self.horizontalLayout.addWidget(self.le_ChangeText)

        self.pb_ChangeButton = QPushButton(TEMPLATE)
        self.pb_ChangeButton.setObjectName(u"pb_ChangeButton")

        self.horizontalLayout.addWidget(self.pb_ChangeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(TEMPLATE)

        QMetaObject.connectSlotsByName(TEMPLATE)
    # setupUi

    def retranslateUi(self, TEMPLATE):
        TEMPLATE.setWindowTitle(QCoreApplication.translate("TEMPLATE", u"Form", None))
        self.tl_ChangeLabel.setText(QCoreApplication.translate("TEMPLATE", u"Change me", None))
        self.pb_ChangeButton.setText(QCoreApplication.translate("TEMPLATE", u"Change", None))
    # retranslateUi

