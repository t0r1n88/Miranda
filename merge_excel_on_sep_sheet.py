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


def create_name_sheet(name_file):
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
        with open('wrong_name.txt', 'a', encoding='utf-8') as f:
            bar = name_file + '\n'
            f.write(bar)


def read_excel(name_file):
    """

    :param file: Имя файла
    :return:кортеж из названия листа и датафрейма с данными
    """
    name_sheet = create_name_sheet(name_file)
    # считываем файл excle в пандас датафрейм
    path = 'data/' + name_file
    df = pd.read_excel(path,skipfooter=1)
    return name_sheet, df




if __name__ == '__main__':
    dict_files = pd.read_excel('general.xlsx',sheet_name=None)

    files = give_list_files(PATH_TO_FILES)
    for file in files:
        name_sheet, data = read_excel(file)
        dict_files[name_sheet] = data
    with pd.ExcelWriter('general.xlsx',engine='xlsxwriter') as writer:
        for name_sheet,data_sheet in dict_files.items():
            data_sheet.to_excel(writer,sheet_name=name_sheet)


        # write_sheet(general_file, name_sheet, data)
