# DEMO_DASH<br>
Dashboard demo для RegionConsult<br>
Программа на базе GUI Dash_board.xlsb, VBA скрипт запускает _main.py<br>
Требуемые библиотеки:<br>
  from pprint import pprint<br>
  import time<br>
  import re<br>
  import pandas as pd<br>
  import sqlite3<br>
  from openpyxl import load_workbook<br>
  import xlwings as xw<br>

Архитектура:<br>
Папка SRC - в ней хранятся источники<br>
Dash_board.xlsb - файл GUI отправляет параметры, определенные пользователем через скрипт VBA<br>
__init__.py - в этом файле все импорты<br>
_main.py - главный контроллер программы<br>
  src_get.py - модуль открывает источник Блок3_Данные.csv, запускается из _main.py, возвращает df в _main.py<br>
  db.py - модуль взаимодействия с БД sqlite<br>
  query.py - модуль формирования запроса к БД<br>
