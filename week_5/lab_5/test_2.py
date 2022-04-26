import code_2
import test_1
import unittest




def test_fizzBuzz_2():
    assert code_2.fizzBuzz_2(5) == 'Buzz'
    assert code_2.fizzBuzz_2(3) == 'Fizz'
    assert code_2.fizzBuzz_2(0) == 'FizzBuzz'
    assert code_2.fizzBuzz_2(15) == 'FizzBuzz'
    assert code_2.fizzBuzz_2(-5) == 'Buzz'
    assert code_2.fizzBuzz_2(-3) == 'Fizz'
    assert code_2.fizzBuzz_2(4) == 4
    assert code_2.fizzBuzz_2(23) == 'Fizz'
    assert code_2.fizzBuzz_2(51) == 'Buzz'
    assert code_2.fizzBuzz_2(31) == 'Fizz'
    assert code_2.fizzBuzz_2(-51) == 'Buzz'
    assert code_2.fizzBuzz_2(-31) == 'Fizz'
    assert code_2.fizzBuzz_2(26) == 26



def main():
    test_fizzBuzz_2()


if __name__ == '__main__':
    main()