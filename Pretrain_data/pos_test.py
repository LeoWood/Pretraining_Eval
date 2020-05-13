#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/5/12 17:12

import time

import pkuseg

pku_seg = pkuseg.pkuseg(model_name='medicine',user_dict = r'F:\LiuHuan\Projects\UER-py\uer\utils\medical_terms\MedicalTerms(MeSH+Meddical_KG).txt',postag=True)


def pku(line):
    pku_result = pku_seg.cut(line)
    return [(word, tag) for (word, tag) in pku_result]


# import thulac
#
# thup = thulac.thulac()
#
#
# def thu(line):
#     thulac_result = thup.cut(line)
#     return [(word, tag) for (word, tag) in thulac_result]
#
#
# from pyhanlp import HanLP
#
#
# def han(line):
#     hanlp_resut = HanLP.segment(line)
#     return [(term.word, term.nature) for term in hanlp_resut]


# from stanfordcorenlp import StanfordCoreNLP
#
# stanford_nlp = StanfordCoreNLP(r'F:\LiuHuan\stanford-corenlp-4.0.0', lang='zh')


# def stanford(line):
#     stanford_resut = stanford_nlp.pos_tag(line)
#     return [(word, tag) for (word, tag) in stanford_resut]


with open('R_test.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

for pos in [pku]:
    t1 = time.time()
    with open(pos.__name__ + '_mix.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(str(pos(line)) + '\n')
        t2 = time.time()
        print(pos.__name__ + "用时：" + str(t2 - t1))
        f.write(pos.__name__ + "用时：" + str(t2 - t1))

if __name__ == '__main__':
    pass
