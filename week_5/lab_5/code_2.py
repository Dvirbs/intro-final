def fizzBuzz_2(num: int):
    num_string = str(num)
    if (num % 5 == 0 and num % 3) or ('3' in num_string and '5' in num_string):
        return 'FizzBuzz'
    if num % 3 == 0 or '3' in num_string:
        return 'Fizz'
    if num % 5 == 0 or '5' in num_string:
        return 'Buzz'
    return num