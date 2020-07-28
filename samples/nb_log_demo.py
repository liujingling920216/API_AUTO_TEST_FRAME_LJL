from nb_log import LogManager


logger_aa = LogManager('aa').get_logger_and_add_handlers()
logger_aa.info("hah")


logger_bb = LogManager('bb').get_logger_and_add_handlers()
logger_bb.debug("debug信息")

