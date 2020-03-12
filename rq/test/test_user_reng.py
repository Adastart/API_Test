#coding=utf-8
import sys
sys.path.append('../..')
import requests
import unittest
import json
from lib.read_excel import *
from lib.case_log import *

from config.config_logs import *
class TestUserReng(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       # cls.data_list=excel_to_find(r"/Users/aoxing/PycharmProjects/untitled3/rq/data/test_user_data_1.xlsx","Test_User_Reng")
        cls.data_list=excel_to_find(os.path.join(data_path,"test_user_data_1.xlsx"),"Test_User_Reng")
    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_reng_normal(self):
        case_data=get_excel_to(self.data_list,'test_user_reng_normal')
        if not case_data:
            ('测试用例不存在')
            return
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=int(case_data.get('expect_res'))

        res=requests.post(url=url,data=json.loads(data))
        response=res.json()
        case_logging(case_data,url,data,expect_res,response)
        self.assertEqual(expect_res,response['result'])

    def test_user_reng_nologin(self):
        case_data=get_excel_to(self.data_list,'test_user_reng_nologin')
        if not case_data:
            ('测试用例不存在')
            return
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=int(case_data.get('expect_res'))

        res=requests.post(url=url,data=json.loads(data))
        response = res.json()
        case_logging(case_data,url,data,expect_res,response)
        self.assertEqual(expect_res, response['result'])

    def test_user_reng_onemoney(self):
        case_data=get_excel_to(self.data_list,'test_user_reng_onemoney')
        if not case_data:
            ('测试用例不存在')
            return
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=int(case_data.get('expect_res'))

        res=requests.post(url=url,data=json.loads(data))
        response = res.json()
        case_logging(case_data,url,data,expect_res,response)
        self.assertEqual(expect_res, response['result'])

    def test_user_reng_wrong(self):
        case_data=get_excel_to(self.data_list,'test_user_reng_wrong')
        if not case_data:
            ('测试用例不存在')
            return
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=int(case_data.get('expect_res'))

        res=requests.post(url=url,data=json.loads(data))
        response = res.json()
        case_logging(case_data,url,data,expect_res,response)
        self.assertEqual(expect_res, response['result'])

if __name__=='__main__':
    unittest.main(verbosity=2)
