import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'data\\test_case.xlsx')

wb = xlrd.open_workbook(excel_path)
ws = wb.sheet_by_name('Sheet1')
mergecells = ws.merged_cells


