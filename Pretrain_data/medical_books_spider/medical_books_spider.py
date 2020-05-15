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

def pCls():
    with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
        books_pCls = [line.strip().split() for line in f.readlines()]

    driver = get_driver()
    i = 0
    for title, link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())

            # 存正文内容
            for p in soup.find_all('div', class_='pCls'):
                fw.write(p.get_text().strip().replace('\n','') + '\n')


            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                ## 去参考文献
                cite = driver.find_elements_by_xpath('//div[@class="h4" and contains(text(),"参考文献")]')
                if cite:
                    continue

                # 存正文内容
                for p in soup.find_all('div', class_='pCls'):
                    fw.write(p.get_text().strip().replace('\n','') + '\n')

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break

def p_no_class():
    with open('titles_urls_p.txt', 'r', encoding='utf-8') as f:
        books_p_no_class = [line.strip().split() for line in f.readlines()]

    driver = get_driver()
    i = 0
    for title, link in books_p_no_class:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())


            # 存正文内容
            try:
                for p in driver.find_elements_by_xpath('//p[not(@class)]'):
                    fw.write(p.text + '\n')
            except:
                pass

            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())


                # 存正文内容
                try:
                    for p in driver.find_elements_by_xpath('//p[not(@class)]'):
                        fw.write(p.text + '\n')
                except:
                    pass

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break

def p_content():
    # with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
    #     books_pCls = [line.strip().split() for line in f.readlines()]
    books_pCls = [['临床心电图详解与诊断','https://yixueshu.gitee.io/xdtxj/text00002.html#chapter3'],['微生物学','https://yixueshu.gitee.io/wswx/text00005.html']]
    driver = get_driver()
    i = 0
    for title, link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())

            # 存正文内容
            for p in soup.find_all('p', class_='content'):
                fw.write(p.get_text() + '\n')

            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                # 存正文内容
                for p in soup.find_all('p', class_='content'):
                    fw.write(p.get_text() + '\n')

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break


def p_body():
    # with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
    #     books_pCls = [line.strip().split() for line in f.readlines()]
    books_pCls = [['Duus神经系统疾病定位诊断学','https://yixueshu.gitee.io/duus/text00009.html#bookmark20']]
    driver = get_driver()
    i = 0
    for title, link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())

            # 存正文内容
            for p in soup.find_all('p', class_='p_body_text_first_indent'):
                fw.write(p.get_text() + '\n')

            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                # 存正文内容
                for p in soup.find_all('p', class_='p_body_text_first_indent'):
                    fw.write(p.get_text() + '\n')

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break

def p_align():
    # with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
    #     books_pCls = [line.strip().split() for line in f.readlines()]
    books_pCls = [['医学检验项目选择与临床应用','https://yixueshu.gitee.io/yxjy/text00000.html#filepos0000058782']]
    driver = get_driver()
    i = 0
    for title, link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())

            # 存正文内容
            try:
                for p in driver.find_elements_by_xpath('//p[not(@align)]'):
                    fw.write(p.text + '\n')
            except:
                pass

            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                # 存正文内容
                try:
                    for p in driver.find_elements_by_xpath('//p[not(@align)]'):
                        fw.write(p.text + '\n')
                except:
                    pass

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break


def p_normal():
    # with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
    #     books_pCls = [line.strip().split() for line in f.readlines()]
    books_pCls = [['临床营养学','https://yixueshu.gitee.io/lcyyx/text00002.html']]
    driver = get_driver()
    i = 0
    for title, link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())

            # 存正文内容
            for p in soup.find_all('p', class_='normaltext'):
                fw.write(p.get_text() + '\n')

            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                # 存正文内容
                for p in soup.find_all('p', class_='normaltext'):
                    fw.write(p.get_text() + '\n')

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break

def p_normal_1():
    # with open('titles_urls_pCls.txt', 'r', encoding='utf-8') as f:
    #     books_pCls = [line.strip().split() for line in f.readlines()]
    books_pCls = [['生理学','https://yixueshu.gitee.io/slx/text00004.html']]
    driver = get_driver()
    i = 0
    for title, link in books_pCls:
        if not os.path.exists(title):
            os.mkdir(title)
        with open(title + '.txt', 'w', encoding='utf-8') as fw:
            driver.get(link)
            time.sleep(random.randint(1, 5))

            # 存源代码
            soup = BeautifulSoup(driver.page_source, "html.parser")
            source_file = title + '/' + str(i) + '.html'
            page_to_txt(source_file, soup.prettify())

            # 存正文内容
            for p in soup.find_all('p', class_='normaltext1'):
                fw.write(p.get_text() + '\n')

            go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
            go_on.click()

            while True:
                i += 1
                time.sleep(random.randint(1, 5))

                # 存源代码
                soup = BeautifulSoup(driver.page_source, "html.parser")
                source_file = title + '/' + str(i) + '.html'
                page_to_txt(source_file, soup.prettify())

                # 存正文内容
                for p in soup.find_all('p', class_='normaltext1'):
                    fw.write(p.get_text() + '\n')

                try:
                    go_on = driver.find_element_by_xpath('//button[@onclick="nextPage()"]')
                    go_on.click()
                except:
                    print(title, 'Done~')
                    break


if __name__ == '__main__':
    pCls()
    exit()
    p_no_class()
    p_align()
    p_body()
    p_content()
    p_normal()
    p_normal_1()
