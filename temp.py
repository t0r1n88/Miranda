import os
import xlwings as xw

path = 'data'
files = []
# Перебираем файлы в указанной директории
for file in os.listdir(path):
    if not file.startswith('~$') and file.endswith('.xlsx'):
        files.append(file)

counter = 0
path_master = 'master.xlsx'
while counter < len(files):
    master_workbook = xw.Book(path_master)
    try:
        for i in range(10):
            name_sheet = files[counter][:-5]
            if len(name_sheet) > 30:
                name_sheet = name_sheet[:30]

            append_workbook = xw.Book(f'data/{files[counter]}')
            append_workbook.sheets(1).name = name_sheet

            # Получаем лист из добавляемого файла
            append_sheet = append_workbook.sheets(1)
            #
            append_sheet.api.Copy(After=master_workbook.sheets(1).api)
            counter += 1
            print(counter)
    except IndexError:
        # да я знаю что выглядит не очень
        master_workbook.save()
        master_workbook.app.quit()
        break

    master_workbook.save()
    master_workbook.app.quit()

