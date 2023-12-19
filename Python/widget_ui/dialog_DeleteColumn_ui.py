# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_DeleteColumn.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog_DeleteColumn(object):
    def setupUi(self, Dialog_DeleteColumn):
        if not Dialog_DeleteColumn.objectName():
            Dialog_DeleteColumn.setObjectName(u"Dialog_DeleteColumn")
        Dialog_DeleteColumn.resize(400, 323)
        self.horizontalLayout_2 = QHBoxLayout(Dialog_DeleteColumn)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hl_MainDialogBody = QHBoxLayout()
        self.hl_MainDialogBody.setObjectName(u"hl_MainDialogBody")
        self.vl_DeleteColumns = QVBoxLayout()
        self.vl_DeleteColumns.setObjectName(u"vl_DeleteColumns")
        self.vl_DeleteColumns.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_DeleteColumns = QLabel(Dialog_DeleteColumn)
        self.label_DeleteColumns.setObjectName(u"label_DeleteColumns")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_DeleteColumns.sizePolicy().hasHeightForWidth())
        self.label_DeleteColumns.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_DeleteColumns.setFont(font)
        self.label_DeleteColumns.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.vl_DeleteColumns.addWidget(self.label_DeleteColumns)

        self.sa_ComboBoxes = QScrollArea(Dialog_DeleteColumn)
        self.sa_ComboBoxes.setObjectName(u"sa_ComboBoxes")
        self.sa_ComboBoxes.setFrameShape(QFrame.NoFrame)
        self.sa_ComboBoxes.setWidgetResizable(True)
        self.sa_WidgetContent = QWidget()
        self.sa_WidgetContent.setObjectName(u"sa_WidgetContent")
        self.sa_WidgetContent.setGeometry(QRect(0, 0, 297, 273))
        self.verticalLayout_3 = QVBoxLayout(self.sa_WidgetContent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vl_ComboBoxes = QVBoxLayout()
        self.vl_ComboBoxes.setObjectName(u"vl_ComboBoxes")

        self.verticalLayout_3.addLayout(self.vl_ComboBoxes)

        self.sa_ComboBoxes.setWidget(self.sa_WidgetContent)

        self.vl_DeleteColumns.addWidget(self.sa_ComboBoxes)


        self.hl_MainDialogBody.addLayout(self.vl_DeleteColumns)

        self.bBox_OK_Cancel = QDialogButtonBox(Dialog_DeleteColumn)
        self.bBox_OK_Cancel.setObjectName(u"bBox_OK_Cancel")
        self.bBox_OK_Cancel.setOrientation(Qt.Vertical)
        self.bBox_OK_Cancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.hl_MainDialogBody.addWidget(self.bBox_OK_Cancel)


        self.horizontalLayout_2.addLayout(self.hl_MainDialogBody)


        self.retranslateUi(Dialog_DeleteColumn)
        self.bBox_OK_Cancel.accepted.connect(Dialog_DeleteColumn.accept)
        self.bBox_OK_Cancel.rejected.connect(Dialog_DeleteColumn.reject)

        QMetaObject.connectSlotsByName(Dialog_DeleteColumn)
    # setupUi

    def retranslateUi(self, Dialog_DeleteColumn):
        Dialog_DeleteColumn.setWindowTitle(QCoreApplication.translate("Dialog_DeleteColumn", u"Dialog", None))
        self.label_DeleteColumns.setText(QCoreApplication.translate("Dialog_DeleteColumn", u"Delete Column(s)", None))
    # retranslateUi

