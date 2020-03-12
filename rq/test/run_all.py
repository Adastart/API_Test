#coding=utf-8
import sys
sys.path.append('../..')
import unittest
from datetime import datetime
from lib.send_email import *
from lib.HTMLTestReportCN import *
from config.config_logs import *
from lib.case_log import *


logging.info("=============================测试开始==========================================")
#suite = unittest.defaultTestLoader.discover("./") #
suite = unittest.defaultTestLoader.discover(test_path) #

#with open(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" Report.html", 'wb') as  f:# ⼆进制写格式打开要⽣成的报告⽂件

with open(report_file,'wb') as f:
    HTMLTestRunner(stream=f,title="api test",description="测试描述",tester="星星").run(suite)

send_email(report_file)
logging.info("==============================测试结束=========================================")
