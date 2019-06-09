# coding=utf-8
import csv
import numpy as np
import pandas as pd
from itertools import islice
import jieba
import codecs
import jieba.posseg as pseg

'''用于统计每个季度的动漫数量'''


def process_data0():
    anime_data = pd.read_csv(r'../res/anime_data.csv')
    # print(anime_data.head())
    # 用于记录根据日起分组的data
    data_groupby_season = anime_data.groupby('anime_season', as_index=False).count()
    print(data_groupby_season.columns)
    output = pd.DataFrame(
        data={"anime_season": data_groupby_season["anime_season"].tolist(),
              "anime_num": data_groupby_season["anime_name"].tolist()})
    output.to_csv('../res/anime_num.csv', index=False)


'''用于统计每年的动漫数量'''


def process_data1():
    with open(r'../res/anime_num.csv', 'r') as inputFile, open(r'../res/anime_num1.csv', 'w',
                                                               encoding='utf-8') as outputFile:
        reader = csv.reader(inputFile)
        writer = csv.writer(outputFile)
        writer.writerow(['year', 'anime_num'])
        year = 2010
        sum = 0
        for line in islice(reader, 1, None):
            print(line)
            if int(line[0][0:4]) == year:
                sum += int(line[1])
            else:
                writer.writerow([year, sum])
                year = int(line[0][0:4])
                sum = int(line[1])


'''用于统计所有的动漫类型'''


def type_ana():
    with open(r'../res/anime_data.csv', 'r') as inputFile:
        reader = csv.reader(inputFile)
        word_set = set()
        for line in islice(reader, 1, None):
            # for word in str(line[2]).split(sep=' '):
            #     if word not in word_set:
            #         word_set.add(word)
            word_set.add(str(line[2]).split(sep=' ')[0])
            # if str(line[2]).split(sep=' ')[0]=='':
            #     print(line[2])
        # print(word_set)
        return word_set


def process_data2(year, word_set):
    with open(r'../res/anime_data.csv', 'r') as inputFile, open(r'../res/anime_num2.csv', 'w',
                                                                encoding='utf-8') as outputFile:
        reader = csv.reader(inputFile)
        writer = csv.writer(outputFile)
        writer.writerow(['anime_type', 'anime_num'])
        dict_type = dict()
        for line in islice(reader, 1, None):
            if int(line[1][0:4]) == year:
                if str(line[2]).split(sep=' ')[0] not in dict_type:
                    dict_type[str(line[2]).split(sep=' ')[0]] = 1
                else:
                    dict_type[str(line[2]).split(sep=' ')[0]] += 1
        # print(dict_type)
        for item in dict_type.items():
            writer.writerow(item)


def process_data3(year, month):
    with open(r'../res/anime_rank.csv', 'r') as inputFile, open(r'../res/anime_num3.csv', 'w',
                                                                encoding='utf-8-sig') as outputFile:
        reader = csv.reader(inputFile)
        writer = csv.writer(outputFile)
        writer.writerow(['anime_name', 'd_score'])
        for line in islice(reader, 1, None):
            if int(line[0]) == int(str(year) + str(month)):
                # print(line[2])
                writer.writerow([line[1], str(line[2]).replace('D值:', '')])


def process_data4(inputFile, outputFile):
    infopen = open(inputFile, 'r', encoding="utf-8")
    outfopen = open(outputFile, 'w', encoding="utf-8")

    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")

    infopen.close()
    outfopen.close()


def process_data5():
    names = {}  # 姓名字典
    relationships = {}  # 关系字典
    lineNames = []  # 每段内人物关系
    # count names
    jieba.load_userdict("../res/dict.txt")  # 加载字典
    with codecs.open("../res/strike_the_blood_pro.txt", "r", "utf-8") as f:
        for line in f.readlines():
            poss = pseg.cut(line)  # 分词并返回该词词性
            lineNames.append([])  # 为新读入的一段添加人物名称列表
            for w in poss:
                if w.flag != "nrj" or len(w.word) < 2:
                    continue  # 当分词长度小于2或该词词性不为nr时认为该词不为人名
                lineNames[-1].append(w.word)  # 为当前段的环境增加一个人物
                if names.get(w.word) is None:
                    names[w.word] = 0
                    relationships[w.word] = {}
                names[w.word] += 1  # 该人物出现次数加 1
    # explore relationships
    for line in lineNames:  # 对于每一段
        for name1 in line:
            for name2 in line:  # 每段中的任意两个人
                if name1 == name2:
                    continue
                if relationships[name1].get(name2) is None:  # 若两人尚未同时出现则新建项
                    relationships[name1][name2] = 1
                else:
                    relationships[name1][name2] = relationships[name1][name2] + 1  # 两人共同出现次数加 1

    with codecs.open("../res/strike_the_blood_relationship.txt", "w", "utf-8") as f:
        f.write("First,Second,Weight\r\n")
        for name, edges in relationships.items():
            for v, w in edges.items():
                if w > 3:
                    f.write(name + "," + v + "," + str(w) + "\r\n")


if __name__ == '__main__':
    # process_data0()
    process_data1()
    # word_set = type_ana()
    # process_data2(2010, word_set)
    # process_data3(2010, '01')
    # process_data4(r'../res/strike_the_blood.txt', '../res/strike_the_blood_pro.txt')
    # process_data5()
