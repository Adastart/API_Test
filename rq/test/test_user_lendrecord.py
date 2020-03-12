#coding=utf-8
import sys
sys.path.append("../..")
import unittest
import requests

from config.config_logs import *
from lib.case_log import *
from lib.read_excel import *


class Test_User_Lendrecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.file_list=excel_to_find(r"/Users/aoxing/PycharmProjects/untitled3/rq/data/test_user_data_1.xlsx","Test_User_LendRecord")
        cls.file_list=excel_to_find(os.path.join(data_path,"test_user_data_1.xlsx"),"Test_User_LendRecord")

    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_lendrecord_normal(self):
        case_data=get_excel_to(self.file_list,'test_user_lendrecord_normal')
        if not case_data:
            logging.info ('用例不存在')

        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=str(int(case_data.get('expect_res')))
        print(expect_res)
        res=requests.post(url=url,data=data)
        response=res.json()
        self.assertEqual(expect_res,response['result'])
        case_logging(case_data,url,data,expect_res,response)

    def test_user_lendrecord_nologin(self):
        case_data=get_excel_to(self.file_list,'test_user_lendrecord_nologin')
        if not case_data:
            logging.info('用例不存在')
            return
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=str(int(case_data.get('expect_res')))
        res=requests.post(url=url,data=data)
        response=res.json()
        self.assertEqual(expect_res,response['result'])
        case_logging(case_data,url,data,expect_res,response)

    def test_user_lendrecord_noexistent(self):
        case_data=get_excel_to(self.file_list,'test_user_lendrecord_noexistent')
        if not case_data:
            logging.info('用例不存在')
            return
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=str(int(case_data.get('expect_res')))
        res=requests.post(url=url,data=data)
        response=res.json()
        self.assertEqual(expect_res,response['result'])
        case_logging(case_data,url,data,expect_res,response)

if __name__ =='__main__':
    unittest.main(verbosity=2)










