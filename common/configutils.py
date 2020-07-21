import os
import configparser


config_path = os.path.join(os.path.dirname(__file__),'..','conf/config.ini')
# print(config_path)

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    @property
    def TEST_CASE_DATA_PATH(self):
        test_case_data_path = self.conf.get('path','TEST_CASE_DATA_PATH')
        return test_case_data_path

    @property
    def REPORT_PATH(self):
        report_path = self.conf.get('path','TEST_REPORT')
        return report_path

    @property
    def TEST_CASE_PATH(self):
        test_case_path = self.conf.get('path','TEST_CASE_PATH')
        return test_case_path


    @property
    def LOG_PATH(self):
        log_path = self.conf.get('path','LOG_PATH')
        return log_path

    @property
    def LOG_LEVER(self):
        log_lever = self.conf.get('log','LOG_LEVER')
        return log_lever

    @property
    def HOST(self):
        host = self.conf.get('default','HOST')
        return host

    @property
    def SMTP_SERVER(self):
        smtp_server_value = self.conf.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def SMTP_SENDER(self):
        smtp_sender_value = self.conf.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def SMTP_PASSWORD(self):
        smtp_password_value = self.conf.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.conf.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def SMTP_CC(self):
        smtp_cc_value = self.conf.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def SMTP_SUBJECT(self):
        smtp_subject_value = self.conf.get('email', 'smtp_subject')
        return smtp_subject_value

config_utils = ConfigUtils()

if __name__ == '__main__':
    print(config_utils.TEST_CASE_DATA_PATH)
    print(config_utils.LOG_PATH)
    print(config_utils.LOG_LEVER)