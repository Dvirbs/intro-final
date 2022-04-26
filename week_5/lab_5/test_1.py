import code_1
import unittest


def test_fizzBuzz_1():
    assert code_1.fizzBuzz_1(5) == 'Buzz'
    assert code_1.fizzBuzz_1(3) == 'Fizz'
    assert code_1.fizzBuzz_1(0) == 'FizzBuzz'
    assert code_1.fizzBuzz_1(15) == 'FizzBuzz'
    assert code_1.fizzBuzz_1(-5) == 'Buzz'
    assert code_1.fizzBuzz_1(-3) == 'Fizz'
    assert code_1.fizzBuzz_1(4) == 4


def main():
    test_fizzBuzz_1()


if __name__ == '__main__':
    main()

