import pandas as pd
import os
from pathlib import Path
import xlsxwriter
import xlrd

# Константы
PATH_TO_FILES = 'data'


def give_list_files(path, extension='xlsx'):
    """
    Функция для получения списка файлов с заданными расширениями и без временных файлов
    :param path: Путь к файлам
    :return: Список с файлами
    """
    # Создаем список где будут хранится найденые пути до файлов
    files = []
    # Перебираем файлы в указанной директории
    for file in os.listdir(path):
        if not file.startswith('~$') and file.endswith(extension):
            files.append(file)
    return files


def name_sheet(name_file):
    """
    Функция для получения названия листа из имени файла. Так как для удобной ориентировки они должны совпадать
    :param name_file: имя файла вместе с расширением
    :return: строка с названием файла
    """
    if name_file.endswith('.xlsx'):
        # Получаем имя листа, с помощью среза
        name_sheet = name_file[:-5]
        if len(name_sheet) < 30:
            return name_sheet
        else:
            return name_sheet[:30]
    else:
        with open('wrong_name.txt','a',encoding='utf-8') as f:
            bar = name_file + '\n'
            f.write(bar)



def read_excel(name_file):
    """

    :param file: Имя файла
    :return:
    """
    name_sheet(name_file)

    # df = pd.read_excel(f'data//{file}',skiprows=0)
    # print(df.columns[1])


if __name__ == '__main__':
    files = give_list_files(PATH_TO_FILES)
    for file in files:
        read_excel(file)
