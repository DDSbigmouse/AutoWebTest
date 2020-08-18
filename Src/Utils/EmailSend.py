# -*- coding: utf-8 -*-



import sys
from email.utils import parseaddr, formataddr
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
import os



# 邮件主题
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def SendEmialNoitce(message_str):
    # Step 1：
    # 构造MIMEText对象
    msg = MIMEText(message_str, 'plain', 'utf-8')

    # Step 2：
    from_addr = '15021660228@163.com' # Email地址
    password =  'JOSHUA8989' # 口令
    # to_addr1 = 'sei_lzy2011@163.com'#  收件人地址 1:
    to_addr2 = '15021660228@163.com'# 收件人地址 2:
    smtp_server = 'smtp.163.com' # SMTP服务器地址

    # Step 3：
    # 邮件格式化
    msg['From'] = _format_addr('Python大佬DDS <%s>' % from_addr) # 发件人
    # msg['To'] = _format_addr('小黄人 <%s>' % to_addr1) # 收件人
    msg['To'] = _format_addr('小黄人 <%s>' % to_addr2) # 收件人
    msg['Subject'] = Header('来自电电猪的报告……', 'utf-8').encode() # 主题

    # Step 4：
    # SMTP协议就是简单的文本命令和响应
    print('开始发送邮件')
    server = SMTP_SSL(smtp_server,465)        # SSL安全协议端口是465
    # server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    # server.set_debuglevel(1) # 打印出和SMTP服务器交互的所有信息
    server.login(from_addr, password) # 登录SMTP服务器
    server.sendmail(from_addr, [to_addr2], msg.as_string()) #可以一次发给多个人，所以传入一个list ,as_string()把MIMEText对象变成str
    server.quit()
    print('发送邮件完毕')






if __name__ == '__main__':
    SendEmialNoitce();