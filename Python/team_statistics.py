import sys
# Import necessary PySide6 modules
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QApplication, QTreeWidgetItem, QTreeWidgetItemIterator
from PySide6.QtCharts import QChart, QChartView, QHorizontalBarSeries, QValueAxis, QBarCategoryAxis, QBarSet, QAbstractBarSeries
# Import style settings, data handling libraries, and other custom modules
from AppStyle import Style
import pandas as pd
import sqlalchemy as db

# Import UI elements
from widget_ui.widget_team_search_ui import Ui_Form_TeamStatistics
# Import custom settings and functions
import Settings
import Functions

# Create a class inheriting from QWidget and Ui_Form_TeamStatistics
class Team_Statistics(QWidget, Ui_Form_TeamStatistics):
    def __init__(self, parent=None):
        super(Team_Statistics, self).__init__(parent)
        self.setupUi(self)
        # Connect itemClicked signal to Load_Graph_Team_Comparison method
        self.tw_Teams.itemClicked.connect(self.Load_Graph_Team_Comparison)
        # Populate the tree widget
        self.populate_tree()

    def populate_tree(self):
        # Fetch team data from the database and populate the sidebar tree widget
        df_teams = pd.read_sql_table("team", Settings.dbconn)
        for i in df_teams.index:
            # Create tree branches for each team and set necessary data
            branch = QTreeWidgetItem(self.tw_Teams)
            branch.setFlags(branch.flags() | Qt.ItemIsUserCheckable)
            branch.setText(0, df_teams['TeamName'][i])
            branch.setData(0, Qt.UserRole, df_teams['TeamId'][i])  # Save TeamId for corresponding teamName
            branch.setCheckState(0, Qt.Unchecked)

    def Load_Graph_Team_Comparison(self, item, column):
        # Initiate empty list for each data category
        team_names = []
        team_games = []
        team_goals_for = []
        team_goals_against = []
        team_avg_gpg = []
        team_penalty = []
        
        # Fetch team data for each category
        for branch in QTreeWidgetItemIterator(self.tw_Teams, QTreeWidgetItemIterator.NoChildren | QTreeWidgetItemIterator.Checked):
            team = branch.value()
            team_names.append(team.text(column))
            team_games.append(self.getNumberOfGames(team.data(column, Qt.UserRole)))
            team_goals_for.append(self.getNumberOfGoalsFor(team.data(column, Qt.UserRole)))
            team_goals_against.append(self.getNumberOfGoalsAgainst(team.data(column, Qt.UserRole)))
            team_avg_gpg.append(self.getAverageGoals(team.data(column, Qt.UserRole)))
            team_penalty.append(self.getPenaltyHours(team.data(column, Qt.UserRole)))
       
        # Create a HorizontalBarSeries named series
        serie = QHorizontalBarSeries()
        
        # Create a QBarSet and for each team append data into each category list
        for i, team_name in enumerate(team_names):
            set = QBarSet(team_name)
            set.append([
                team_games[i],
                team_goals_for[i],
                team_goals_against[i],
                team_avg_gpg[i],
                team_penalty[i]
            ])
            serie.append(set)

        chart = QChart()
        
        # Configure labels
        serie.setLabelsVisible(True)
        serie.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

        # Change label color
        label_color = "black"  # Red color
        for bar_set in serie.barSets():
            bar_set.setLabelColor(label_color)
        
        # Add series of data to the chart
        chart.addSeries(serie)

        # Configure axis titles
        chart.setTitle("Comparison graph")
        axis_y = QBarCategoryAxis()
        axis_y.append([
            "Games played", 
            "Goals for", 
            "Goals against", 
            "Average goals per 100 games", 
            "Penalty hours"
        ])
        # Add x and y axis
        chart.addAxis(axis_y, Qt.AlignLeft)
        serie.attachAxis(axis_y)
        
        axis_x = QValueAxis()
        chart.addAxis(axis_x, Qt.AlignBottom)
        serie.attachAxis(axis_x)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QChartView(chart)
        
        # Empty layout to ensure no residues from earlies searches remains
        self.deleteItemsOfLayout(self.chart_area_layout)
        # Insert new layout
        self.chart_area_layout.insertWidget(0, chart_view, 100)

        chart.setAnimationOptions(chart.SeriesAnimations)
        chart.setTheme(chart.ChartThemeLight)
        chart_view.setChart(chart)

    # The mechanism for counting number of games
    def getNumberOfGames(self, teamId):
        df_Event_Games = pd.read_sql_query(db.text(f"select count(*) from hockey.event_game_end where AwayteamId = {teamId} or HomeTeamId = {teamId};"), Settings.dbconn)
        return df_Event_Games.iloc[0][0]
    
    # The mechanism for counting number of goals made for the team
    def getNumberOfGoalsFor(self, teamId):
        df_Event_Goalsfor = pd.read_sql_query(db.text(f"select count(*) from hockey.event_goal where ScoringTeamId = {teamId};"), Settings.dbconn)
        return df_Event_Goalsfor.iloc[0][0]
    
    # The mechanism for counting number of goals made against the team
    def getNumberOfGoalsAgainst(self, teamId):
        df_Event_Goalsagainst = pd.read_sql_query(db.text(f"select count(*) from event_goal where (AwayTeamId = {teamId} or HomeTeamId = {teamId}) and ScoringTeamId <> {teamId};"), Settings.dbconn)
        return df_Event_Goalsagainst.iloc[0][0]
    
    # The mechanism for counting how many goals were made per 100 game
    def getAverageGoals(self, teamId):
        df_Event_average_goals = pd.read_sql_query(db.text(f"select avg(r.goals)*100 from (select count(*) as goals from event_goal where ScoringTeamId = {teamId} group by GameId) as r;"), Settings.dbconn)
        return df_Event_average_goals.iloc[0][0]
    
    # The mechanism for counting how many penalty hours a team had
    def getPenaltyHours(self, teamId):
        df_Event_penalty = pd.read_sql_query(db.text(f"select sum(PenaltyDuration)/60 from hockey.event_penalty where TeamPenaltyId= {teamId};"), Settings.dbconn)
        return df_Event_penalty.iloc[0][0]
    
    # The mechanism for emptying the layout
    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())


if __name__ == '__main__':
    Settings.init()
    Functions.Instant_Connect_To_DB()
    app = QApplication(sys.argv)
    app.setStyleSheet(Style)
    a = Team_Statistics()
    a.show()
    sys.exit(app.exec())
