from ex7 import *


def test_mult():
    assert mult(5, 4) == 20
    assert mult(5, -4) == -20
    assert mult(-5, 4) == -20
    assert mult(-5, 0) == 0
    assert mult(5, 0) == 0
    assert mult(5.5, 2) == 11


def test_is_even():
    assert is_even(1) is False
    assert is_even(2) is True
    assert is_even(9) is False
    assert is_even(99) is False
    assert is_even(0) is True


def test_log_mult():
    assert log_mult(3, 4) == 12
    assert log_mult(3, -4) == -12
    assert log_mult(3, 0) == 0
    assert log_mult(3, 1) == 3
    assert log_mult(3, -1) == -3
    assert log_mult(3, 5) == 15
    assert log_mult(3, -5) == -15
    assert log_mult(4, -5) == -20
    assert log_mult(4, 5) == 20


def test_is_power():
    assert is_power(0, 5) is False
    assert is_power(0, 0) is False
    assert is_power(1, 1) is True
    assert is_power(3, 9) is True
    assert is_power(3, 27) is True
    assert is_power(5, 125) is True
    assert is_power(2, 64) is True
    assert is_power(2, 64) is True



def test_reverse():
    assert reverse('dvir ben simhon') == 'nohmis neb rivd'
    assert reverse('') == ''
    assert reverse('a') == 'a'


def test_number_of_ones():
    assert number_of_ones(10) == 2
    assert number_of_ones(11) == 4
    assert number_of_ones(12) == 5
    assert number_of_ones(13) == 6
    assert number_of_ones(14) == 7
    assert number_of_ones(15) == 8
    assert number_of_ones(16) == 9
    assert number_of_ones(17) == 10
    assert number_of_ones(18) == 11
    assert number_of_ones(19) == 12
    assert number_of_ones(20) == 12
    assert number_of_ones(21) == 13


def test_magic_list():
    assert magic_list(0) == []
    assert magic_list(1) == [[]]
    assert magic_list(2) == [[], [[]]]
    assert magic_list(3) == [[], [[]], [[], [[]]]]
    assert magic_list(4) == [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]


if __name__ == '__main__':
    test_mult()
    test_is_even()
    test_log_mult()
    test_is_power()
    test_reverse()
    test_number_of_ones()
    test_magic_list()
