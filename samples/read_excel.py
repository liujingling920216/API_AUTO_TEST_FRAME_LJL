# encoding: utf-8
import os
import xlrd

current_path = os.path.dirname(__file__)
# print(current_path)
excel_path = os.path.join(current_path,'data/test_data.xlsx')
# print(excel_path)

wb = xlrd.open_workbook(excel_path)
ws = wb.sheet_by_name('Sheet1')
mergecells = ws.merged_cells    # 返回一个列表  起始行，结束行，起始列，结束列
print(mergecells)


def get_merged_cell_value(row_index,col_index):
    "对合并单元格进行处理，能获取普通单元格以及合并单元格的内容"
    for (rlow,rhigh,clow,chigh) in mergecells:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = ws.cell_value(rlow,clow)
                break
            else:
                cell_value = ws.cell_value(row_index,col_index)
        else:
            cell_value = ws.cell_value(row_index, col_index)
    return cell_value

print(get_merged_cell_value(5,0))


