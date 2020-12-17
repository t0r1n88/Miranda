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

