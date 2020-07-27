import os
import xlrd
from xlutils.copy import copy

excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xls')

wb = xlrd.open_workbook(excel_path,formatting_info=True)  #加上formatting_info拷贝附件的时候将格式一并拷贝
new_wb = copy(wb)
ws = new_wb.get_sheet(wb.sheet_names().index('Sheet1'))
ws.write(1,3,60)
new_wb.save(excel_path)






