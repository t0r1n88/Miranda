import pandas as pd
import os
from pathlib import Path
import xlsxwriter

# Константы
PATH_TO_FILES = 'data/'


def give_list_files(path):
    """
    Функция для получения списка файлов с заданными расширениями и без временных файлов
    :param path: Путь к файлам
    :return: Список с файлами
    """
    # Создаем список где будут хранится найденые пути до файлов
    files = []
    # Перебираем файлы в указанной директории
    for file in os.listdir():
        print(file)
        if not file.startswith('~$') and file.endswith('xlsx'):
            files.append(file)
    return files


if __name__ == '__main__':
    print('Lindy Booth')
    print(give_list_files(PATH_TO_FILES))
