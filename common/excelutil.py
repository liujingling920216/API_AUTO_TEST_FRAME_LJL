import os
import xlrd
from common.configutils import config_utils

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path,'..',config_utils.TEST_CASE_DATA_PATH)


class ExcelUtils:
    def __init__(self,sheet_name,excel_path=excel_path):
        self.excel_path = excel_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()   # 这种写法能获取整个表格对象

    def get_sheet(self):
        self.wb = xlrd.open_workbook(excel_path)
        self.ws = self.wb.sheet_by_name(self.sheet_name)

    def get_nrows(self):
         nrows = self.ws.nrows
         return nrows

    def get_ncols(self):
         ncols = self.ws.ncols
         return ncols

    def get_merged_cell(self):
        merged_cell = self.ws.merged_cells
        return merged_cell

    def __get_cell_value(self,row, col):
        cell_value = self.ws.cell_value(row, col)
        return cell_value


    def get_merged_cell_value(self,row_index, col_index):
        "对合并单元格进行处理，能获取普通单元格以及合并单元格的内容"
        for (rlow, rhigh, clow, chigh) in self.get_merged_cell():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.__get_cell_value(rlow, clow)
                    break
                else:
                    cell_value = self.__get_cell_value(row_index, col_index)
            else:
                cell_value = self.__get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_data_by_dic(self):
        all_data_list = []
        first_row_value = self.ws.row(0)
        for r in range(1,self.get_nrows()):
            row_dict = {}
            for c in range(0,self.get_ncols()):
                # ws.row 返回的格式形如[text:'测试用例编号', text:'测试用例名称']
                row_dict[first_row_value[c].value] = self.get_merged_cell_value(r,c)
            all_data_list.append(row_dict)
        return all_data_list



if __name__ == '__main__':
    excelutils = ExcelUtils('Sheet1')
    print(excelutils.get_merged_cell_value(3,0))
    # for i in excelutils.get_sheet_data_by_dic():
    #     print(i)

    print(excelutils.get_sheet_data_by_dic())
