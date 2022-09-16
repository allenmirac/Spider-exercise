from unicodedata import name
import requests
from lxml import etree
import os

url = "http://pic.netbian.com/"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.56'
}
page_text = requests.get(url, headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul[@class="clearfix"]/li')
# print(len(li_list))
# a=0
if not os.path.exists("./Spider/彼岸"):
    os.mkdir("./Spider/彼岸")
for li in li_list:
    href = url + li.xpath('./a/@href')[0]
    # if a==0:
        # print(href)
        # a+=1
    img_text = requests.get(href, headers).text
    img_tree = etree.HTML(img_text)

    # 爬取图片地址，名称
    detail_url = url + img_tree.xpath('//div[2]/div[1]/div[@class="photo"]/div[1]/div[2]/a/img/@src')[0]
    detail_name = img_tree.xpath('//div[2]/div[1]/div[@class="photo"]/div[1]/div[1]/h1/text()')[0]+'.jpg'
    # print(detail_name)

    detail_name = detail_name.encode('iso-8859-1').decode('gbk')
    img_data = requests.get(detail_url, headers).content # 返回图片的编码

    with open("./Spider/彼岸/"+detail_name, "wb") as fp:
        fp.write(img_data)