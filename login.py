# 用户登录
import json

import requests

url_login = 'http://backend.mengguochengzhen.cn/v1/public/login'
session = requests.session();
parms_login = {'token': '0', 'username': 'testadmin', 'password': '111111'}
requests_login = session.post(url_login, data=parms_login)
print(json.loads(requests_login.text))