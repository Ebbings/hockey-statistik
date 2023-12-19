# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ConnectToDatabase.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(360, 290)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(360, 290))
        Dialog.setStyleSheet(u"QLabel {\n"
"	min-width: 80px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Header = QLabel(Dialog)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(80, 60))
        self.Header.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.Header.setFont(font)

        self.verticalLayout_2.addWidget(self.Header, 0, Qt.AlignHCenter)

        self.vLayout_Fields = QVBoxLayout()
        self.vLayout_Fields.setObjectName(u"vLayout_Fields")
        self.vLayout_Fields.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.hLayout_driver = QHBoxLayout()
        self.hLayout_driver.setObjectName(u"hLayout_driver")
        self.tl_driver = QLabel(Dialog)
        self.tl_driver.setObjectName(u"tl_driver")
        self.tl_driver.setMaximumSize(QSize(80, 16777215))

        self.hLayout_driver.addWidget(self.tl_driver)

        self.cb_driver = QComboBox(Dialog)
        self.cb_driver.addItem("")
        self.cb_driver.setObjectName(u"cb_driver")

        self.hLayout_driver.addWidget(self.cb_driver)


        self.vLayout_Fields.addLayout(self.hLayout_driver)

        self.hLayout_username = QHBoxLayout()
        self.hLayout_username.setObjectName(u"hLayout_username")
        self.tl_username = QLabel(Dialog)
        self.tl_username.setObjectName(u"tl_username")

        self.hLayout_username.addWidget(self.tl_username)

        self.le_username = QLineEdit(Dialog)
        self.le_username.setObjectName(u"le_username")

        self.hLayout_username.addWidget(self.le_username)


        self.vLayout_Fields.addLayout(self.hLayout_username)

        self.hLayout_password = QHBoxLayout()
        self.hLayout_password.setObjectName(u"hLayout_password")
        self.tl_password = QLabel(Dialog)
        self.tl_password.setObjectName(u"tl_password")

        self.hLayout_password.addWidget(self.tl_password)

        self.le_password = QLineEdit(Dialog)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.Password)

        self.hLayout_password.addWidget(self.le_password)


        self.vLayout_Fields.addLayout(self.hLayout_password)

        self.hLayout_host = QHBoxLayout()
        self.hLayout_host.setObjectName(u"hLayout_host")
        self.tl_host = QLabel(Dialog)
        self.tl_host.setObjectName(u"tl_host")
        self.tl_host.setMinimumSize(QSize(80, 0))

        self.hLayout_host.addWidget(self.tl_host)

        self.le_host = QLineEdit(Dialog)
        self.le_host.setObjectName(u"le_host")

        self.hLayout_host.addWidget(self.le_host)


        self.vLayout_Fields.addLayout(self.hLayout_host)

        self.hLayout_port = QHBoxLayout()
        self.hLayout_port.setObjectName(u"hLayout_port")
        self.tl_port = QLabel(Dialog)
        self.tl_port.setObjectName(u"tl_port")

        self.hLayout_port.addWidget(self.tl_port)

        self.le_port = QLineEdit(Dialog)
        self.le_port.setObjectName(u"le_port")

        self.hLayout_port.addWidget(self.le_port)


        self.vLayout_Fields.addLayout(self.hLayout_port)

        self.hLayout_database = QHBoxLayout()
        self.hLayout_database.setObjectName(u"hLayout_database")
        self.tl_database = QLabel(Dialog)
        self.tl_database.setObjectName(u"tl_database")

        self.hLayout_database.addWidget(self.tl_database)

        self.le_database = QLineEdit(Dialog)
        self.le_database.setObjectName(u"le_database")

        self.hLayout_database.addWidget(self.le_database)


        self.vLayout_Fields.addLayout(self.hLayout_database)


        self.verticalLayout_2.addLayout(self.vLayout_Fields)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Header.setText(QCoreApplication.translate("Dialog", u"Connect to Database", None))
        self.tl_driver.setText(QCoreApplication.translate("Dialog", u"Driver", None))
        self.cb_driver.setItemText(0, QCoreApplication.translate("Dialog", u"mysql+pymysql", None))

        self.tl_username.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.tl_password.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.tl_host.setText(QCoreApplication.translate("Dialog", u"Host adress", None))
        self.le_host.setText(QCoreApplication.translate("Dialog", u"185.157.160.111", None))
        self.tl_port.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.le_port.setText(QCoreApplication.translate("Dialog", u"33306", None))
        self.tl_database.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.le_database.setText(QCoreApplication.translate("Dialog", u"hockey", None))
    # retranslateUi

