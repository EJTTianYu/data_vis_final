# coding=utf-8
from urllib import request
from bs4 import BeautifulSoup as bs
import re
import csv
import codecs


def dilidili_crawler():
    age_list = ['10', '11', '12', '13', '14', '15', '16', '17', '18']
    mth_list = ['01', '04', '07', '10']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    html_dict = {}
    for year in age_list:
        for month in mth_list:
            html = request.urlopen(
                request.Request(url="http://www.dilidili.name/anime/20{}{}/".format(year, month),
                                headers=headers)).read().decode("utf-8")
            html_dict['20{}{}'.format(year, month)] = html
    # print(html)
    return html_dict


if __name__ == "__main__":
    html_dict = dilidili_crawler()
    with open(r'../res/anime_data.csv', 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['anime_name', 'anime_season', 'anime_type'])
        for i in html_dict.keys():
            d_soup = bs(html_dict[i], features="lxml")
            anime_list = d_soup.find(name='div', attrs={'class': 'anime_list'})
            # print(dl)
            for dl in anime_list.find_all(name='dl'):
                anime_item = []
                # print(dl.find(name='h3').find(name='a').string)
                # print(i)
                anime_item.append(dl.find(name='h3').find(name='a').string)
                anime_item.append(i)
                for tag in dl.find_all(name='div', attrs={'class': 'd_label'}):
                    des = tag.find(name='b')
                    # print(des.string)
                    # if des.string == r'年代：':
                    #     label = tag.find(name='a')
                    #     print(tag.string if label == None else label.string)
                    if des.string == r'标签：':
                        # if (tag.string != None):
                        label_string = ''
                        labels = tag.find_all(name='a')
                        # print(tal.string for tal in label)
                        for tal in labels:
                            # print(tal.string)
                            label_string = label_string + tal.string + ' '
                        anime_item.append(label_string)
                writer.writerow(anime_item)
