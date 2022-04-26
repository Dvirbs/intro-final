import typing
from ex7_helper import *


def mult(x: float, y: int) -> float:
    """
    The result of the calculation of x is double y
    :return the results
    """
    if y == 1:
        return x
    if y == -1:
        return -x
    elif y < 0:
        return add(-x, mult(x, int(add(y, 1))))
    else:
        return add(x, mult(x, subtract_1(y)))


def is_even(n: int) -> bool:
    """
    returns True if n is an even number, and False another
    """
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 0:
        return True
    return is_even(subtract_1(subtract_1(n)))


def log_mult(x: float, y: int) -> float:
    """
    The result of the calculation of x is double y
    """
    if y == 0:
        return 0
    elif y == 2:
        return add(x, x)
    elif y == -2:
        return add(-x, -x)
    elif y == 1:
        return x
    elif y == -1:
        return -x

    elif is_odd(y):
        num = log_mult(x, divide_by_2(subtract_1(y)))
        return x + add(num, num)
    else:
        num = log_mult(x, divide_by_2(y))
        return add(num, num)


def is_power(b: int, x: int) -> bool:
    """
    Checking is there a non-negative integer n so that b to the power of n is equal to x.
    The function returns True if it exists, and False otherwise.
    """

    if x == 0:
        return False
    elif x == 1:
        return True
    if b == 0 and x == 0:
        return True
    elif b == 0 and x != 0:
        return False
    if b == 1 and x == 1:
        return True
    elif b == 1 and x != 1:
        return False
    return _power_helper(b, x, 0)


def _calculate_power(b: int, n: int) -> int:
    """
    calculate the power of b^n
    """
    if n == 0:
        return 1
    return int(log_mult(b, _calculate_power(b, n - 1)))


def _power_helper(b: int, x: int, n: int = 0) -> bool:
    if _calculate_power(b, n) == x:
        return True
    if _calculate_power(b, n) > x:
        return False
    return _power_helper(b, x, n + 1)


def reverse(s: str) -> str:
    """
    receives a string and returns the string containing the same characters ,but in reverse order.
    """
    return _reverse_helper(s, str(), len(s))


def _reverse_helper(s: str, rivers_str: str, n: int) -> str:
    """
    helpung reverse function to reverse the string s
    :param s: a string to reverse the latter's
    :param rivers_str: a empty string in the beginning is empty and full filling the rivers letters
    :param n: the len of stirng s
    :return: reverse string
    """
    if n == 0:
        return rivers_str
    rivers_str = append_to_end(rivers_str, s[n - 1])
    return _reverse_helper(s, rivers_str, n - 1)


# in the last function i use - and not substract function!!! need to check if i can

# function 7
def number_of_ones(n: int) -> int:
    count = 0
    return _number_of_ones_helper(n, count)


def _number_of_ones_helper(n: int, count: int) -> int:
    count += _number_of_ones_for_single_number(n)
    if n == 0:
        return count
    return _number_of_ones_helper(n - 1, count)


def _number_of_ones_for_single_number(n: int) -> int:
    """

    :param n:
    :return:
    """
    count = 0
    return _check_the_leftovers(n, count)


def _check_the_last_digit(n: int, count: int) -> int:
    """
    check if the last digit is one and update the count parameter
    :return: an update count parameter
    """
    if n % 10 == 1:
        count += 1
    return count


def _check_the_leftovers(n: int, count: int) -> int:
    if n == 0:
        return count
    elif n != 0:
        count = _check_the_last_digit(n, count)
    return _check_the_leftovers(n // 10, count)


def play_hanoi(hanoi: typing.Any, n: int, src: typing.Any, dst: typing.Any, temp: typing.Any) -> None:
    if n <= 0:
        return
    play_hanoi(hanoi, n - 1, src, temp, dst)
    hanoi.move(src, dst)
    play_hanoi(hanoi, n - 1, temp, dst, src)


def magic_list(n: int) -> list[typing.Any]:
    result: typing.List[typing.Any] = list()
    return _magic_list_helper(n, [], result)


def _magic_list_helper(n: int, lst: typing.List[typing.Any], result: typing.List[typing.Any]) -> typing.List[
    typing.Any]:
    if n == 0:
        return result
    result.append(lst)
    return _magic_list_helper(n - 1, result[:], result)


def compare_2d_lists(l1: typing.List[typing.List[int]], l2: typing.List[typing.List[int]]) -> bool:
    if len(l1) != len(l2) or not _1d_lists_same_len(l1, l2):
        return False
    if not compare_2d_lists_helper(l1, l2):
        return False
    return True


def compare_2d_lists_helper(l1: typing.List[typing.List[int]], l2: typing.List[typing.List[int]]) -> bool:
    if len(l1) == 0:
        return True
    if not _same_arguments_1d_lists(l1[-1], l2[-1]):
        return False
    return compare_2d_lists_helper(l1[:-1], l2[:-1])


def _same_arguments_1d_lists(lst1: typing.List[typing.Any], lst2: typing.List[typing.Any]) -> bool:
    if len(lst1) == 0:
        return True
    if lst1[-1] != lst2[-1]:
        return False
    return _same_arguments_1d_lists(lst1[:-1], lst2[:-1])


def _1d_lists_same_len(l1: typing.List[typing.Any], l2: typing.List[typing.Any]) -> bool:
    if len(l1) == 0:
        return True
    if len(l1[-1]) != len(l2[-1]):
        return False
    return _1d_lists_same_len(l1[:-1], l2[:-1])


if __name__ == '__main__':
    pass
