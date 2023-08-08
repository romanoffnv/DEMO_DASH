import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(parent_dir)
SRC_DIR = parent_dir + '\SRC'

from __init__ import *
from src_get import main as src_get
from db import db_connect as dbcon
from db import db_post as dbpost
from query import main as query

def main():
    # Принимаем переменные из VBA
    cur_date = sys.argv[1]
    bank = sys.argv[2]
    
    # Открываем источник Блок3_Данные.csv в панде
    src = src_get(SRC_DIR, fname = 'Блок3')
    
    # Коннектимся к SQLlite 
    db_name = 'data.db'
    table_name = 'debts'
    cursor, cnx = dbcon(SRC_DIR, db_name)
    
    # Выгружаем данные в БД
    src_post_db = dbpost(cursor, cnx, table_name, src, close = False)

    # Делаем sql запрос к базе данных с нужными параметрами
    sql_query = query(cursor, table_name, cur_date, bank)
    

    # Выгружаем данные из sql_query в открытый Dash_board.xlsb
    app = xw.apps.active
    wb = app.books.active
    ws = wb.sheets.active

    # Распределяем данные по нужным ячейкам
    ws.range('D6').value = sql_query
    ws.range('E3').value = cur_date
    ws.range('G3').value = bank
    
    
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
