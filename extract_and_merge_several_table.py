"""
Извлечение данных из нескольких таблиц с одинаковой структурой.Объединение этих данных в одну таблицу с добавлением
 признака Название таблицы откуда извлечены данные
"""
import pandas as pd
import xlrd
import os

path = 'data'
files = []
min_excel_file = 100

# Перебираем файлы в указанной директории
for file in os.listdir(path):
    if not file.startswith('~$') and file.endswith('.xlsx'):
        files.append('data/'+file)


# Объединяем файлы пользуясь list comprehension
df = pd.concat([pd.read_excel(file,skiprows=1) for file in files],ignore_index=True)

df.to_excel('Itog.xlsx',index=False)
