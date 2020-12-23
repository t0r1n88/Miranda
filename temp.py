import xlwings as xw
import os
import openpyxl







path1 = '1.xlsx'
path2 = 'master.xlsx'


path3 = '3.xlsx'


wb1 = xw.Book(path1)
wb2 = xw.Book(path2)

ws1 = wb1.sheets(1)
ws1.api.Copy(Before=wb2.sheets(1).api)

wb3 = xw.Book(path3)
ws3 = wb3.sheets(1)
ws3.api.Copy(Before=wb2.sheets(1).api)
wb2.save()
wb2.app.quit()
