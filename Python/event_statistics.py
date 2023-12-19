import sys
# Import necessary PySide6 modules
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QApplication, QDialog, QCheckBox, QSpacerItem, QSizePolicy
from AppStyle import Style

# Import style settings, data handling libraries, and other custom modules
import pandas as pd

# Import UI elements
from widget_ui.widget_event_search_ui import Ui_Form
from widget_ui.dialog_DeleteColumn_ui import Ui_Dialog_DeleteColumn

# Import custom settings and functions
import Settings
import Functions


class Event_Statistics(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Event_Statistics, self).__init__(parent)
        self.setupUi(self)

        self.df_Teams = pd.read_sql_table("team", Settings.dbconn)
        
        #Creates a empty list to enable hiding of columns later
        self.hidden_columns = [] 

        self.load_Teams_to_cb()

        #Listen for changes in scroll lists
        self.cb_TeamName.currentTextChanged.connect(self.load_seasons_to_cb)
        self.cb_Season.currentTextChanged.connect(self.load_table)
        self.tb_HideColumns.clicked.connect(self.hide_columns)

    #Get TeamId from TeamName
    def getTeamId(self, TeamName):
        return self.df_Teams.loc[self.df_Teams['TeamName'] == TeamName, 'TeamId'].values[0]
    
    #Insert teams into scroll list teams
    def load_Teams_to_cb(self):
        self.df_ScrollTeam = self.df_Teams["TeamName"].sort_values()
        self.cb_TeamName.addItems(self.df_ScrollTeam)

    # Load available seasons for corresponding team
    def load_seasons_to_cb(self):
        if self.cb_TeamName.currentIndex() == 0:
            return
        
        TeamId = self.getTeamId(self.cb_TeamName.currentText())
        
        # Sort out relevant seasons for selected team
        self.df_Played_Seasons = pd.read_sql_query(f"SELECT Season FROM event_shot join game on event_shot.GameId=game.GameId where AwayTeamId={TeamId} or HomeTeamId={TeamId} group by Season order by season", Settings.dbconn)

        self.df_ScrollSeason = self.df_Played_Seasons["Season"].sort_values()
        
        # Turn off listening for changes while clearing scroll list for season
        self.cb_Season.blockSignals(True)
        self.cb_Season.clear()
        self.cb_Season.blockSignals(False)

        # Make preselected option empty string
        self.cb_Season.addItem('')

        # Add relevant season to scroll list
        self.cb_Season.addItems(self.df_ScrollSeason)

    
    def load_table(self):
        if self.cb_TeamName.currentIndex() == 0:
            return
        
        # If Season='' then all seasons are selected
        if self.cb_Season.currentText() == '':
            Season = ''
        else:
            Season = self.cb_Season.currentText()
        
        TeamId = self.getTeamId(self.cb_TeamName.currentText())

        # Call procedure in database to fetch all relevant data for selected team and season
        EventStatistics = pd.read_sql_query(f"call Get_events_by_team_season({TeamId}, '{Season}');", Settings.dbconn)

        # Define width and height of table
        self.tw_Team_Season.setColumnCount(EventStatistics.shape[1])
        self.tw_Team_Season.setRowCount(EventStatistics.shape[0])

        # Set column titles same as in procedure
        header_labels = []
        for column in list(EventStatistics.columns.values):
            header_labels.append(column)
        self.tw_Team_Season.setHorizontalHeaderLabels(header_labels)

        # Fill table with data fetched from procedure 
        for row in range(EventStatistics.shape[0]):
            for col in range(EventStatistics.shape[1]):
                value = str(EventStatistics.iloc[row, col])
                
                # Formats cell value as either number or string 
                if value.isdigit():
                    value = int(value)
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, value)
                self.tw_Team_Season.setItem(row, col, item)

        # Resize all columns to fit the widest content in the cells in one go
        self.tw_Team_Season.resizeColumnsToContents()

    # Enable hiding of columns
    def hide_columns(self):
        if self.tw_Team_Season.columnCount() == 0:
            return
        
        # Call seperate class dialog that handeles column visibility
        dialog_hide = Dialog_DeleteColumn(self)
        state = dialog_hide.exec()
        if state:
            # Iterate only on checkboxes found in dialog window
            # Order of checkboxes matches order of columns in table
            for i, widget in enumerate(dialog_hide.vl_ComboBoxes.parentWidget().findChildren(QCheckBox)):
                if widget.isChecked():
                    self.tw_Team_Season.setColumnHidden(i, True)
                else:
                    self.tw_Team_Season.setColumnHidden(i, False)
                    

#Enable function to hide columns, uses the same dialog-base as delete columns
class Dialog_DeleteColumn(QDialog, Ui_Dialog_DeleteColumn):
    def __init__(self, parent: QWidget) -> None:
        super(Dialog_DeleteColumn, self).__init__(parent)
        self.setupUi(self)
        self.label_DeleteColumns.setText(QCoreApplication.translate("Dialog_DeleteColumn", u"Hide Column(s)", None))
        
        # Create checkbox for each column found in table
        for i in range(parent.tw_Team_Season.columnCount()):
            headder = parent.tw_Team_Season.horizontalHeaderItem(i)
            cb = QCheckBox(self.sa_WidgetContent)
            cb.setObjectName(f"cb_{i+1}")
            cb.setText(QCoreApplication.translate("Dialog_DeleteColumn", f"{headder.text()}", None))

            if parent.tw_Team_Season.isColumnHidden(i):
                cb.setChecked(True)
            
            self.vl_ComboBoxes.addWidget(cb)
        
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vl_ComboBoxes.addItem(spacer)

        

if __name__ == '__main__':
    Settings.init()
    Functions.Instant_Connect_To_DB()
    app = QApplication(sys.argv)
    #app.setStyleSheet(Style)
    a = Event_Statistics()
    a.show()
    sys.exit(app.exec())
