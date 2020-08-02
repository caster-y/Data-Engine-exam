# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
list_img=[]
list_name=[]
list_HighPrice=[]
list_LowPrice=[]
# 请求URL
url = 'http://car.bitauto.com/xuanchegongju/?l=8&mid=8'
# 得到页面的内容
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
html=requests.get(url,headers=headers,timeout=10)
content = html.text
# 通过content创建BeautifulSoup对象
soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')

#找到完整的信息
temp=soup.find('div',class_ = "search-result-list")
df=pd.DataFrame()
temp_list=temp.find_all('a')
for i in temp_list:
    list_name.append(i.p.string)
    a=i.p.next_sibling.next_sibling.string[:-1]
    list_LowPrice.append(a.split('-')[0])
    list_HighPrice.append(a.split('-')[-1])
df['名称']=list_name
df['最低价格']=list_LowPrice
df['最高价格']=list_HighPrice
temp_list_img=temp.find_all('img')
for i in temp_list_img:
    list_img.append(i.get('src'))
df['图片及链接']=list_img   
df.to_csv('ProjectA.csv')

