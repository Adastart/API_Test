#coding=utf-8
from rq.config.config_logs import *

def case_logging(case_name,url,data,expect_res,response_text):
    logging.info('用例标题：{}'.format(case_name))
    logging.info('url：{}'.format(url))
    logging.info('测试数据：{}'.format(data))
    logging.info('期望结果{}'.format(expect_res))
    logging.info('预期结果{}'.format(response_text))



