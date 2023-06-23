"""
Подсчет количества дубликатов в списке детей посетивших профпробы
"""
import pandas as pd

df = pd.read_excel('data/data.xlsx')
out_df = df.groupby('ФИО ребенка').count()[['№ п/п']]
dupl_df = out_df[out_df['№ п/п'] > 1]
dupl_df.rename(columns={'№ п/п':'Количество участий в пробах'},inplace=True)
dupl_df.to_excel('Дубликаты.xlsx')
out_df.to_excel('Список.xlsx')


