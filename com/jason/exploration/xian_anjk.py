#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 14:05
# @Author  : Jason
# @Site    : 
# @File    : xian_anjk.py
# @Software: PyCharm
import  requests
from bs4 import  BeautifulSoup

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

def get_page(url):

    response = requests.get(url,headers=header)
    #print(response.text)


    #通过BeautifulSoup进行解析出每个房源详细列表进行打印

    soup = BeautifulSoup(response.text,'html.parser')
    result_li = soup.find_all('li',{'class':'list-item'})
    #for i in result_li:
        #print(i)

    #进行下一页的爬去
    rest_next_page = soup.find_all('a',{'class':'aNxt'})

    if len(rest_next_page) != 0 :
        get_page(rest_next_page[0].attrs['href'])
    else:
        print('没有下一页了')

    #进行循环遍历其中的房源详细列表
    for i in result_li:
        page_url = str(i)
        soup = BeautifulSoup(page_url,'html.parser')
        result_href = soup.find_all('a',{'class':'houseListTitle'})[0]
        print(result_href.attrs['href'])


if __name__ == '__main__':
    url = 'https://xa.anjuke.com/sale/'
    get_page(url)



