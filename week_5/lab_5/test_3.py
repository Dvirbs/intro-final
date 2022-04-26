import code_3
import test_1
import test_2
import unittest


def test_fizzBuzz_3():
    assert code_3.fizzBuzz_3(3) == 3
    assert code_3.fizzBuzz_3(13) == 'Fizz'
    assert code_3.fizzBuzz_3(25) == 25
    assert code_3.fizzBuzz_3(4) == 4
    assert code_3.fizzBuzz_3(51) == 'FizzBuzz'
    assert code_3.fizzBuzz_3(0) == 'FizzBuzz'
    assert code_3.fizzBuzz_3(15) == 'FizzBuzz'


def main():
    test_fizzBuzz_3()


if __name__ == '__main__':
    main()








