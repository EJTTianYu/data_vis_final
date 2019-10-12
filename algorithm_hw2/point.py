# coding=utf-8

import time
import logging
import random


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "数据点的横坐标:{}, 纵坐标:{}".format(self.x, self.y)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# 用于生成随机点,生成的随机点的横纵坐标均为[0,100000]间的两位小数
def generate_point():
    x = round(random.uniform(0, 100000), 2)
    y = round(random.uniform(0, 100000), 2)
    return Point(x, y)


# 用于生成平面上的随机点列表
def generate_point_list(point_num):
    point_list = []
    for i in range(point_num):
        point_list.append(generate_point())
    return point_list


# 用于计算两点的欧式距离
def cal_distance(point_a, point_b):
    return ((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2) ** (1 / 2)


# 暴力算法,算法复杂度为O(n^2)
def violent_solution(point_list):
    point_num = len(point_list)
    if point_num < 2:
        logging.error("点数少于2，程序即将退出")
    if point_num == 2:
        point_pair_list = []
        point_pair_list.append(point_list[0])
        point_pair_list.append(point_list[1])
        return point_pair_list
    point_pair_list = []
    point_p = point_list[0]
    point_q = point_list[1]
    min_dist = cal_distance(point_p, point_q)
    for i in range(point_num):
        for j in range(i + 1, point_num):
            distance = cal_distance(point_list[i], point_list[j])
            if distance < min_dist:
                point_p = point_list[i]
                point_q = point_list[j]
                min_dist = distance
    point_pair_list.append(point_p)
    point_pair_list.append(point_q)
    return point_pair_list


# 生成器：生成横跨跨两个点集的候选点
def candidateDot(point_u, right, dis, med_x):
    # 遍历right（已按横坐标升序排序）。若横坐标小于med_x-dis则进入下一次循环；若横坐标大于med_x+dis则跳出循环；若点的纵坐标好是否落在在[u[1]-dis,u[1]+dis]，则返回这个点
    for point_v in right:
        if point_v.x < med_x - dis:
            continue
        if point_v.x > med_x + dis:
            break
        if point_v.y >= point_u.y - dis and point_v.y <= point_u.y + dis:
            yield point_v


# 求出横跨两个部分的点的最小距离
def combine(left, right, resMin, med_x):
    dis = resMin[1]
    minDis = resMin[1]
    pair = resMin[0]
    for point_u in left:
        if point_u.x < med_x - dis:
            continue
        for point_v in candidateDot(point_u, right, dis, med_x):
            dis = cal_distance(point_u, point_v)
            if dis < minDis:
                minDis = dis
                pair = [point_u, point_v]
    return [pair, minDis]


# 使用分支法方法
def divide_and_conquer(point_list):
    point_num = len(point_list)
    # 根据平面点的 x 坐标进行排序
    point_list = sorted(point_list, key=lambda point: point.x)
    if point_num <= 1:
        return None, float('inf')
    elif point_num == 2:
        return [point_list, cal_distance(point_list[0], point_list[1])]
    else:
        half = int(point_num / 2)
        # 记录中间值
        med_x = (point_list[half].x + point_list[-half - 1].x) / 2
        left = point_list[:half]
        resLeft = divide_and_conquer(left)
        right = point_list[half:]
        resRight = divide_and_conquer(right)

        # 获取两集合中距离最短的点对
        if resLeft[1] < resRight[1]:
            resMin = combine(left, right, resLeft, med_x)
        else:
            resMin = combine(left, right, resRight, med_x)
        pair = resMin[0]
        minDis = resMin[1]
    return [pair, minDis]


if __name__ == "__main__":
    point_list = generate_point_list(10000)

    start_time_violent = time.time()
    point_pair_use_violent = violent_solution(point_list)
    end_time_violent = time.time()

    start_time_divide = time.time()
    point_pair_use_divide = divide_and_conquer(point_list)[0]
    end_time_divide = time.time()
    print("暴力算法耗时:{}, 分治算法耗时:{}".format(end_time_violent - start_time_violent, end_time_divide - start_time_divide))
    if cal_distance(point_pair_use_violent[0], point_pair_use_violent[1]) == cal_distance(point_pair_use_divide[0],
                                                                                          point_pair_use_divide[1]):
        print("最短距离的pair为:{};{}. 最短距离为:{}, task complete!".format(point_pair_use_violent[0], point_pair_use_violent[1],
                                                                  cal_distance(point_pair_use_violent[0],
                                                                               point_pair_use_violent[1])))
