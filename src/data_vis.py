# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import operator
from functools import reduce
from matplotlib.font_manager import _rebuild
import jieba
from collections import Counter
from wordcloud import WordCloud
from scipy.misc import imread
import codecs
import jieba.posseg as pseg
import networkx as nx

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


# 用于可视化任务1，绘制散点图
def data_vis0():
    df_data = pd.read_csv('../res/anime_num1.csv')
    df_data.head()

    fig, ax = plt.subplots()
    colors = ['#99CC01', '#FFFF01', '#0000FE', '#FE0000', '#A6A6A6', '#D9E021', '#FFF16E', '#0D8ECF', '#FA4D3D']
    ax.scatter(df_data['year'], df_data['anime_num'], s=df_data['anime_num'] * 20,
               c=colors, alpha=0.6)

    ax.set_xlabel('anime_season')
    ax.set_ylabel('anime_num')
    ax.set_title('anime num vis')

    ax.grid(True)
    fig.tight_layout()
    # plt.xticks([])
    plt.xlim((2009, 2019))
    plt.ylim((0, 200))
    plt.show()


# 用于可视化任务2，绘制饼图
def data_vis1():
    df_data = pd.read_csv('../res/anime_num2.csv')
    labels = df_data['anime_type'].tolist()
    sizes = df_data['anime_num'].tolist()
    # explode = []
    # for item in df_data['anime_num'].tolist():
    #     if int(item) > 5:
    #         explode.append(0.1)
    #     else:
    #         explode.append(0)

    colors = ['#99CC01', '#FFFF01', '#66CCFF', '#FF6600', '#A6A6A6', '#D9E021', '#FFF16E', '#0D8ECF', '#FA4D3D',
              '#D2D2D2', '#FFDE45', '#9b59b6']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    plt.show()


# 用于可视化任务3，绘制横向直方图
def data_vis2():
    df_data = pd.read_csv('../res/anime_num3.csv')
    anime_names = df_data['anime_name'].tolist()
    anime_names.reverse()
    d_scores = df_data['d_score'].tolist()
    d_scores.reverse()
    colors = ['#99CC01', '#FFFF01', '#66CCFF', '#FF6600', '#A6A6A6', '#D9E021', '#FFF16E', '#0D8ECF', '#FA4D3D',
              '#D2D2D2', '#FFDE45', '#9b59b6']
    colors.reverse()
    plt.barh(range(len(d_scores)), d_scores, tick_label=anime_names, color=colors, alpha=0.6)
    plt.show()


# 用于可视化任务4，绘制词云
def txt_ana():
    content = open(r'../res/strike_the_blood_pro.txt', encoding='utf-8')
    mylist = list(content)
    # print(content)
    # con_words = [x for x in jieba.cut(content) if len(x) >= 2]
    # print(Counter(con_words).most_common(100))
    word_list = [' '.join(jieba.cut(sen)) for sen in mylist]
    con_words = ' '.join(word_list)
    mask = imread('../res/chac1.jpeg')
    wordcloud_tmp = WordCloud(font_path='../res/SimHei.ttf', background_color='white', mask=mask).generate(con_words)
    plt.imshow(wordcloud_tmp)
    plt.axis('off')
    plt.show()


def network_vis():
    strike_df = pd.read_csv(r'../res/strike_the_blood_relationship.txt')
    strike_df['weight'] = strike_df.Weight / 120
    strike_df2 = strike_df[strike_df.weight > 0.025].reset_index(drop=True)
    plt.figure(figsize=(12, 12))
    G = nx.Graph()
    for ii in strike_df2.index:
        G.add_edge(strike_df2.First[ii], strike_df2.Second[ii], weight=strike_df2.weight[ii])
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.2]
    emidle = [(u, v) for (u, v, d) in G.edges(data=True) if (d['weight'] > 0.1 and d['weight'] <= 0.2)]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.1]
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, alpha=0.6, node_size=350)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=2, alpha=0.9, edge_color='g')
    nx.draw_networkx_edges(G, pos, edgelist=emidle, width=1.5, alpha=0.6, edge_color='y')
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1, alpha=0.3, edge_color='g', style='dashed')
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.axis('off')
    plt.title("《噬血狂袭》第三卷 天使炎 社交网络可视化")
    plt.show()


if __name__ == '__main__':
    # _rebuild()
    # data_vis1()
    # data_vis2()
    # txt_ana()
    network_vis()
