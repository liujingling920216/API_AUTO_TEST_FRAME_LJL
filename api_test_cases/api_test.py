import unittest
import warnings
import paramunittest
from nb_log import LogManager
from common.testdatatransferutils import TestDataTransferUtils
from common.requestsutils import RequestUtils

all_cases_info_list = TestDataTransferUtils().get_testdata_by_list()
logger = LogManager().get_logger_and_add_handlers()

@paramunittest.parametrized(
    *all_cases_info_list
)

class TestCase(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        logger.info('测试初始化操作')

    def setParameters(self,case_name ,case_info):
        logger.info('加载测试数据')
        self.case_name = case_name
        self.case_info = case_info

    def test_case(self):
        logger.info('测试用例：%s 开始执行'%(self.case_info[0].get('测试用例编号')))
        self._testMethodDoc = self.case_info[0].get('测试用例名称')
        self._testMethodName =self.case_info[0].get('测试用例编号')
        actual_result = RequestUtils().test_steps(self.case_info)
        self.assertTrue(actual_result.get('check_result'), actual_result.get('message'))

if __name__ == '__main__':
    unittest.main()
