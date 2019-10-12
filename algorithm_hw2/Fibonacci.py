# coding=utf-8
import time

import numpy as np


# 使用递归方法求Fibonacci数
def recursion_Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return recursion_Fibonacci(n - 1) + recursion_Fibonacci(n - 2)


# 使用动态规划的方式求Fibonacci数,算法复杂度为O(n)
def dynamic_Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    Fibonacci_list = []
    Fibonacci_list.append(0)
    Fibonacci_list.append(1)
    for i in range(2, n + 1):
        tmp = Fibonacci_list[-1] + Fibonacci_list[-2]
        Fibonacci_list.append(tmp)
    return Fibonacci_list[n]


# 求矩阵的n次方
def matrix_power_n(n):
    if n == 1:
        return np.array([[1, 1], [1, 0]])
    if n % 2 == 1:
        return np.dot(matrix_power_n(1), matrix_power_n(n - 1))
    else:
        return np.dot(matrix_power_n(n / 2), matrix_power_n(n / 2))


# 使用分治法求Fibonacci数,算法复杂度为O(lg n)
def divide_and_conquer(n):
    return int(matrix_power_n(n - 1)[0][0])


if __name__ == "__main__":
    # 指定Fibonacci数的n值
    n = 1000000

    start_time_recursion = time.time()
    # Fibonacci_use_recursion = recursion_Fibonacci(n)
    end_time_recursion = time.time()

    start_time_dynamic = time.time()
    # Fibonacci_use_dynamic = dynamic_Fibonacci(n)
    end_time_dynamic = time.time()

    start_time_divide = time.time()
    Fibonacci_use_divide = divide_and_conquer(n)
    end_time_divide = time.time()
    print("递归算法耗时:{}, 动态规划算法耗时:{}, 分治法耗时:{}, task complete!".format(round(end_time_recursion - start_time_recursion, 10),
                                                                    round(end_time_dynamic - start_time_dynamic, 10),
                                                                    round(end_time_divide - start_time_divide, 10)))
