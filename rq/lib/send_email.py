#coding=utf-8
import smtplib  #建立smtp连接
from email.mime.text import MIMEText #邮件格式

# 1. 编写邮件内容（Email邮件需要专⻔的MIME格式）
msg = MIMEText('this is a test email', 'plain', 'utf-8') # plain指普通⽂本格式邮件内容
# 2. 组装Email头（发件⼈，收件⼈，主题）
msg['From'] = '15701374212@163.com' # 发件⼈
msg['To'] = '1064420684@qq.com' # 收件⼈
msg['Subject'] = 'Api Test Report' # 邮件主题
# 3. 连接smtp服务器并发送邮件
smtp = smtplib.SMTP_SSL('smtp.163.com') # smtp服务器地址 使⽤SSL模式
smtp.login('15701374212@163.com', 'Ao1351668') # ⽤户名和密码
smtp.sendmail("15701374212@163.com", "1064420684@qq.com", msg.as_string())
smtp.quit()