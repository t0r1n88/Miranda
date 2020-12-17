import pytest
import os
#Константы
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


