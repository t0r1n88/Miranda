from merge_excel_on_sep_sheet import *
import pytest
import os
path = 'c:/Users/1/PycharmProjects/Miranda/data/'
def test_give_list_files(extension='xlsx'):
    """
    GIVEN(Дано) Папка с файлами
    WHEN(Когда) Используем функцию give_list
    THEN(Тогда) Должны получить список файлов с указанными расширениями,временные файлы не должны попасть в этот список
    :param list_files:список файлов предварительно созданный
    :return:
    """

    assert type(give_list_files(path)) == list
    for file in give_list_files(path):
        assert file.endswith(extension)

def test_name_sheet(names_files,correct_name_files):
    """
    GIVEN(Дано) Список с именами файлов
    WHEN(Когда) Используем функцию name_sheet
    THEN(Тогда) Должны получить корректные именя для листов книги, корректно обработать имена файлов без расширений
    :param names_files: список с именами файлов
    """
    lst_test = []
    for name_file in names_files:
        # print(name_file)
        n = name_sheet(name_file)
        lst_test.append(n)


    assert lst_test == correct_name_files




