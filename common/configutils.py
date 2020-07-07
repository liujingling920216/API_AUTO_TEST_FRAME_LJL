import os
import configparser


config_path = os.path.join(os.path.dirname(__file__),'..','conf\config.ini')

class ConfigUtils:
    def __init__(self,config_path=config_path):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    @property
    def TEST_CASE_DATA_PATH(self):
        test_case_data_path = self.conf.get('path','TEST_CASE_DATA_PATH')
        return test_case_data_path

config_utils = ConfigUtils()

if __name__ == '__main__':
    print(config_utils.TEST_CASE_DATA_PATH)