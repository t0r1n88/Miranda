import xlwings as xw
import os
import time
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


path_master = 'master.xlsx'





files = give_list_files(PATH_TO_FILES)
# Открываем основную книгу
master_workbook = xw.Book(path_master)
for file in files:
    name_sheet = file[:-5]
    if len(name_sheet) > 30:
        name_sheet = name_sheet[:30]

    # открываем книгу которую будем добавлять
    append_workbook = xw.Book(f'data/{file}')
    append_workbook.sheets(1).name = name_sheet




    # Получаем лист из добавляемого файла
    append_sheet = append_workbook.sheets(1)
    #
    append_sheet.api.Copy(After=master_workbook.sheets(1).api)
    time.sleep(15)
    append_workbook.app.quit()
master_workbook.save()
master_workbook.app.quit()

