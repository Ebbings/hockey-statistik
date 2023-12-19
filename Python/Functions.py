import sqlalchemy as db
import pandas as pd
import re
import Settings

from PySide6.QtWidgets import QDialog
from widget_ui.dialog_ConnectToDatabase_ui import Ui_Dialog

def ConnectToMySQLDBviaSQLAlchemy():
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    state = dialog.exec()
    if state == 1:
        driver = ui.cb_driver.currentText()
        username = ui.le_username.text()
        password = ui.le_password.text()
        host = ui.le_host.text()
        port = ui.le_port.text()
        dataBase = ui.le_database.text()
        connString = f"{driver}://{username}:{password}@{host}:{port}/{dataBase}"
        Settings.dbengine = db.create_engine(connString, isolation_level='AUTOCOMMIT')
        Settings.dbconn = Settings.dbengine.connect()
        return Settings.dbconn

    if state == 0:
        return None

def Instant_Connect_To_DB():
    connString = f"mysql+pymysql://my_db_admin:mysql@185.157.160.111:33306/hockey"
    Settings.dbengine = db.create_engine(connString, isolation_level='AUTOCOMMIT')
    Settings.dbconn = Settings.dbengine.connect()
    return Settings.dbconn

def convert_height_str_to_m(height_str):
    FEET_TO_M = 0.3048
    pattern = re.compile(r"""(\d+)' *(\d+)(?:"|'')?""")
    feet, inches = map(float, re.match(pattern, height_str).groups())
    return FEET_TO_M * (feet + inches/12)

def convert_height_str_to_cm(height_str):
    return convert_height_str_to_m(height_str) * 100.0

def get_db_tables(dataBase, connection):
    query = f"select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = '{dataBase}' and TABLE_TYPE = 'BASE TABLE'"
    df = pd.read_sql(db.text(query), connection)
    return df.squeeze()

def get_table_columns(dataBase, table, connection):
    query = f"select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = '{dataBase}' and TABLE_NAME = '{table}' order by ORDINAL_POSITION"
    df = pd.read_sql(db.text(query), connection)
    return df.squeeze()

def get_table_key_columns(dataBase, table, connection):
    query = f"select column_name from information_schema.KEY_COLUMN_USAGE where constraint_name = 'PRIMARY' and table_schema = '{dataBase}' and table_name = '{table}' order by ORDINAL_POSITION;"
    df = pd.read_sql(db.text(query), connection)
    return df.squeeze()

def match_to_sql_column(schema, table, column, value, connection):
    query = f"select 1 from information_schema.columns where table_schema = '{schema}' and table_name = '{table}' and column_name = '{column}' and data_type in ('text', 'char', 'nchar', 'varchar', 'nvarchar', 'date', 'datetime', 'time');"
    df = pd.read_sql(db.text(query), connection)
    if df.empty:
        return value
    else:
        return "'"+value.replace("'", "\\'")+"'"

def get_list_all_pandas_compute_functions():
    agg_list = ['count', 'first', 'last', 'max', 'mean', 'median',
                'min', 'ohlc', 'prod', 'size', 'sem', 'std', 'sum', 'var']
    agg_list.sort()
    return agg_list

def convert_to_list_of_lists(lst):
    return([[el] for el in lst])

def check_int(s):
    if len(s) == 0: return False
    if s[0] in ('-', '+'): # if these characters exists in s
        return s[1:].isdigit() #return from index 1
    return s.isdigit() #else return from index 0

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def check_float(s):
    if len(s) == 0: return False
    if s[0] in ('-', '+'): # if these characters exists in s
        return is_float(s[1:]) #return from index 1
    return is_float(s)

def check_date_time(datatype, dt):
    if len(dt) == 0: return False
    date = pd.read_sql_query(f"call is_string_valid_datatype('{datatype}', '{dt}');", Settings.dbconn)

    if date.empty:
        return False
    return True