from common.testdatatransferutils import TestDataTransferUtils
from common.requestsutils import RequestUtils

# testdatatransferutils是列表类型
all_cases_info_list = TestDataTransferUtils().get_testdata_by_list()
for case in all_cases_info_list:
    RequestUtils().test_steps(case['case_info'])



