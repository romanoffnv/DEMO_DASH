import os
import sys

from __init__ import *

def db_connect(SRC_DIR, db_name):
        file = os.path.join(SRC_DIR, db_name)
        cnx = sqlite3.connect(file)
        cnx.row_factory = lambda cursor, row: row[0]
        cursor = cnx.cursor()
        return cursor, cnx 

def db_get(db_name, table_name):
    file = db_connect('cnx', db_name)
    cnx = sqlite3.connect(file)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", cnx)
    return df

def db_post(cursor, cnx, table_name, src, close):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    src.to_sql(name=f'{table_name}', con=cnx, if_exists='replace', index=False)
    cnx.commit()
    if close:
        cnx.close()

    
    


