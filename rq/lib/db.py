#coding=utf-8
import pymysql
import sys
sys.path.append('..')
from config.config_logs import *



class DB:

    def __init__(self):
        self.connt=pymysql.connect(host=db_host,
                                   port=db_port,
                                   user=db_user,
                                   passwd=db_passwd,
                                   db=db_name,#库名
                                   charset='utf8'
                                   )
        self.cur=self.connt.cursor()

    def __del__(self):
        self.cur.close()
        self.connt.close()

    def find(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()



    def update(self,sql):
        try:
            self.cur.execute(sql)
            self.connt.commit()
        except Exception as e:
            self.connt.rollback()
            print(str(e))

    def check(self,userid):
        self.find("SELECT * FROM cap_capital_account WHERE user_id='{}'".format(userid))
        return self.cur.fetchall()


