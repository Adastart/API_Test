#coding=utf-8

import unittest
import requests
import json
from rq.lib.read_excel import *
import sys
sys.path.append("../..")
from rq.config.config_logs import *


class TestUserlend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.data_list=excel_to_find("test_user_data_1.xlsx","Test_User_Lend")
        cls.data_list=excel_to_find(os.path.join(data_path,"test_user_data_1.xlsx"),"Test_User_Lend")
    @classmethod
    def tearDownClass(cls):
        pass

    def test_user_lend_nomal(self):
        case_data=get_excel_to(self.data_list,'test_user_lend_normal')
        if not case_data:
            print('用例数据不存在')
        url=case_data.get('url')
        data=case_data.get('data')
        expect_res=case_data.get('expect_res')

        res=requests.post(url=url,data=json.loads(data))

   #     self.assertEqual(expect_res,res.text)
   #     self.assertIn(res.text,expect_res)
        print(res.text)

    def test_user_lend_nologin(self):
        case_data=get_excel_to(self.data_list,'test_user_lend_nologin')
        if not case_data:
            print('用例数据不存在')
        url=case_data.get('url')
        data=case_data.get('data')
        expect=case_data.get('expect')

        res=requests.post(url=url,data=json.loads(data))

      #  self.assertIn(expect,res.text)
        print(res.text)

if __name__=='__main__':
    unittest.main(verbosity=2)




