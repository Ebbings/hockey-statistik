import sys
# Import necessary PySide6 modules
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QPushButton, QWidget, QTableWidgetItem, QApplication, QDialog, QDialogButtonBox, QCheckBox, QSpacerItem, QSizePolicy, QMessageBox

# Import style settings, data handling libraries, and other custom modules
from AppStyle import Style
import pandas as pd
import sqlalchemy as db

# Import UI elements
from widget_ui.add_data_ui import Ui_Form
from widget_ui.dialog_AddColumn_ui import Ui_Dialog_AddColumn
from widget_ui.dialog_DeleteColumn_ui import Ui_Dialog_DeleteColumn

# Import custom settings and functions
import Settings
import Functions
import math

class Add_data(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Add_data, self).__init__(parent)
        self.setupUi(self)
        
        self.deleteButton = QPushButton("delete_this_row")
        self.add_sql_tables_to_cb()

        # Construct connections for signal events to listen to.
        self.cb_SqlTables.currentTextChanged.connect(self.load_table)
        self.tw_DataToInsert.cellChanged.connect(self.update_data_in_sql_table)
        self.pb_AddRow.clicked.connect(self.add_empty_row)
        self.pb_SaveRow.clicked.connect(self.insert_data_into_Mysql)
        self.sb_CurrentPage.valueChanged.connect(self.value_changed)
        self.pb_PreviousPage.clicked.connect(self.previous_page)
        self.pb_NextPage.clicked.connect(self.next_page)
        self.pb_AddNewColumn.clicked.connect(self.add_column_dialog)
        self.pb_DeleteColumn.clicked.connect(self.delete_column_dialog)

    # Used by paging to switch to the previus page.
    def previous_page(self):
        self.sb_CurrentPage.setValue(self.sb_CurrentPage.value() - 1)

    # Used by paging to switch to the next page.
    def next_page(self):
        self.sb_CurrentPage.setValue(self.sb_CurrentPage.value() + 1)

    def value_changed(self):
        self.block_signals(True)
        self.add_datarows_to_table()
        self.block_signals(False)
    
    # Name of all sql-tables added to scroll list
    def add_sql_tables_to_cb(self):
        self.cb_SqlTables.addItems(Functions.get_db_tables('hockey', Settings.dbconn))

    # Internal function that decides whether the program listens to the signal events or not.
    def block_signals(self, block:bool):
        self.tw_DataToInsert.blockSignals(block)
        self.sb_CurrentPage.blockSignals(block)
    
    # Load selected sql-table from database to QTableWidget in program.
    def load_table(self):
        if self.cb_SqlTables.currentIndex() == 0:
            return
        
        # Stop listening to signal events to prevent infinite loop.
        self.block_signals(True)
        
        self.sb_CurrentPage.setValue(1)
        self.sql_table = self.cb_SqlTables.currentText()
        self.sql_columns = Functions.get_table_columns('hockey', self.sql_table, Settings.dbconn)
        self.put_columns_into_table()
        self.add_datarows_to_table()
        
        self.block_signals(False)

    # Sets the column headder labels as is returned from the sql table. 
    def put_columns_into_table(self):
        self.tw_DataToInsert.clear()
        
        # Number of columns from sql table plus one for delete row button.
        self.tw_DataToInsert.setColumnCount(len(self.sql_columns)+1)

        header_labels = []
        for column in self.sql_columns:
            header_labels.append(column)
        header_labels.append("Delete")
        self.tw_DataToInsert.setHorizontalHeaderLabels(header_labels)

    # Fill the QTableWidget with data from SQL table.
    def add_datarows_to_table(self):
        if self.cb_SqlTables.currentIndex() == 0:
            return
        
        # Fetch total number of rows in table to use in paging calculation.
        sql_stmt = f'select count(*) from {self.cb_SqlTables.currentText()}'
        with Settings.dbengine.begin() as conn:
            exe = conn.execute(db.text(sql_stmt))
            max_rows = exe.scalar()
        
        max_pages = math.ceil(max_rows/self.sb_RowsPerPage.value())
        
        # Limit the paging field to not go over max number of pages.
        self.sb_CurrentPage.setMaximum(max_pages)
        self.label_MaxNumberOfPages.setText(f'/ {max_pages}')

        current_page = self.sb_CurrentPage.value()

        # Fetch data from sql table offsetted by the limit (paging) function.
        sql_stmt = f'select * from {self.cb_SqlTables.currentText()} limit {(current_page - 1) * self.sb_RowsPerPage.value()}, {self.sb_RowsPerPage.value()}'
        
        Statistics = pd.read_sql_query(sql_stmt, Settings.dbconn)
        
        del_col_index = len(self.sql_columns)
        
        # Set the page row number and start filling the QTableWidget with data from SQL Select.
        self.tw_DataToInsert.setRowCount(Statistics.shape[0])
        for row in range(Statistics.shape[0]):
            for col in range(Statistics.shape[1]):
                value = str(Statistics.iloc[row, col])
                if value.isdigit():
                    value = int(value)
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, value)
                self.tw_DataToInsert.setItem(row, col, item)
            
        # Add the delete row button to the last cell for every row.
        for row in range(self.tw_DataToInsert.rowCount()):
            deleteButton = QPushButton("Delete Row")
            deleteButton.clicked.connect(self.delete_row)
            self.tw_DataToInsert.setCellWidget(row, del_col_index, deleteButton)

        # Resize all columns to fit the widest content in the cells in one go.
        self.tw_DataToInsert.resizeColumnsToContents()

    # Add a new empty row to be filled with data.
    def add_empty_row(self):
        if self.tw_DataToInsert.rowCount() == 0:
            return
        
        # Stop listening to event signals while new row is being edited.
        self.block_signals(True)
        self.tw_DataToInsert.setRowCount(self.tw_DataToInsert.rowCount()+1)

    # Reads what the user have entered on the new edited row.
    def read_data_from_QtableWidget(self):
        if self.tw_DataToInsert.rowCount() == 0:
            return
        
        widgetItemList = []
        
        # Read from all cells one by one
        for i in range(len(self.sql_columns)):
            widgetItem = self.tw_DataToInsert.item(self.tw_DataToInsert.rowCount()-1, i)
            # Construct a list of all entered values.
            if (widgetItem and widgetItem.text()):
                widgetItemList.append(widgetItem.text())

        # Convert each value in the list to be a seperate list consiting of only that value. Ex: ['1', 'a', 'b2'] -> [['1'], ['a'], ['b2']]
        widgetItemList = Functions.convert_to_list_of_lists(widgetItemList)
        
        # Create a dictionary for mapping each value to the corresponding column.
        widgetItemDict = {self.sql_columns[i]: widgetItemList[i] for i in range(len(self.sql_columns))} 
        
        # Return the dictionary as a Pandas DataFrame for easier handeling.
        return pd.DataFrame().from_dict(widgetItemDict)
    
    # Writes the new row from the QTableWidget tothe SQL Table.
    def insert_data_into_Mysql(self):
        if self.tw_DataToInsert.rowCount() == 0 or not self.tw_DataToInsert.signalsBlocked():
            return
        
        # Fetch the new row as a Pandas DataFrame.
        col_value = self.read_data_from_QtableWidget()
        if col_value.empty:
            return
        
        # Write the entire Pandas DataFrame to the SQL Table.
        col_value.to_sql(self.cb_SqlTables.currentText(), 
                         con = Settings.dbconn, 
                         schema = 'hockey',
                         if_exists = 'append',
                         index = False)
        
        # Refresh the content in QTableWidget to reflect the new changes in SQL Table.
        self.add_datarows_to_table()
        # Start listening again for the signal-events.
        self.block_signals(False)
        
    # Is called whenever a cell is changed in the QTableWidget and writes the changes to the SQL Table.
    def update_data_in_sql_table(self, row_index, column_index):
        schema = 'hockey'
        # Fetch the current loaded SQL Table name.
        table = self.cb_SqlTables.currentText()
        # Fetch the column name the change is taking place in.
        column = self.sql_columns[column_index]
        # Fetch the value that has been changed.
        cell = self.tw_DataToInsert.item(row_index, column_index)
        
        # Start constructing a SQL Update statement.
        update_smt = f'update {table} '
        # Use function to determine if the value should be encapsulated with ''.
        update_smt += f'set {column} = {Functions.match_to_sql_column(schema, table, column, cell.text(), Settings.dbconn)} '
        update_smt += 'where '
                        
        # Use all other columns and thier values in the WHERE clause for the UPDATE statement.
        for i, col_name in enumerate(self.sql_columns):
            if i == column_index:
                continue
            row_cell = self.tw_DataToInsert.item(row_index, i)
            sql_and = ''
            # All rows after the first must begin with AND.
            if i > 0:
                sql_and = 'and '
            # Convert Python None syntax to corresponding SQL NULL syntax for all empty columns.
            if row_cell.text() == 'None': 
                update_smt += f'{sql_and}{col_name} is NULL '
            # Convert the rest of all the values in QTableWidget to matching SQL syntax.
            else:
                update_smt += f'{sql_and}{col_name} = {Functions.match_to_sql_column(schema, table, col_name, row_cell.text(), Settings.dbconn)} '
        
        # Execute the update statement in SQL database.
        with Settings.dbengine.begin() as conn:
            conn.execute(db.text(update_smt))

        # Stop listening to signal events while QTableWidget gets reloaded with new changes.
        self.block_signals(True)
        self.add_datarows_to_table()
        # Start listening to signal events again.
        self.block_signals(False)

    # Deletes a row in QTableWidget and also SQL Table.
    def delete_row(self):
        # Figure out which button have been pressed and on which row it is located.
        button = self.sender()
        index = self.tw_DataToInsert.indexAt(button.pos())
        if index.isValid():
            # Start fetching information to be used in SQL Delete statement.
            row_index = index.row()
            schema = 'hockey'
            table = self.cb_SqlTables.currentText()
            delete_smt = f'delete from {table} where '
            # Use all values in all column for the row to be deleted in where cluse in delete statement.
            for i, col_name in enumerate(self.sql_columns):
                row_cell = self.tw_DataToInsert.item(row_index, i)
                sql_and = ''
                # All rows after the first must begin with an AND.
                if i > 0:
                    sql_and = 'and '
                # Convert all values to matching SQL syntax.
                if row_cell.text() == 'None': 
                    # Convert Python None syntax to SQL NULL suntax.
                    delete_smt += f'{sql_and}{col_name} is NULL '
                else:
                    # Use function to determine if the value should be encapsulated with ''.
                    delete_smt += f'{sql_and}{col_name} = {Functions.match_to_sql_column(schema, table, col_name, row_cell.text(), Settings.dbconn)} '
            
        # Execute delete statement in SQL database.
        with Settings.dbengine.begin() as conn:
            conn.execute(db.text(delete_smt))

        # Stop listening to signal events while QTableWidget gets reloaded with new changes.
        self.block_signals(True)
        self.add_datarows_to_table()
        # Start listening to signal events again.
        self.block_signals(False)

    # Constructs the dialog that handeles adding new columns to the SQL Table.
    def add_column_dialog(self):
        if self.cb_SqlTables.currentIndex() == 0: 
            return
        
        # Call custom PySide6 dialog class for handeling new column configuration.
        dialog_AddCol = Dialog_AddNewColumn(self, self.cb_SqlTables.currentText())
        state = dialog_AddCol.exec()
        if state:
            # Fetch all information on how the new column should be configured.
            column_name = dialog_AddCol.le_AddColumnName.text()
            data_type = dialog_AddCol.cb_AddColumnDatatype.currentText()
            default = dialog_AddCol.le_AddColumnDefaultValue.text()
            isnull = dialog_AddCol.checkb_AddColumnAllowNull.isChecked()
            # Create new column in SQL Table.
            self.addColumn(column_name, data_type, default, isnull)
        
    # Constructs new column in SQL Table.
    def addColumn(self, column_name, data_type, default, isnull):
        # Encapsulate default value in '' if relevant.
        if len(default) > 0:
            if data_type in ["TINYTEXT", "TEXT", "DATE", "TIME", "DATETIME"]:
                default = "'"+default+"'"
            default = "DEFAULT "+default

        default = default.replace(',', '.')
        
        # Determine if new column is nullable or not.
        if isnull: allow_null = "NULL"
        else: allow_null = "NOT NULL"

        # Construct the ALTER TABLE statement with new column parameters.
        alter_stmt = f"ALTER TABLE {self.cb_SqlTables.currentText()} ADD COLUMN {column_name} {data_type} {default} {allow_null}"

        # Execute and create the new column in SQL Table.
        with Settings.dbengine.begin() as conn:
             conn.execute(db.text(alter_stmt))

        # Reload QTableWidget with new column and possible default value.
        self.load_table()


    # Removes a column from SQL Table and QTableWidget.
    def delete_column_dialog(self):
        if self.cb_SqlTables.currentIndex() == 0: 
            return
        
        # Call custom PySide6 dialog class for column deletion.
        dialog_delete_col = Dialog_DeleteColumn(self, self.cb_SqlTables.currentText())
        state = dialog_delete_col.exec()
        if state:
            checked_cols = []
            
            # Filter and itterate thrugh all checked boxes for each column present in table.
            for widget in dialog_delete_col.vl_ComboBoxes.parentWidget().findChildren(QCheckBox):
                # All checked columns are saved for further processing.
                if widget.isChecked():
                    checked_cols.append(widget.text())
                
            if not checked_cols == []:
                # Make sure user is certain the columns should be deleted. All data in those columns will be irreverible deleted!
                msgBox = QMessageBox()
                msgBox.setText(f"Are you sure you want to delete the columns: {checked_cols}")
                msgBox.setInformativeText("Deleted columns are gone forever and all data along with it.")
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.setDefaultButton(QMessageBox.No)
                msgBox.setIcon(QMessageBox.Warning)
                ret = msgBox.exec()
                
                if ret == QMessageBox.No:
                    # User have changed their mind.
                    return
                
                for column in checked_cols:
                    # Construct the Alter Table statement to drop the selected columsn from SQL Table.
                    alter_stmt = f"ALTER TABLE {self.cb_SqlTables.currentText()} DROP COLUMN {column}"
                    with Settings.dbengine.begin() as conn:
                        conn.execute(db.text(alter_stmt))

        # Reload QTableWidget with a new slimmer look.
        self.load_table()
    

