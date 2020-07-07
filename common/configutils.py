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
    def LOG_PATH(self):
        log_path = self.conf.get('path','LOG_PATH')
        return log_path

    @property
    def LOG_LEVER(self):
        log_lever = self.conf.get('log','LOG_LEVER')
        return log_lever

config_utils = ConfigUtils()

if __name__ == '__main__':
    print(config_utils.TEST_CASE_DATA_PATH)
    print(config_utils.LOG_PATH)
    print(config_utils.LOG_LEVER)