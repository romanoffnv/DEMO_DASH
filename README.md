# DEMO_DASH
Dashboard demo для RegionConsult
Программа на базе GUI Dash_board.xlsb, VBA скрипт запускает _main.py
Требуемые библиотеки:
  from pprint import pprint
  import time
  import re
  import pandas as pd
  import sqlite3
  from openpyxl import load_workbook
  import xlwings as xw

Архитектура:
Папка SRC - в ней хранятся источники
Dash_board.xlsb - файл GUI отправляет параметры, определенные пользователем через скрипт VBA
__init__.py - в этом файле все импорты
_main.py - главный контроллер программы
  src_get.py - модуль открывает источник Блок3_Данные.csv, запускается из _main.py, возвращает df в _main.py
  db.py - модуль взаимодействия с БД sqlite
  query.py - модуль формирования запроса к БД
