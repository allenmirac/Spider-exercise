# https://juejin.cn/post/7082986114885091358
import csv					#保存在excel表格中
import requests				
from lxml import etree
from threading import Lock, Thread	#加入锁
import json
from concurrent.futures import ThreadPoolExecutor	#用了但是不知道为什么没有用，线程池：https://juejin.cn/post/6844903861245706253
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

def get_price(url, i):
    resp = requests.get(url, header)
    page_text = resp.text
    resp_json = json.loads(page_text)
    price_list = resp_json['list']
    # with open("Spider/json.txt", 'a+', encoding='utf-8') as fp:
    #     if fp.write(resp_json):
    #         print("Succeed!")
    # print(resp_json['list'])
    
    for i in price_list:
        name = i['prodName']
        price = i['avgPrice']
        detail = name+price
        with open('Spider/output/Price.csv', 'a+', encoding='gbk', newline='') as fp:
            fp = csv.writer(fp)
            fp.writerow(name+price)
    print(f'第{i}页爬取成功...........')
if __name__ == '__main__':
    lock = Lock()
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 30):
		  #t.submit(get_price,url = f'http://xinfadi.com.cn/getPriceData.html?current={i}',page_info = i)
            url = f'http://xinfadi.com.cn/getPriceData.html?current={i}'
            get_price(url, i)