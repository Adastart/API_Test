#coding=utf-8

from rq.test.test_user_reng import TestUserReng
from rq.lib.HTMLTestReportCN import *

# #使⽤TestLoader（⽤例加载器）⽣成测试集
# suite=unittest.TestLoader().loadTestsFromTestCase(TestUserReng)
# unittest.TextTestRunner(verbosity=2).run(suite)

#discover       用例发现    
# suite = unittest.defaultTestLoader.discover("./") # 遍历当前⽬录及⼦包中所有test_*.py中所有unittest⽤例
# unittest.TextTestRunner(verbosity=2).run(suite)



suite=unittest.TestSuite()
test_Case=suite.addTests([TestUserReng('test_user_reng_normal'),TestUserReng('test_user_reng_nologin')])

# with open("report.html",'wb') as f:
#     HTMLTestRunner(stream=f,verbosity=2,title='api_test',description='test_user_reng',tester='ada').run(suite)
#

unittest.TextTestRunner(verbosity=2).run(suite)