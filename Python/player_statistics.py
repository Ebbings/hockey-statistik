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
from widget_ui.widget_player_search_ui import Ui_Form_PlayerStatistics

import Settings
import Functions

# Create a class inheriting from QWidget and Ui_Form_PlayerStatistics
class Player_Statistics(QWidget, Ui_Form_PlayerStatistics):
    def __init__(self, parent=None):
        super(Player_Statistics, self).__init__(parent)
        self.setupUi(self)
        # Connect itemClicked signal to Load_Graph_Team_Comparison method
        self.tw_TeamsAndPlayers.itemClicked.connect(self.Load_Graph_Player_Comparison)
        # Populate the tree widget
        self.populate_tree()


    def populate_tree(self):
        # Fetch team data from the database and populate the sidebar tree widget
        query = db.text("""
            select row_number() over (partition by q.TeamId order by q.PlayerName) as 'RowNo'
                , count(q.TeamId) over (partition by q.TeamId order by q.TeamId) as 'MaxRowNo'
                , q.*
            from (
                select t.TeamId
                    , t.TeamName
                    , p.PlayerId
                    , p.PlayerName
                from player_statistics as p
                join team as t on t.TeamId = p.TeamId
                group by t.TeamId, t.TeamName, p.PlayerId, p.PlayerName
            ) as q
            order by q.TeamName, q.PlayerName;
            """)
        df = pd.read_sql_query(query, Settings.dbconn)
        for i in df.index:
            # Create tree branches for each team with team as parent and players in that team as children
            if df['RowNo'][i] == 1:
                # When RowNo = 1, thers a new team and we create a new parent 
                parent = QTreeWidgetItem(self.tw_TeamsAndPlayers)
                parent.setText(0, df['TeamName'][i])
                parent.setFlags(parent.flags() | Qt.ItemIsAutoTristate | Qt.ItemIsUserCheckable)
                parent.setData(0, Qt.UserRole, df['TeamId'][i])
            # Creates children for current parent
            child = QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, df['PlayerName'][i])
            child.setCheckState(0, Qt.Unchecked)
            child.setData(0, Qt.UserRole, df['PlayerId'][i])

    
    def Load_Graph_Player_Comparison(self, item, column):
        # Begin construction of select statement for data retrieval
        sql_stmt = """
            select p.PlayerName as 'Name'
                , t.TeamName as 'Team'
                , sum(p.NumberOfGames) as 'Games played'
                , sum(p.NumberOfGoals) as 'Goals'
                , (sum(p.NumberOfGoals) / sum(p.NumberOfGames))*100 as 'Average goals per 100 games'
                , sum(p.PenaltyMinutes) as 'Penalty minutes'
            from player_statistics as p
            join team as t on t.TeamId = p.TeamId
            """
        
        i = 0
        # Extract all checked players from QTreeWidget for construction of the where component
        for branch in QTreeWidgetItemIterator(self.tw_TeamsAndPlayers, QTreeWidgetItemIterator.NoChildren | QTreeWidgetItemIterator.Checked):
            i += 1
            child = branch.value()
            parent = child.parent()
            
            # Only the first row begins with where, all subsequent rows begin with or
            if i == 1:
                sql_stmt += "where "
            else:
                sql_stmt += "\t"+"or "
            # Use the PlayerId in combination with the corresponding TeamId
            sql_stmt += f"(t.TeamId = {parent.data(column, Qt.UserRole)} and p.PlayerId = {child.data(column, Qt.UserRole)})"+"\n"
        # Group by team and player to calculate correct amount in aggregate functions
        sql_stmt += "group by t.TeamId, t.TeamName, p.PlayerId, p.PlayerName;"
        
        # If i has not changed; exit function
        if i == 0:
            return
        # Execute constructed select statement to retrieve player statistics 
        df = pd.read_sql_query(db.text(sql_stmt), Settings.dbconn)
        
        serie = QHorizontalBarSeries()

        for i in df.index:
            # Create a set for a player and append the players values in each category
            set = QBarSet(df['Name'][i])
            set.append([
                df['Games played'][i],
                df['Goals'][i],
                df['Average goals per 100 games'][i],
                df['Penalty minutes'][i]
            ])
            serie.append(set)
        # Configure labels
        chart = QChart()
        serie.setLabelsVisible(True)
        serie.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)

        # Change label color
        label_color = "black"  # Red color
        for bar_set in serie.barSets():
            bar_set.setLabelColor(label_color)

        # Add series of data to the chart
        chart.addSeries(serie)
        chart.setTitle("Comparison graph")

        # Configure axis titles
        axis_y = QBarCategoryAxis()
        axis_y.append(["Games played", "Goals", "Average goals per 100 games", "Penalty minutes"])
        chart.addAxis(axis_y, Qt.AlignLeft)
        serie.attachAxis(axis_y)

        # Add x and y axis
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
    a = Player_Statistics()
    a.show()
    sys.exit(app.exec())
