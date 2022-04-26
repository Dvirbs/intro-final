from ex7_helper import *
from typing import *
import hanoi_game


def mult(x: float, y: int) -> float:
    if y == 0:
        return 0
    if y == 1:
        return x
    return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    if n == 0:
        return True
    elif n == 1:
        return False
    return is_even(subtract_1(subtract_1(n)))


def log_mult(x: float, y: int):
    if y == 0:
        return 0
    if y == 1:
        return x
    elif is_odd(y):
        mid = divide_by_2(y)
        return add(add(log_mult(x, mid), log_mult(x, mid)), x)
    else:
        mid = divide_by_2(y)
        return add(log_mult(x, mid), log_mult(x, mid))


def is_power(b: int, x: int):
    pass


def is_power_helper(b: int, x: int, res=0):
    if x < res:
        return False
    return is_power_helper(b, x, int(log_mult(b, int(n))))


def reverse(s: str) -> str:
    return reverse_helper(s, "")


def reverse_helper(s: str, new_s) -> str:
    if len(s) == 1:
        return append_to_end(new_s, s[-1])
    return reverse_helper(s[:-1], append_to_end(new_s, s[-1]))


def number_of_ones_helper(n: int, counter: int = 0) -> int:
    if n % 10 == 1:
        counter += 1
    if (n // 10) % 10 == 1:
        counter += 1
    if (n // 100) % 10 == 1:
        counter += 1
    elif n == 0:
        return counter
    return number_of_ones_helper(n - 1, counter)


def ones_diffrent_pos(n, tenth, counter):
    if n // 10 == 0:
        return counter
    elif (n // 10) % 10 == 1:
        counter += 1
    return ones_diffrent_pos(n // 10, tenth, counter)


def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any):
    if n == 0:
        return
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n-1 , temp, dest, src)



"let go the stress about thing that will pass soon"
