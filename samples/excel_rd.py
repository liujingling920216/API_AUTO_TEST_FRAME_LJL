import xlrd

wb = xlrd.open_workbook('example.xlsx')
ws = wb.sheet_by_name('Sheet1')
value = ws.cell_value(0,1)
print(type(value))
print(value)