# coding=utf-8

import pymysql
import matplotlib.pyplot as plt
import time
import numpy as np

# Host ：166.111.7.145
# 	•	Username： root
# 	•	Password：Ise_Nel_2017
# 	•	Port：33306
# 	•	Database：IKR
if __name__ == "__main__":
    conn = pymysql.connect(host='166.111.7.145', port=33306, user='root', passwd='Ise_Nel_2017', db='dev_merge')
    cur = conn.cursor()
    cur.execute(
        "(select id,costTime from dev_merge.insertTestWithDefaultPath_IoTDB_merge2_true1563370838767 where id%3000=0)")
    # cur.execute(
    #     "(select id,costTime from zc_test_2019_6_12.insertTestWithDefaultPath_IoTDB_53_pipeline1562126338251 where id%1000=0) UNION (select id,costTime from zc_test_2019_6_12.insertTestWithDefaultPath_IoTDB_58_insert_test1562642019201 where id%1000=0)")
    results = cur.fetchall()
    times = []
    value = []
    print("查询结果集成功")
    for row in results:
        # time.append(row[0])
        timeArray = time.localtime(row[0] / 1000)
        dateTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        times.append(dateTime)
        value.append(row[1] * 1000)
    print("处理数据成功,开始绘图")
    plt.xlabel("time")
    # xlabels = range(min(times), max(times), 100000)
    # plt.xticks(range(50, 100000, 6000))
    plt.ylabel("avg latency")
    plt.ylim(0, max(value) + 100)
    # print(min(times))
    plt.hlines(np.mean(value), -10000, 100000, colors='black')
    print(np.mean(value))
    plt.title("Latest Ingestion Operation TTLB in ms changing with Time More Detail for merge=false")
    plt.plot(times, value)
    plt.show()
