import os
import xlrd
from xlutils.copy import copy

excel_path = os.path.join(os.path.dirname(__file__),'data/test_data.xls') #修改excel操作，暂时不支持xlsx，修改之前需要将格式改成xls

wb = xlrd.open_workbook(excel_path,formatting_info=True)  #加上formatting_info拷贝附件的时候将格式一并拷贝
new_wb = copy(wb)  #创建一个副本对象
ws = new_wb.get_sheet(wb.sheet_names().index('Sheet1')) #副本对象没有sheet_by_name，或者sheet_by_index,通常用get_sheet方法
ws.write(1,3,60)    #write(row坐标，col坐标，修改的值)
new_wb.save(excel_path)






