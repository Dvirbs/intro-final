def fizzBuzz_3(num: int):
    # num_string = str(num)
    # if num % 3 == 0 and '3' in num_string:
    #     return num
    # if (num % 3 == 0 and '3' not in num_string) or (num % 3 != 0 and '3' in num_string):
    #     return 'Fizz'
    # if num % 5 == 0 and '5' in num_string:
    #     return num
    # if (num % 5 == 0 and '5' not in num_string) or (num % 5 != 0 and '5' in num_string):
    #     return 'Buzz'
    #
    # if (num % 5 == 0 and num % 3) or ('3' in num_string and '5' in num_string):
    #     return 'FizzBuzz'
    # if num % 5 == 0 and num % 3 and '3' in num_string and '5' in num_string:
    #     return 'FizzBuzz'
    # if (num % 5 == 0 and '3' in num_string) or (num % 3 and '5' in num_string):
    #     return 'FizzBuzz'
    # if (num % 5 == 0 and '5' in num_string) or ('3' in num_string and num % 3):
    #     return 'FizzBuzz'
    # if ('3' in num_string and num % 3) or (num % 5 == 0 and '5' in num_string):
    #     return 'FizzBuzz'
    # if ('5' in num_string and num % 3) or ('3' in num_string and num % 5 == 0):
    #     return 'FizzBuzz'
    #
    # if num % 5 == 0 and num % 3 and '3' in num_string and '5' not in num_string:
    #     return num
    # if num % 5 == 0 and num % 3 and '5' not in num_string and '3' not in num_string:
    #     return num
    # if (num % 5 == 0 and '3' in num_string and '5' not in num_string) and num % 3 == 0:
    #     return num
    # if '3' in num_string and num % 3 == 0 and '5' not in num_string and num % 5 == 0:
    #     return num
    # return num
    num_string = str(num)
    count3 = 0
    count5 = 0

    if num % 3 == 0:
        count3 += 1
    if '3' in num_string:
        count3 += 1
    if num % 5 == 0:
        count5 += 1
    if '5' in num_string:
        count5 += 1

    if count5 != 0 and count3 != 0:
        if (count3 + count5) % 2 == 1:
            return 'FizzBuzz'
        if (count3 + count5) % 2 == 0:
            return 'FizzBuzz'
    if count5 % 2 == 0:
        if count3 % 2 == 1:
            return 'Fizz'
        if count3 % 2 == 0:
            return num
    if count3 % 2 != 0:
        if count5 % 2 == 1:
            return 'Buzz'
        if count5 % 2 == 0:
            return num

    if count3 % 2 == 1:
        return 'Fizz'
    if count3 % 2 == 0:
        return num
    if count5 % 2 == 1:
        return 'Buzz'
    if count5 % 2 == 0:
        return num
