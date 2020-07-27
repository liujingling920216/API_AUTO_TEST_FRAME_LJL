import os
from common.excelutil import ExcelUtils


current_path = os.path.abspath(os.path.dirname(__file__))
excel_path = os.path.join(current_path,'..','data\\test_case.xls')  # E:\python\API_AUTO_TEST_FRAME_LJL\common\..\data\test_case.xls
# print(excel_path)

class TestDataTransferUtils:
    def __init__(self,excel_path=excel_path):
        self.excel_path = excel_path
        self.test_data_sheet = ExcelUtils("Sheet1")
        self.test_data = self.test_data_sheet.get_sheet_data_by_dic()

    def _get_testdata_by_dic(self):
        test_data_dic = {}
        for r in self.test_data:
            "r是excel表中某一行数据"
            test_data_dic.setdefault(r["测试用例编号"], []).append(r)
        return test_data_dic
    """
    得到如下字典格式：
    {
        'case01': [{'测试用例编号': 'case01','测试用例名称': '测试能否正确执行获取access_token接口','测试用例步骤': 'step_01'}],
        'case02': [{'测试用例编号': 'case02','测试用例名称': '测试能否正确新增用户标签','测试用例步骤': 'step_01'}, {'测试用例编号': 'case02','测试用例名称': '测试能否正确新增用户标签','测试用例步骤': 'step_02'}],
        'case03': [{'测试用例编号': 'case03','测试用例名称': '测试能否正确删除用户标签','测试用例步骤': 'step_01'}, {'测试用例编号': 'case03','测试用例名称': '测试能否正确删除用户标签','测试用例步骤': 'step_02'}]
    }
    """
    def get_testdata_by_list(self):
        all_case_list = []
        for k,v in self._get_testdata_by_dic().items():
            case_dict = {}
            case_dict["case_name"] = k
            case_dict["case_info"] = v
            all_case_list.append(case_dict)
        return all_case_list

    def get_row_index(self,case_id,case_step):
        for row_id in range(len(self.test_data)):
            if self.test_data[row_id]['测试用例编号'] == case_id and self.test_data[row_id]['测试用例步骤'] == case_step:
                break;
        return row_id+1

    def get_col_index(self):
        for col_id in range(len(self.test_data_sheet.sheet.row(0))):
            if self.test_data_sheet.sheet.row(0)[col_id].value=='测试结果':
                break
        return col_id

    def write_test_result_to_excel(self,case_id,case_step,result='通过'):
        row_id = self.get_row_index(case_id,case_step)
        col_id = self.get_col_index()
        self.test_data_sheet.update_excel_result(row_id,col_id,result)

    def clear_test_result_from_excel(self):
        row_count = self.test_data_sheet.get_nrows()
        col_id = self.get_col_index
        self.test_data_sheet.clear_excel_result(1, row_count, col_id)

if __name__ == '__main__':
    testdatatransferutils = TestDataTransferUtils()
    # for i in testdatatransferutils.get_testdata_by_list():
    #     print(i)
    # get_row = testdatatransferutils.get_row_index('case02','step_01')
    # print(get_row)
    # col_index = testdatatransferutils.get_col_index()
    # print(col_index)
    testdatatransferutils.write_test_result_to_excel('case02','step_01','pass')







