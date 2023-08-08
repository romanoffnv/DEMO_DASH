import os
import sys


from __init__ import *


def main(cursor, table_name, cur_date, bank):
    # Запрос в sql базу
    date_col = 'Дата'
    overdue = 'Просрочка, дней'
    bank_col = 'Первоначальный кредитор'
    over_from = [-1, 0, 30, 60, 90]
    over_to = [0, 30, 60, 90, 2147483647]
    
    
    
    def query_db(over_from, over_to, date, bank):
        query = f"SELECT COUNT(*) FROM {table_name} WHERE \"{overdue}\" > {over_from} AND \"{overdue}\" <= {over_to}  AND \"{bank_col}\" = '{bank}' AND \"{date_col}\" = \"{date}\""
        cursor.execute(query)
        return cursor.fetchall()
    
    L_overdues_collect = []
    for f, t in zip(over_from, over_to):
        L_overdues_collect.append(query_db(f, t, cur_date, bank))
    
    L_overdues = [item for sublist in L_overdues_collect for item in sublist]
    

    return L_overdues
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
