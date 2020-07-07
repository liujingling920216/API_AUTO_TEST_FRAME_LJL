import os
from common.excelutil import ExcelUtils


current_path = os.path.abspath(os.path.dirname(__file__))
excel_path = os.path.join(current_path,'..','data\\test_case.xlsx')
print(excel_path)

class TestDataTransferUtils:
    def __init__(self,excel_path=excel_path):
        self.excel_path = excel_path
        self.test_data = ExcelUtils("Sheet1").get_sheet_data_by_dic()


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

if __name__ == '__main__':
    testdatatransferutils = TestDataTransferUtils()
    for i in testdatatransferutils.get_testdata_by_list():
        print(i)





