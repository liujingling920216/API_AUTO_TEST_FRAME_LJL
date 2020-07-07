import os
import logging
import time
from common.configutils import config_utils


current_path = os.path.dirname(__file__)
log_output_path = os.path.join( current_path,'..', config_utils.LOG_PATH  )

class LogUtils:
    def __init__(self,log_path=log_output_path):
        # 创建一个logger对象，并且设置默认的日志级别(必须设置默认日志级别)
        log_level = int(config_utils.LOG_LEVER)
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)
        self.log_name = os.path.join(log_path, 'ApiTest_%s.log' % time.strftime('%Y_%m_%d'))

        # 创建日志格式对象
        format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        # 创建FileHandler对象
        fp = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fp.setLevel(log_level)
        fp.setFormatter(format)
        self.logger.addHandler(fp)

        # 创建流对象
        sp = logging.StreamHandler()
        sp.setFormatter(format)
        self.logger.addHandler(sp)
        self.logger.setLevel(log_level)

        sp.close()
        fp.close()

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    logger = LogUtils().get_log()
    logger.debug("debug测试写日志功能")