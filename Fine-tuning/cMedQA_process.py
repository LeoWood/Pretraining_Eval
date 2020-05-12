#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/3/6 10:44
import os
import pandas as pd
from tqdm import tqdm


if __name__ == '__main__':
    path = r"D:\UCAS\Phd\Projects\201908CsciBERT\预训练评测\cMedQA2-master"
    question = pd.read_csv(path + '/question.csv',index_col=0)
    answer = pd.read_csv(path + '/answer.csv',index_col=0)
    train = pd.read_csv(path + '/train_candidates.txt')
    dev = pd.read_csv(path + '/dev_candidates.txt')
    test = pd.read_csv(path + '/test_candidates.txt')

    ## train
    train_set = []
    with open(path + '/train.tsv','w',encoding='utf-8') as f:
        for i in tqdm(range(len(train))):
            q_id = train.iloc[i]['question_id']
            q = question.loc[q_id]['content']
            a_pos_id = train.iloc[i]['pos_ans_id']
            a_pos = answer.loc[a_pos_id]['content']
            train_pos = [q_id,a_pos_id,1]
            if train_pos not in train_set:
                train_set.append(train_pos)
                f.write('1' + '\t' + q + '\t' + a_pos + '\n')

            a_neg_id = train.iloc[i]['neg_ans_id']
            a_neg = answer.loc[a_neg_id]['content']
            train_neg = [q_id,a_neg_id,0]
            if train_neg not in train_set:
                f.write('0' + '\t' + q + '\t' + a_neg + '\n')

    ## dev
    with open(path + '/dev.tsv', 'w', encoding='utf-8') as f:
        for i in tqdm(range(len(dev))):
            q = question.loc[dev.iloc[i]['question_id']]['content']
            a = answer.loc[dev.iloc[i]['ans_id']]['content']
            label = dev.iloc[i]['label']
            f.write(label + '\t' + q + '\t' + a + '\n')

    ## test
    with open(path + '/test.tsv', 'w', encoding='utf-8') as f:
        for i in tqdm(range(len(test))):
            q = question.loc[test.iloc[i]['question_id']]['content']
            a = answer.loc[test.iloc[i]['ans_id']]['content']
            label = test.iloc[i]['label']
            f.write(label + '\t' + q + '\t' + a + '\n')




