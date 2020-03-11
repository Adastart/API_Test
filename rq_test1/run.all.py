#coding=utf-8

from datetime import datetime
import unittest
import sys
sys.path.append('../..')

from rq_test1.lib.HTMLTestReportCN import *
from rq_test1.config.config_logs import *

logging.info("==================================测试开始====================================")

suite=unittest.defaultTestLoader.discover(test_path)
#with open(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/report/Test_Report.html" ,'wb') as f:
dt = datetime.now().strftime('%m-%d %H:%M:%S')
file_prefix = '/Users/aoxing/PycharmProjects/untitled3/rq_test1/report/Report '
file_suffix = ".html"
#with open(file_prefix + dt + file_suffix, 'wb') as f:
with open(report_file, 'wb') as f:

    HTMLTestRunner(stream=f,title='API_Test',description='测试描述',tester='敖星星').run(suite)

logging.info("==================================测试结束====================================")

#
# with open(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/report/Test_Report.html" ,'wb') as f:
#      open(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " Report.html", 'wb')  # ⼆进制写格式打开要⽣成的报告⽂件
#
#
#      open(r"/Users/aoxing/PycharmProjects/untitled3/rq_test1/report/(datetime.now().strftime('%Y-%m-%d %H:%M:%S') +  Report.html", 'wb')  # ⼆进制写格式打开要⽣成的报告⽂件
