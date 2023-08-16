import smtplib
from email.mime.text import MIMEText

class Mail(object):
    def __init__(self, mail_host, mail_user, mail_pass, mail_sender, mail_receivers):
        # 设置服务器所需信息
        self.mail_host = mail_host #163邮箱服务器地址
        self.mail_user = mail_user #163用户名
        self.mail_pass = mail_pass #密码(部分邮箱为授权码)
        self.sender = mail_sender #邮件发送方邮箱地址
        self.receivers = mail_receivers #邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发

    def send(self, title, text):
        message = MIMEText(text, 'plain', 'utf-8')
        message['Subject'] = title
        message['From'] = self.sender
        message['To'] = self.receivers[0]

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.mail_host, 25)
            # 登录到服务器
            smtpObj.login(self.mail_user, self.mail_pass)
            # 发送
            smtpObj.sendmail(
                self.sender, self.receivers, message.as_string())
            # 退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误

if __name__ == '__main__':
    Email = Mail('smtp.163.com', 'xl20210613@163.com', 'YLCYZGMGFZBTLTWH', 'xl20210613@163.com', ['xl20210613@163.com'])
    Email.send('Self-CheckIn', '')