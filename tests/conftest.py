import pytest
import os

# Константы
PATH_TO_FIlES = 'data_test'


@pytest.fixture()
def list_files():
    """
    Фикстура для получения списка файлов с нужным расширением

    :return:Возвращает список содержащий пути до файлов
    """
    files = []
    for file in os.listdir(PATH_TO_FIlES):
        if not file.startswith('~$') and file.endswith('xlsx'):
            files.append(file)
    return files


@pytest.fixture()
def names_files():
    """
    Фикстура для генерации списка имен файлов, чтобы проверить как функция name_sheet извлекает имена для листов из имен
    файлов
    :return: список проверяемых имен файлов
    """
    lst_names_files = ['Заявка 43 на 06.11.2020.xlsx', 'заявки 2.xlsx', '1.xlsx',
                       'Заявка о ведении учета на складе лакокрасочных изделий 6312125       ',
                       'Заявка 553 на 06.11.2020 лакокрасочных изделий номер 152.xlsx']
    return lst_names_files


@pytest.fixture()
def correct_name_files():
    """
    Фикстура для создания списка с корректными именами которые должны получиться после работы функции name_sheet
    :return: Список с файлами
    """
    lst = ['Заявка 43 на 06.11.2020', 'заявки 2', '1',None, 'Заявка 553 на 06.11.2020 лакок']
    return lst
