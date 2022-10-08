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

def get_price(url, pege_info):
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
        with open('Spider/output/Price.csv', 'a+', encoding='gbk', newline='') as fp:
            fieldnames = ['菜名', '价格']
            fp = csv.DictWriter(fp, fieldnames)
            # fp.writeheader()
            fp.writerow({'菜名':name, '价格':price})
    print(f'第{pege_info}页爬取成功...........')
if __name__ == '__main__':
    lock = Lock()
    with open('Spider/output/Price.csv', 'a+', encoding='gbk', newline='') as fp:
        fieldnames = ['菜名', '价格']
        fp = csv.DictWriter(fp, fieldnames)
        fp.writeheader()
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 21):
            url=f'http://xinfadi.com.cn/getPriceData.html?current={i}'
            get_price(url, i)