# Custom UI elements class for dialog box to add columns to SQL Table.
class Dialog_AddNewColumn(QDialog, Ui_Dialog_AddColumn):
    # Define in parameters and parent widget.
    def __init__(self, parent: QWidget, table) -> None:
        super(Dialog_AddNewColumn, self).__init__(parent)
        self.setupUi(self)
        self.table_columns = Functions.get_table_columns('hockey', table, Settings.dbconn)

        # Dissable the OK button to prevent the user from making a invalid configuration.
        # The OK button should only be enabled when column configuration have passed validation.
        self.buttonBox_AddColumn.button(QDialogButtonBox.Ok).setEnabled(False)
                
        # Connect all Interactive elemts to validation function.
        self.le_AddColumnName.textEdited.connect(self.validate_new_column)
        self.cb_AddColumnDatatype.currentIndexChanged.connect(self.validate_new_column)
        self.le_AddColumnDefaultValue.textEdited.connect(self.validate_new_column)
        self.checkb_AddColumnAllowNull.stateChanged.connect(self.validate_new_column)

    # Logic to determine whereif the column configuration can be added to a SQL Tabe.
    def validate_new_column(self):
        # Dissable the OK button to prevent the user from making a invalid configuration
        self.buttonBox_AddColumn.button(QDialogButtonBox.Ok).setEnabled(False)
        
        # Fetch current user entered information.
        name = self.le_AddColumnName.text()
        datatype = self.cb_AddColumnDatatype.currentText()
        cb_index = self.cb_AddColumnDatatype.currentIndex()
        default = self.le_AddColumnDefaultValue.text()
        allow_null = self.checkb_AddColumnAllowNull.isChecked()
        
        whole_numbers = ['TINYINT', 'SMALLINT', 'INT']
        text_types = ['TINYTEXT', 'TEXT']
        float_number = ['DOUBLE']
        datetime = ['DATETIME', 'DATE', 'TIME']

        # All validation logic goes here. If a check fails teh call is returned back to the begining.
        # The call need to make it all the way to the bottom for the OK button to be enabled.
        if name in self.table_columns[0]:
            print('Column name already exists in table')
            return

        if cb_index == 0:
            return
        
        if allow_null == False and default == '':
            print('Non nullable columns need a provided default value.')
            return
        
        if datatype in whole_numbers and len(default) > 0:
            if not Functions.check_int(default):
                print('Default value must be a valid number.')
                return
            
        if datatype in text_types and len(default) > 0:
            print(f"{datatype} can't have a default value.")
            return
            
        default = default.replace(',', '.')
        if default.count('.') > 1:
            print('Only one (.) allowed')
            return
        
        if datatype in float_number and len(default) > 0:
            if not Functions.check_float(default):
                print('Default value must be a valid float number.')
                return
        
        if datatype in datetime and len(default) > 0:
           if not Functions.check_date_time(datatype, default):
               print('Invalid datetime type')
               return

        #ToDo: Add more validation if nessesary.
        
        # The user have enterd a valid configuration combination, and column can be created.
        self.buttonBox_AddColumn.button(QDialogButtonBox.Ok).setEnabled(True)


