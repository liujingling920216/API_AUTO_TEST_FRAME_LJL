import os
import unittest
from nb_log import LogManager
from common import HTMLTestReportCN
from common.configutils import config_utils
from common.emailutils import EmailUtils

current_path = os.path.dirname(__file__)
report_path = os.path.join(current_path,'..',config_utils.REPORT_PATH)
test_case_path = os.path.join(current_path,'..',config_utils.TEST_CASE_PATH)
logger = LogManager(__file__).get_logger_and_add_handlers()

class RunCase:
    def __init__(self):
        self.test_case_path = test_case_path
        self.report_path = report_path
        self.title = '刘惊玲接口自动化测试报告'
        self.description = '接口自动化框架'
        self.tester = 'sophia.liu'

    def load_test(self):
        discover = unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                       pattern='api_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite =unittest.TestSuite()
        all_suite.addTests(discover)
        logger.info('加载所有的测试模块及方法到测试套件')
        return all_suite

    def run(self):
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_file_path, 'wb')
        logger.info('初始化创建测试报告路径：%s' % report_file_path)
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester=self.tester)
        runner.run(self.load_test())
        fp.close()
        return report_file_path

if __name__ == '__main__':
    report_path = RunCase().run()
    mail_body = '<h3 align="center">自动化测试报告</h3>'
    attach_path = report_path
    EmailUtils(mail_body, attach_path).send_mail()
