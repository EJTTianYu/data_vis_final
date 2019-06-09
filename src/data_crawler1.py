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
    with open(r'../res/anime_rank.csv', 'w', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['anime_season', 'anime_name', 'anime_type'])
        for i in html_dict.keys():
            d_soup = bs(html_dict[i], features="lxml")
            anime_rank_list = d_soup.find(name='div', attrs={'class': 'rm_con'})
            # print(dl)
            for ul in anime_rank_list.find_all(name='ul', attrs={'class': 'textlist'}):
                for li in ul.find_all(name='li'):
                    anime_item = []
                    anime_item.append(i)
                    d_score = li.find(name='em')
                    # print(d_score.string)
                    d_name = li.find(name='a')
                    # print(d_name.string)
                    anime_item.append(d_name.string)
                    anime_item.append(d_score.string)
                    writer.writerow(anime_item)
