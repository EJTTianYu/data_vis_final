# coding=utf-8

from tkinter import *
import random
import math
from algorithm_hw2.point import Point, divide_and_conquer, cal_distance


class ClosestPairs(object):

    def __init__(self, size=0, canvas_w=1200, canvas_h=700):
        self.size = size

        self.window = Tk()
        self.window.title("Find the Closest Pair of Points")

        # 设定frame和canvas的显示宽高
        self.frame_w = self.canvas_w = canvas_w
        self.frame_h = self.canvas_h = canvas_h

        # 圆点半径
        self.dot_radius = 2

        self.hbar_offset = 0
        self.vbar_offset = 0

        # 创建frame
        self.frame = Frame(self.window, width=self.frame_w, height=self.frame_h)
        self.frame.grid(row=0, column=0)

        # 创建canvas
        self.canvas = Canvas(self.frame,
                             width=self.canvas_w,
                             height=self.canvas_h,
                             background="white",
                             )

        # canvas绑定点击事件
        self.canvas.bind("<Button -1>", self.add_point)

        # canvas属性设置
        self.canvas.pack(expand=True, fill=BOTH)

        # 声明点列表
        self.point_list = []

    def show_window(self):
        for i in range(self.size):
            point_x = random.uniform(0, self.canvas_w)
            point_y = random.uniform(0, self.canvas_h)
            new_point = Point(point_x, point_y)
            # 判断点是否重复
            if new_point in self.point_list:
                continue
            self.point_list.append(new_point)
            self.canvas.create_oval(point_x - self.dot_radius, point_y - self.dot_radius,
                                    point_x + self.dot_radius, point_y + self.dot_radius, fill='red')
        self.window.mainloop()

    def add_point(self, event):
        point_x = self.hbar_offset + event.x
        point_y = self.vbar_offset + event.y
        new_point = Point(point_x, point_y)

        print("点击的坐标是(%d,%d)" % (point_x, point_y))
        # 判断点是否重复
        if new_point in self.point_list:
            print("您点击的点已经记录在界面上存在！")
            return
        self.size += 1
        self.canvas.create_oval(point_x - self.dot_radius, point_y - self.dot_radius,
                                point_x + self.dot_radius, point_y + self.dot_radius, fill='blue')
        self.point_list.append(new_point)
        if self.size == 1:
            print("当前平面上的总点数为1, 再次点击后开始最短点对计算")
            return
        point_pair_use_divide = divide_and_conquer(self.point_list)[0]
        print("分治算法得到点击加入点后的最短点对距离为：%f  最短点对的坐标是(%f,%f),(%f,%f)"
              % (cal_distance(point_pair_use_divide[0], point_pair_use_divide[1]), point_pair_use_divide[0].x,
                 point_pair_use_divide[0].y,
                 point_pair_use_divide[1].x, point_pair_use_divide[1].y))


if __name__ == '__main__':
    size = int(input("请输入点的数量："))
    cp = ClosestPairs(size=size)
    cp.show_window()
