import logging

# # logging模块默认设置的日志级别是warning，而debug和info的级别是低于warning的，所以不会打印这两种日志信息
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug信息")
# logging.info("info信息")
# logging.warning("warning信息")
# logging.error("error信息")
# logging.critical("critical信息")

# 创建一个logger对象，并且设置默认的日志级别
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 创建日志格式对象
format = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

#创建FileHandler对象
fp = logging.FileHandler('test.log','a',encoding='utf-8')

# fp.setLevel(logging.DEBUG)
fp.setFormatter(format)
logger.addHandler(fp)


# 创建流对象
sp = logging.StreamHandler()
sp.setFormatter(format)
logger.addHandler(sp)
logger.setLevel(logging.DEBUG)

logger.info('文件记录日志')


