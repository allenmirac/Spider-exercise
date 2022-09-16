import requests

session = requests.Session()
url = "https://passport.17k.com/ck/user/login"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56'
}
data = {
    "loginName":"13222630915",
    "password":"Wang1998"
}
res = session.post(url, data, headers)
# page_text = res.text
# with open("Spider/17K.html", "w", encoding="utf-8") as fp:
#     fp.write(page_text)
resp = session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp.text)
