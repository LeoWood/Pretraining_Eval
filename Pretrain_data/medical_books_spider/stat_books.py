#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/5/15 22:29
import os

if __name__ == '__main__':
    num = 0
    for file in os.listdir('books'):
        with open(file,'r',encoding='utf-8') as f:
            num += len(f.readlines())
    print(num)