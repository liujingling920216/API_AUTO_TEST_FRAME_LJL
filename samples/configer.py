import os
import configparser

config_path = os.path.join(os.path.dirname(__file__),'..','conf\config.ini')
print(config_path)
conf = configparser.ConfigParser()
conf.read(config_path,encoding='utf-8')
print(conf.get('path','TEST_CASE_DATA_PATH'))