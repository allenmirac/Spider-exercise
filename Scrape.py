# urljoin一看就懂
# 主要是data的写法，为什么只能固定
# 两种写法：1、使用两个request，2、使用session保存登录的Cookies信息。
# 1、前面的那个requests来保存Cookies信息，并且不允许重定向（allow_redirects=False）后面的requests使用这个Cookies
# 2、使用session直接保存了Cookies，可以直接登录，
# session你可以认为是一连串的请求，在这个过程中 都cookie不会丢失。

import requests
from urllib.parse import urljoin
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
url = 'https://login2.scrape.center/'
data = {
    'username':'admin',
    'password':'admin'
}
LOGIN_URL = urljoin(url, '/login')
# 方法一
# INDEX_URL = urljoin(url, '/page/1')

# response_login = requests.post(LOGIN_URL, data,header, allow_redirects=False)
# 
# cookies = response_login.cookies
# response_index = requests.get(INDEX_URL,cookies=cookies)
# print('Response Status', response_index.status_code)
# print('Response URL', response_index.url)

# 方法二
session = requests.Session()
# 登录的时候一般使用的是post
resp = session.post(LOGIN_URL, data, header)

with open("Spider/htmlTest/17K.html", "w", encoding='utf-8') as fp:
    if fp.write(resp.text):
        print("fp.write")