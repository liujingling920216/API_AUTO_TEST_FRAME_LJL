import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender = '1040616989@qq.com'
reciever = 'liujingling0216@163.com'
cc = 'liujingling0216@163.com'
subject = '测试邮件主题'


body = '<h3 align="center">自动化测试报告</h3>'

msg = MIMEMultipart()
msg.attach(MIMEText(body,'html','utf-8'))
msg['From'] = sender
msg['To'] = reciever
msg['Cc'] = cc
msg['Subject'] = subject

html_path = os.path.dirname(__file__)+'/../test_reports/P1P2接口自动化测试报告V1.4/P1P2接口自动化测试报告V1.4.html'
print(os.path.basename(html_path))   #获取文件名称


#构造html附件
attach_file = MIMEText(open(html_path,'rb').read(),'base64','utf-8')
attach_file["Content-Type"] = 'application/octet-stream'
attach_file.add_header("Content-Disposition",'attachment',filename=(os.path.basename(html_path)))
msg.attach(attach_file)

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(user='1040616989@qq.com',password='cmvuhkbgldhxbebh')
smtp.sendmail(sender,reciever,msg.as_string())
smtp.close()



