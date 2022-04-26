import matplotlib.pyplot as plt
import numpy as np
import timeit
from ex7 import *
import sys


def top10(arr):
    return np.average(arr[len(arr) * 9 // 10:])


def time_code(func_name: str, func_param: str, N: int, ROUNDS: int = 8):
    """
    :param func_name: 'log_mult'
    :param func_param: '(987, %d)'
    :param N: 5000
    """
    time_series = []
    for n in range(1, N):
        time_series.append(timeit.timeit(func_name + func_param % n,
                                         "from __main__ import %s" % func_name,
                                         number=ROUNDS))
    return np.array(time_series)


def plot_complexity(func_name: str, func_param: str, N: int, ROUNDS: int = 8,
                    SMOOTH: bool = True, EXP: bool = False,
                    recursion_limit: int = 10000) -> None:
    """
    examples for parameters:
    :param func_name: 'log_mult'
    :param func_param: '(987, %d)'
    :param N: 5000
    """
    base_recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(recursion_limit)
    KERNEL = N // 50 + 1

    o_1 = np.ones(N)
    o_log_n = np.log(np.arange(N))
    o_n = np.arange(N)
    o_n_log_n = o_n * o_log_n
    o_n_2 = o_n * o_n
    time_complexity = {'O(1)': o_1, 'O(log n)': o_log_n, 'O(n)': o_n,
                       'O(n log n)': o_n_log_n, 'O(n^2)': o_n_2}
    time_series = time_code(func_name, func_param, N, ROUNDS)
    limit = top10(time_series)
    if SMOOTH:
        plt.plot(np.convolve(time_series / limit, np.ones(KERNEL) / KERNEL,
                             mode='valid'))
    else:
        plt.plot(time_series / limit)
    lg = ['code']
    for key in time_complexity.keys():
        ratio = top10(time_complexity[key])
        plt.plot(time_complexity[key] / ratio)
        lg.append(key)
    if EXP:
        o_2_n = np.exp2(o_n)
        ratio = o_2_n[-1]
        plt.plot(o_2_n / ratio)
        lg.append('O(2^n)')

    plt.title(func_name + func_param)
    plt.xlabel('n')
    plt.ylabel('sec/%f' % limit)
    plt.legend(lg)
    plt.show()

    sys.setrecursionlimit(base_recursion_limit)


if __name__ == '__main__':
    print("example:\n\n"
          "log_mult (987,%d) 1000\n"
          "this call will time the function log_mult(987, n)\n"
          "with 0 < n < 1000\n\n"
          "*the timer fluctuates, so you should not trust the outcome\n"
          "especially if there are major jumps*")
    while True:
        user_input = input('Enter new call: ')
        if user_input == 'exit':
            break
        params = user_input.split(' ')
        plot_complexity(params[0], params[1], int(params[2]))
