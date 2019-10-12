# coding:UTF-8
import time

timestamp = 1565573364

#转换成localtime
time_local = time.localtime(timestamp)
#转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print(dt)
# list = []
# for i in range(401, 429):
#     list.append(i)
# print(list)