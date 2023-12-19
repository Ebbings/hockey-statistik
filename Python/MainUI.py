import sys
# Import necessary PySide6 modules
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication
from PySide6.QtCore import Qt

# Import style settings, data handling libraries, and other custom modules
from AppStyle import Style
import Functions
import Settings
# Import UI elements
from widget_ui.main_form_ui import Ui_MainWindow
# Import classes 
from team_statistics import Team_Statistics
from player_statistics import Player_Statistics
from event_statistics import Event_Statistics
from add_data import Add_data

#Custom class for printing messages in the main application
class ConsoleWriter:
    def __init__(self, text_edit):
        self.text_edit = text_edit

    def write(self, text):
        self.text_edit.insertPlainText(text)

    def flush(self):
        pass


class MainUI(QMainWindow, Ui_MainWindow):
    #Setup main window
    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()

        self.setWindowTitle("Hockey Statistics")
        self.setCursor(Qt.ArrowCursor)

        #Connect each module to a button
        self.pb_TeamStat.clicked.connect(self.lw1)
        self.pb_PlayerStat.clicked.connect(self.lw2)
        self.pb_EventStat.clicked.connect(self.lw3)
        self.pb_AddData.clicked.connect(self.lw4)
        
        self.pb_ConnectToDb.clicked.connect(self.connect_DB)

        ###########################################################################
        # Change the print to be added to the qtextbox
        sys.stdout = ConsoleWriter(self.textEdit)

        ###########################################################################
        # Make it so that text can only be added via prints and can be typed in
        self.textEdit.setReadOnly(True)

        ###########################################################################
        # Add application splash text at statup.
        self.placeholder_widget = QLabel("Please connect to a DB to use the application.")
        self.sw_Content.addWidget(self.placeholder_widget)

    # Load widget content by calling for the imported classes
    def LoadWidgets(self):
        print("Loading content...")
        # Add Widget to QStackedWidget Here
        self.sw_Content.addWidget(Team_Statistics())
        self.sw_Content.addWidget(Player_Statistics())
        self.sw_Content.addWidget(Event_Statistics())
        self.sw_Content.addWidget(Add_data())
        print("Loading complete")
        
    # Changes active widget
    def lw1(self):
        if Settings.dbconn:
            self.sw_Content.setCurrentIndex(1)
        else:
            print('Connect to DB first.')

    def lw2(self):
        if Settings.dbconn:
            self.sw_Content.setCurrentIndex(2)
        else:
            print('Connect to DB first.')

    def lw3(self):
        if Settings.dbconn:
            self.sw_Content.setCurrentIndex(3)
        else:
            print('Connect to DB first.')

    def lw4(self):
        if Settings.dbconn:
            self.sw_Content.setCurrentIndex(4)
        else:
            print('Connect to DB first.')

    # Connects to database via dialog window found in functions file
    def connect_DB(self):
        print('Connecting to DB.')
        Functions.ConnectToMySQLDBviaSQLAlchemy()
        if Settings.dbconn:
            self.LoadWidgets()
        else:
            print('No connection found.')
        

if __name__ == '__main__':
    Settings.init()
    app = QApplication(sys.argv)
    # app.setStyleSheet(Style)
    a = MainUI()
    a.show()
    sys.exit(app.exec())
