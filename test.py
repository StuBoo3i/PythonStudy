import requests

login_url = 'http://192.168.249.131/pikachu/vul/sqli/sqli_id.php'
data = {
    'id': '2',
    'submit': '提交'
}

# 创建会话对象
session = requests.Session()

# 发送登录请求，获取并保存 Cookie
response = session.post(login_url, data=data)
cookies = response.cookies

print(response.text)
