from urllib import request
from bs4 import BeautifulSoup as bs
import re
import matplotlib.pyplot as plt
import random
import matplotlib
import jieba
from collections import Counter
from wordcloud import WordCloud
import jieba
import codecs
import jieba.posseg as pseg


def dilidili_crawler():
    age_list = ['10', '11', '12', '13', '14', '15', '16', '17', '18']
    mth_list = ['01', '04', '07', '10']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    html = request.urlopen(
        request.Request(url="http://www.dilidili.name/anime/201907/", headers=headers)).read().decode("utf-8")
    # print(html)
    return html


def crawler():
    html = request.urlopen("http://www.nuc.edu.cn").read().decode("utf-8")
    print(html)


def crosswise_bar():
    matplotlib.rc('font', family='SimHei', weight='bold')

    city_name = ['北京', '上海', '广州', '深圳', '成都']
    city_name.reverse()

    data = []
    for i in range(len(city_name)):
        data.append(random.randint(100, 200))

    colors = ['red', 'yellow', 'blue', 'green', 'gray']
    colors.reverse()

    plt.barh(range(len(data)), data, tick_label=city_name, color=colors)

    # 不要X横坐标标签。
    # plt.xticks(())

    plt.show()


def word_cloud():
    content = open(r'../res/strike_the_blood.txt', encoding='utf-8')
    mylist = list(content)
    # print(content)
    # con_words = [x for x in jieba.cut(content) if len(x) >= 2]
    # print(Counter(con_words).most_common(100))
    word_list = [' '.join(jieba.cut(sen)) for sen in mylist]
    con_words = ' '.join(word_list)
    wordcloud_tmp = WordCloud(font_path='../res/SimHei.ttf', background_color='black').generate(con_words)
    plt.imshow(wordcloud_tmp)
    plt.axis('off')
    plt.show()


def netword_vis():
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
        f.write("First Second Weight\r\n")
        for name, edges in relationships.items():
            for v, w in edges.items():
                if w > 3:
                    f.write(name + " " + v + " " + str(w) + "\r\n")


if __name__ == "__main__":
    # html = dilidili_crawler()
    # d_soup = bs(html, features="lxml")
    # anime_rank_list = d_soup.find(name='div', attrs={'class': 'rm_con'})
    # # print(dl)
    # # for dl in anime_list.find_all(name='dl'):
    # #     print(dl.find(name='h3').find(name='a').string)
    # #     for tag in dl.find_all(name='div', attrs={'class': 'd_label'}):
    # #         # if (tag.string != None):
    # #         label = tag.find_all(name='a')
    # #         # print(tal.string for tal in label)
    # #         for tal in label:
    # #             print(tal.string)
    # for ul in anime_rank_list.find_all(name='ul', attrs={'class': 'textlist'}):
    #     for li in ul.find_all(name='li'):
    #         d_score = li.find(name='em')
    #         print(d_score.string)
    #         d_name = li.find(name='a')
    #         print(d_name.string)
    # crosswise_bar()
    # word_cloud()
    netword_vis()
