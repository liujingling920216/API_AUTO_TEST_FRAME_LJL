import pytest
from common.testdatatransferutils import TestDataTransferUtils
from common.requestsutils import RequestUtils
from nb_log import LogManager


logger = LogManager().get_logger_and_add_handlers()
all_cases_info_list = TestDataTransferUtils().get_testdata_by_list()
params_key = (',').join(all_cases_info_list[0].keys())
print(params_key)     #'case_name,case_info'
params_value = []

for case in all_cases_info_list:
    value = tuple(case.values())
    params_value.append(value)
print(params_value)   #[('case01',[step1,step2]),('case02',[step1,step2]).....]

class TestCase():
    @pytest.mark.parametrize(params_key,params_value)
    def test_case(case_id,case_info):
        logger.info('测试用例：%s开始执行'%(case_info.get('测试用例编号')))
        actual_result = RequestUtils().test_steps(case_info)
        assert actual_result.get('check_result'), actual_result.get('message')

if __name__ == '__main__':
    pytest.main(['-s','-v'])