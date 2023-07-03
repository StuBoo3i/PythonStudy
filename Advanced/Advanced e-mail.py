#发送邮件

'''
SMTP 全称 Simple Mail Transfer Protocol，中文译为简单邮件传输协议，它能跨越网络传输邮件，可实现相同网络处理进程之间的邮件传输，
也可通过中继器或网关实现进程与其他网络之间的邮件传输。

Python 的 smtplib 模块对 SMTP 做了封装，可以很方便的实现邮件的发送，同时提供了 email 模块来构造邮件。

smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)

用于创建 SMTP 对象。参数说明如下：

    host：SMTP 服务器主机。

    port：端口号。

    local_hostname：如果 SMTP 在本机，只需指定服务器地址为 localhost 即可。

    timeout：指定超时时间，可选。

    source_address：该参数允许绑定到具有多个网络接口的计算机中的某些特定源地址或某些特定源 TCP 端口。

SMTP.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())

发送邮件。参数说明如下：

    from_addr：邮件发送者地址。

    to_addrs：邮件接收者地址。

    msg：邮件内容。

'''

#发送简单邮件
import smtplib
from email.mime.text import MIMEText

# 发送者邮箱地址
senderMail = 'neuwangjiabo@163.com'
# 发送者邮箱授权码
authCode = 'VLQVBNGNHWFEVTBL'
# 接收者邮箱地址
receiverMail = '2839430364@qq.com'
# 邮件主题
subject = '简单邮件'
# 邮件内容
content = 'hello email'
msg = MIMEText(content, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = senderMail
msg['To'] = receiverMail
try:
    server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
    print('成功连接到邮件服务器')
    server.login(senderMail, authCode)
    print('成功登录邮箱')
    server.sendmail(senderMail, receiverMail, msg.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as e:
    print('邮件发送异常')
finally:
    server.quit()
