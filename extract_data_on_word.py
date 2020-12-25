import docx
import os


def get_list_files(extension='docx',folder=os.getcwd()):
    """
    Функция для получения списка файлов с определнным расширением.

    :param extension:Расширение файла по умолчанию docx
    :param folder: Папка где нужно искать файлы, по умолчанию папка где запущен скрипт
    :return: Список файлов с нужным расширением
    """
    # Список где будут хранится пути к файлам
    paths = []
    for root,dirs,files in os.walk(folder):
        for file in files:
            if file.endswith(extension) and not file.startswith('~'):
                paths.append(os.path.join(root,file))

    return paths
if __name__ =='__main__':
    files = get_list_files(folder='data')
    print(files)