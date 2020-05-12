#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/3/6 12:02

import json
from tqdm import tqdm

if __name__ == '__main__':
    path = r"D:\UCAS\Phd\Projects\201908CsciBERT\预训练评测\关键词识别\csl_public"
    for file in ['/train','/dev','/test']:
        with open(path + file + '.tsv', 'w', encoding='utf-8') as fw:
            with open(path + file + '.json', 'r', encoding='utf-8') as f:
                fw.write('label\ttext_a\ttext_b\n')
                for line in f.readlines():
                    line = line.strip()
                    data = json.loads(line)
                    # print(data)
                    fw.write(data['label'] + '\t' + ' '.join(data['keyword']) + '\t' + data['abst'] + '\n')