# Custom UI elements class for dialog box to delete columns from SQL Table.
class Dialog_DeleteColumn(QDialog, Ui_Dialog_DeleteColumn):
    # Define calling parent widget and inparameters.
    def __init__(self, parent: QWidget, table) -> None:
        super(Dialog_DeleteColumn, self).__init__(parent)
        self.setupUi(self)
        
        # Fetch current SQL Table columns and possible KEY columns.
        table_columns = Functions.get_table_columns('hockey', table, Settings.dbconn)
        table_key_columns = Functions.get_table_key_columns('hockey', table, Settings.dbconn)
        
        # Filter out the KEY columns since they should not be removable.
        columns = [col for col in table_columns if col not in table_key_columns]
        columns.sort()

        # Construct a check box for each non-KEY column in the SQL Table.
        for i, colname in enumerate(columns):
            cb = QCheckBox(self.sa_WidgetContent)
            cb.setObjectName(f"cb_{i+1}")
            cb.setText(QCoreApplication.translate("Dialog_DeleteColumn", f"{colname}", None))
            self.vl_ComboBoxes.addWidget(cb)
        
        # Add a space for a tidier UI look.
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vl_ComboBoxes.addItem(spacer)



if __name__ == '__main__':
    Settings.init()
    Functions.Instant_Connect_To_DB()
    app = QApplication(sys.argv)
    # app.setStyleSheet(Style)
    a = Add_data()
    a.show()
    sys.exit(app.exec())
