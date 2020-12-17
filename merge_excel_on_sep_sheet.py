import pandas as pd
import os
from pathlib import Path
import xlsxwriter

# Константы
PATH_TO_FILES = 'data'


def give_list_files(path,extension='xlsx'):
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

if __name__ == '__main__':
    files = give_list_files(PATH_TO_FILES)
