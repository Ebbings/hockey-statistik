# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_AddColumn.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QLabel,
    QLayout, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog_AddColumn(object):
    def setupUi(self, Dialog_AddColumn):
        if not Dialog_AddColumn.objectName():
            Dialog_AddColumn.setObjectName(u"Dialog_AddColumn")
        Dialog_AddColumn.resize(390, 197)
        self.verticalLayout = QVBoxLayout(Dialog_AddColumn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_AddColumn = QFormLayout()
        self.formLayout_AddColumn.setObjectName(u"formLayout_AddColumn")
        self.formLayout_AddColumn.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.formLayout_AddColumn.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_AddColumn.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_AddColumn.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_AddColumn.setHorizontalSpacing(30)
        self.formLayout_AddColumn.setVerticalSpacing(10)
        self.formLayout_AddColumn.setContentsMargins(20, -1, -1, -1)
        self.label_AddColumnName = QLabel(Dialog_AddColumn)
        self.label_AddColumnName.setObjectName(u"label_AddColumnName")

        self.formLayout_AddColumn.setWidget(0, QFormLayout.LabelRole, self.label_AddColumnName)

        self.le_AddColumnName = QLineEdit(Dialog_AddColumn)
        self.le_AddColumnName.setObjectName(u"le_AddColumnName")

        self.formLayout_AddColumn.setWidget(0, QFormLayout.FieldRole, self.le_AddColumnName)

        self.label_AddColumnDatatype = QLabel(Dialog_AddColumn)
        self.label_AddColumnDatatype.setObjectName(u"label_AddColumnDatatype")

        self.formLayout_AddColumn.setWidget(1, QFormLayout.LabelRole, self.label_AddColumnDatatype)

        self.cb_AddColumnDatatype = QComboBox(Dialog_AddColumn)
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.addItem("")
        self.cb_AddColumnDatatype.setObjectName(u"cb_AddColumnDatatype")

        self.formLayout_AddColumn.setWidget(1, QFormLayout.FieldRole, self.cb_AddColumnDatatype)

        self.label_AddColumnDefaultValue = QLabel(Dialog_AddColumn)
        self.label_AddColumnDefaultValue.setObjectName(u"label_AddColumnDefaultValue")

        self.formLayout_AddColumn.setWidget(2, QFormLayout.LabelRole, self.label_AddColumnDefaultValue)

        self.le_AddColumnDefaultValue = QLineEdit(Dialog_AddColumn)
        self.le_AddColumnDefaultValue.setObjectName(u"le_AddColumnDefaultValue")

        self.formLayout_AddColumn.setWidget(2, QFormLayout.FieldRole, self.le_AddColumnDefaultValue)

        self.label_AddColumnAllowNull = QLabel(Dialog_AddColumn)
        self.label_AddColumnAllowNull.setObjectName(u"label_AddColumnAllowNull")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_AddColumnAllowNull.sizePolicy().hasHeightForWidth())
        self.label_AddColumnAllowNull.setSizePolicy(sizePolicy)

        self.formLayout_AddColumn.setWidget(3, QFormLayout.LabelRole, self.label_AddColumnAllowNull)

        self.checkb_AddColumnAllowNull = QCheckBox(Dialog_AddColumn)
        self.checkb_AddColumnAllowNull.setObjectName(u"checkb_AddColumnAllowNull")
        self.checkb_AddColumnAllowNull.setChecked(True)
        self.checkb_AddColumnAllowNull.setTristate(False)

        self.formLayout_AddColumn.setWidget(3, QFormLayout.FieldRole, self.checkb_AddColumnAllowNull)


        self.verticalLayout.addLayout(self.formLayout_AddColumn)

        self.buttonBox_AddColumn = QDialogButtonBox(Dialog_AddColumn)
        self.buttonBox_AddColumn.setObjectName(u"buttonBox_AddColumn")
        self.buttonBox_AddColumn.setOrientation(Qt.Horizontal)
        self.buttonBox_AddColumn.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox_AddColumn)


        self.retranslateUi(Dialog_AddColumn)
        self.buttonBox_AddColumn.accepted.connect(Dialog_AddColumn.accept)
        self.buttonBox_AddColumn.rejected.connect(Dialog_AddColumn.reject)

        QMetaObject.connectSlotsByName(Dialog_AddColumn)
    # setupUi

    def retranslateUi(self, Dialog_AddColumn):
        Dialog_AddColumn.setWindowTitle(QCoreApplication.translate("Dialog_AddColumn", u"Dialog", None))
        self.label_AddColumnName.setText(QCoreApplication.translate("Dialog_AddColumn", u"Column name", None))
        self.label_AddColumnDatatype.setText(QCoreApplication.translate("Dialog_AddColumn", u"Column datatype", None))
        self.cb_AddColumnDatatype.setItemText(0, QCoreApplication.translate("Dialog_AddColumn", u"Select datatype", None))
        self.cb_AddColumnDatatype.setItemText(1, QCoreApplication.translate("Dialog_AddColumn", u"TINYTEXT", None))
        self.cb_AddColumnDatatype.setItemText(2, QCoreApplication.translate("Dialog_AddColumn", u"TEXT", None))
        self.cb_AddColumnDatatype.setItemText(3, QCoreApplication.translate("Dialog_AddColumn", u"TINYINT", None))
        self.cb_AddColumnDatatype.setItemText(4, QCoreApplication.translate("Dialog_AddColumn", u"SMALLINT", None))
        self.cb_AddColumnDatatype.setItemText(5, QCoreApplication.translate("Dialog_AddColumn", u"INT", None))
        self.cb_AddColumnDatatype.setItemText(6, QCoreApplication.translate("Dialog_AddColumn", u"DOUBLE", None))
        self.cb_AddColumnDatatype.setItemText(7, QCoreApplication.translate("Dialog_AddColumn", u"DATE", None))
        self.cb_AddColumnDatatype.setItemText(8, QCoreApplication.translate("Dialog_AddColumn", u"TIME", None))
        self.cb_AddColumnDatatype.setItemText(9, QCoreApplication.translate("Dialog_AddColumn", u"DATETIME", None))

        self.label_AddColumnDefaultValue.setText(QCoreApplication.translate("Dialog_AddColumn", u"Column default", None))
        self.le_AddColumnDefaultValue.setText("")
        self.label_AddColumnAllowNull.setText(QCoreApplication.translate("Dialog_AddColumn", u"Allow NULL", None))
        self.checkb_AddColumnAllowNull.setText(QCoreApplication.translate("Dialog_AddColumn", u"Yes / No", None))
    # retranslateUi

