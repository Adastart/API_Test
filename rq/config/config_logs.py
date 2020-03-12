#coding=utf-8
import logging
from datetime import datetime
import os

nowtime= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 项⽬路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前⽂件的上⼀级的上⼀级⽬录（增加⼀级）
data_path = os.path.join(prj_path, 'data') # 数据⽬录
test_path = os.path.join(prj_path, 'test') # ⽤例⽬录
log_file = os.path.join(prj_path, 'log', 'log.txt') # 更改路径到log⽬录下
report_file = os.path.join(prj_path, 'report',nowtime +' Report.html') # 更改路径到report⽬录下




logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s %(levelname)s [%(funcName)s:%(filename)s,%(lineno)d]] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=log_file,
                    filemode='a'
                    )



#数据库配置
db_host='47.103.128.20'
db_port=30306
db_user='p2p'
db_passwd='p2p_2019'
db_name='p2p_test'

#邮件配置
sender_user = '15701374212@163.com'     #发件人邮箱
sender_passwd = '1351668Ao'             #发件人客户端授权码
receivers = '1064420684@qq.com'         #收件人邮箱
smtp_ssl_server = 'smtp.163.com'        #发件人服务器地址
subject = '接⼝测试报告'                  #邮件主题

if __name__=='__main__':
    logging.info("hellow")


