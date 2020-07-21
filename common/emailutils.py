import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.configutils import config_utils

class EmailUtils():
    def __init__(self,smtp_body,smtp_attch_path=None):
        self.smtp_server = config_utils.SMTP_SERVER
        self.smtp_sender = config_utils.SMTP_SENDER
        self.smtp_password = config_utils.SMTP_PASSWORD
        self.smtp_receiver = config_utils.SMTP_RECEIVER
        self.smtp_cc = config_utils.SMTP_CC
        self.smtp_subject = config_utils.SMTP_SUBJECT
        self.smtp_body = smtp_body
        self.smtp_attch = smtp_attch_path

    def mail_message_info(self):
        msg = MIMEMultipart()
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        msg.attach(MIMEText(self.smtp_body,'html','utf-8'))
        if self.smtp_attch:
            '''构建html附件'''
            attach_file = MIMEText(open(self.smtp_attch,'rb').read(),'base64','utf-8')
            attach_file['Content-Type'] = 'application/octet-stream'
            attach_file.add_header('Content-Disposition','attachment', filename=('gbk', '', os.path.basename(self.smtp_attch)))
            msg.attach(attach_file)
        return msg

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_password)
        smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(",")+ self.smtp_cc.split(","), self.mail_message_info().as_string())
        smtp.close()


if __name__ == '__main__':
    mail_body = '<h3 align="center">自动化测试报告</h3>'
    attach_path = os.path.dirname(__file__) + '/../reports/P1P2接口自动化测试报告V1.4/P1P2接口自动化测试报告V1.4.html'
    EmailUtils(mail_body,attach_path).send_mail()



