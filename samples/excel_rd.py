from datetime import datetime
import xlrd


wb = xlrd.open_workbook('example.xlsx')
ws = wb.sheet_by_name('Sheet1')
value = ws.cell_value(0,1)
data_value = datetime(xlrd.xldate_as_tuple(value, 0))
value = data_value.strftime('%Y/%d/%m %H:%M:%S')
print(type(value))
print(value)