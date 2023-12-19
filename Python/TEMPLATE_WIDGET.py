import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from AppStyle import Style

from widget_ui.TEMPLATE_WIDGET_UI_ui import Ui_TEMPLATE

import Settings
import Functions


class TEMPLATE_WIDGET_NAME(QWidget, Ui_TEMPLATE):
    def __init__(self, parent=None):
        super(TEMPLATE_WIDGET_NAME, self).__init__(parent)
        self.setupUi(self)

        self.pb_ChangeButton.clicked.connect(self.changeLabelText)

    def changeLabelText(self):
        self.text_change = self.le_ChangeText.text()
        self.tl_ChangeLabel.setText(self.text_change)


if __name__ == '__main__':
    Settings.init()
    Functions.Instant_Connect_To_DB()
    app = QApplication(sys.argv)
    app.setStyleSheet(Style)
    a = TEMPLATE_WIDGET_NAME()
    a.show()
    sys.exit(app.exec())
