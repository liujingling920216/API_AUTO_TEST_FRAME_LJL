#! /usr/bin/env python
# coding: utf-8
import smtplib
from email.mime.text import MIMEText


# email模块：负责构建邮件
# smtplip模块：负责发送邮件

sender = '1040616989@qq.com'
reciever = 'liujingling0216@163.com'
cc = 'liujingling0216@163.com'
subject = '测试邮件主题'


body = '<h3 align="center">自动化测试报告</h3>'
msg = MIMEText(body,'html','utf-8')
msg['From'] = sender
msg['To'] = reciever
msg['Cc'] = cc
msg['Subject'] = subject

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(user='1040616989@qq.com',password='cmvuhkbgldhxbebh')
smtp.sendmail(sender,reciever,msg.as_string())
smtp.close()










