#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/5/7 20:58


if __name__ == '__main__':
    path = r"D:\UCAS\Phd\Projects\201908CsciBERT\预训练评测\datasets\AMTTL"
    for file in ['//train','//dev','//test']:
        with open(path + file + '.txt', 'r',encoding='utf-8') as fr:
            with open(path + '//UER_data' + file + '.tsv', 'w', encoding='utf-8') as fw:
                fw.write('text_a\tlabel\n')
                text_a = []
                label = []
                for line in fr.readlines():
                    line = line.strip()
                    if not line:
                        if len(text_a)>0:
                            fw.write(' '.join(text_a) + '\t' + ' '.join(label) + '\n')
                            text_a = []
                            label = []
                    else:
                        text_a.append(line.split()[0])
                        label.append(line.split()[1].replace('S','O'))


