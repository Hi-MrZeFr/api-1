# -*- coding: utf-8 -*-
# @Author    : Eurkon
# @Date      : 2021/6/5 10:16

import requests
from bs4 import BeautifulSoup


def weibo_top(params):
    """微博热搜

    Args:
        params (dict): {}

    Returns:
        json: {title: 标题, url: 地址, num: 热度数值, hot: 热搜等级}
    """
    data = []
    response = requests.get('https://s.weibo.com/top/summary/')
    soup = BeautifulSoup(response.text, 'html.parser')
    url = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    num = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')
    hot = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-03')

    for i in range(1, len(url)):
        # 去除广告链接
        if num[i - 1].get_text() != '':
            data.append({
                'title': url[i].get_text(),
                'url': "https://s.weibo.com" + url[i]['href'],
                'num': num[i - 1].get_text(),
                'hot': hot[i].get_text().replace('<i class="icon-txt icon-txt-', '') \
                    .replace('</i>', '').replace('">', '') \
                    .replace('new', '').replace('hot', '').replace('boil', '').replace('boom', '').strip()
            })

    return data


if __name__ == '__main__':
    print(weibo_top({}))