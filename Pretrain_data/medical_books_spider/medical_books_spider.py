#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/5/14 21:12

from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
import requests
import os

def get_driver():
    chromedriver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    return driver

def get_driver_ph():
    driver = webdriver.PhantomJS(executable_path=r"F:\LiuHuan\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    return driver

def page_to_txt(filename,pagesoup):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(pagesoup)



if __name__ == '__main__':
    books_pCls = []
    with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
        books_pCls = [line.strip().split() for line in f.readlines()]

    driver = get_driver()
    i = 0
    for title,link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt','w',encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1,5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source,"html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file,soup.prettify())

            # 存正文内容
            for p in soup.find_all('div',class_='pCls'):
                fw.write(p.get_text() + '\n')


            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1,5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                # 存正文内容
                for p in soup.find_all('div', class_='pCls'):
                    fw.write(p.get_text() + '\n')

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break
