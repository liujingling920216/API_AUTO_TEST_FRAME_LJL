import unittest
import warnings
import paramunittest
from common.testdatatransferutils import TestDataTransferUtils
from common.requestsutils import RequestUtils

all_cases_info_list = TestDataTransferUtils().get_testdata_by_list()

@paramunittest.parametrized(
    *all_cases_info_list
)

class TestCase(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def setParameters(self,case_name ,case_info):
        self.case_name = case_name
        self.case_info = case_info

    def test_case(self):
        actual_result = RequestUtils().test_steps(self.case_info)
        self.assertTrue(actual_result.get('check_result'), actual_result.get('message'))

if __name__ == '__main__':
    unittest.main()
