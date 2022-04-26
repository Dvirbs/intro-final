#################################################################
# FILE : ex3.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex3 2020
# DESCRIPTION: ex that related to lists and vectors actions
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:בהתחלה שכתבתי את פונקציה 4 שמייצרת סדרות לפי הקלטים השתמשתי ביבוא של הספריה הרנדומלית
#       על מנת ליצור סדרות אקראיות, ומכיוון שלמדנו את זה בשיעור.
#       הבנתי רק בסוף שאסור לייבא ספריות ולא רציתי שירדו לי נקודות על זה אז השחרתי את הפונקציות שיוצרות
#       באקראיות את הסדרות וכתבתי פונקציות שיוצרות סדרות קבועות
#       לא רציתי למחוק כי עבדתי קשה על בניית הפונקציות שיוצרות סדרות באקראיות ולכן הם בקובץ פשוט הו משוחרות
#################################################################


def input_list():
    """
    receives numbers from the user until she get empty string.
    :return a list in which all the inputs entered by the user And at the end their sum.
    """
    list_of_num = []
    while True:
        num = input()
        if num != '':
            list_of_num.append(float(num))
        else:
            break
    sum_num = 0
    for i in range(len(list_of_num)):
        sum_num += list_of_num[i]
    list_of_num.append(sum_num)
    return list_of_num


def inner_product(vec_1, vec_2):
    """
    receives two vectors
    :param vec_1: vector 1
    :param vec_2: vector 2
    :return: inner product of the two vectors
    """
    if len(vec_1) != len(vec_2):
        return
    if not len(vec_1):
        return 0
    the_product = 0
    for i in range(len(vec_1)):
        the_product += vec_1[i]*vec_2[i]
    return the_product


def strictly_increasing(sequence):
    """
    checking if the sequence is strictly increasing
    :param sequence: sequence of numbers to check
    :return: True and False in accordance to the sequence
    """
    for i in range(len(sequence)-1):
        if sequence[i+1]-sequence[i] <= 0:
            return False
    return True


def non_decreasing(sequence):
    """
    checking if the sequence is  non decreasing
    :param sequence: sequence of numbers to check
    :return: True and False in accordance to the sequence
    """
    for i in range(len(sequence)-1):
        if sequence[i+1]-sequence[i] < 0:
            return False
    return True


def strictly_decreasing(sequence):
    """
    checking if the sequence is strictly decreasing
    :param sequence: sequence of numbers to check
    :return: True and False in accordance to the sequence
    """
    for i in range(len(sequence)-1):
        if 0 <= sequence[i+1]-sequence[i]:
            return False
    return True


def non_increasing(sequence):
    """
    checking if the sequence is non increasing
    :param sequence: sequence of numbers to check
    :return: True and False in accordance to the sequence
    """
    for i in range(len(sequence)-1):
        if 0 < sequence[i+1]-sequence[i]:
            return False
    return True


def sequence_monotonicity(sequence):
    """
    the function check for monotonic of a final series
    :param sequence: sequence of numbers to check
    :return: List with 4 Boolean organs: True and False in accordance to the sequence
     The 0th place in the list refers to non decreasing, the 1st place to strictly increasing,
     the 2st non increasing,the 3st strictly_decreasing.
    """
    if sequence == [] or len(sequence) == 1:
        return [True, True, True, True]
    return ([non_decreasing(sequence), strictly_increasing(sequence),
            non_increasing(sequence), strictly_decreasing(sequence)])


# def seq_non_decreasing():
#     """
#     A function that making non decreasing sequence
#     :return: 4-digit list representing a non decreasing series
#     """
#     first_num = round(random.uniform(-100, 100), 1)
#     sec_num = round(random.uniform(first_num, 100), 1)
#     third_num = round(random.uniform(sec_num, 100), 1)
#     four_num = round(random.uniform(third_num, 100), 1)
#     return [first_num, sec_num, third_num, four_num]


def seq_non_decreasing():
    """
    A function that making non decreasing sequence
    :return: 4-digit list representing a non decreasing series
    """
    first_num = 5
    sec_num = 21
    third_num = 21
    four_num = 39
    return [first_num, sec_num, third_num, four_num]


# def seq_strictly_increasing():
#     """
#     A function that making strictly increasing sequence
#     :return: 4-digit list representing a strictly increasing series
#     """
#     first_num = round(random.uniform(-100, 100), 1)
#     while 99.7 < first_num:
#         first_num = round(random.uniform(-100, 100), 1)
#     sec_num = round(random.uniform(first_num+0.1, 100), 1)
#     while 99.8 < sec_num:
#         sec_num = round(random.uniform(first_num + 0.1, 100), 1)
#     third_num = round(random.uniform(sec_num+0.1, 100), 1)
#     while 99.9 < third_num:
#         third_num = round(random.uniform(sec_num + 0.1, 100), 1)
#     four_num = round(random.uniform(third_num+0.1, 100), 1)
#     return [first_num, sec_num, third_num, four_num]


def seq_strictly_increasing():
    """
    A function that making strictly increasing sequence
    :return: 4-digit list representing a strictly increasing series
    """
    first_num = 5
    sec_num = 10
    third_num = 21
    four_num = 39
    return [first_num, sec_num, third_num, four_num]


# def seq_strictly_decreasing():
#     """
#     A function that making strictly decreasing sequence
#     :return: 4-digit list representing a strictly decreasing series
#     """
#     first_num = round(random.uniform(-100, 100), 1)
#     while first_num < -99.7:
#         first_num = round(random.uniform(-100, 100), 1)
#     sec_num = round(random.uniform(-100, first_num-0.1), 1)
#     while sec_num < -99.8:
#         sec_num = round(random.uniform(-100, first_num-0.1), 1)
#     third_num = round(random.uniform(-100, sec_num-0.1), 1)
#     while third_num < -99.9:
#         third_num = round(random.uniform(-100, sec_num-0.1), 1)
#     four_num = round(random.uniform(-100, third_num-0.1), 1)
#     return [first_num, sec_num, third_num, four_num]


def seq_strictly_decreasing():
    """
    A function that making strictly decreasing sequence
    :return: 4-digit list representing a strictly decreasing series
    """
    first_num = 50
    sec_num = 39
    third_num = 21
    four_num = 1
    return [first_num, sec_num, third_num, four_num]


# def seq_non_increasing():
#     """
#     A function that making non increasing sequence
#     :return: 4-digit list representing a non increasing series
#     """
#     first_num = round(random.uniform(-100, 100), 1)
#     sec_num = round(random.uniform(-100, first_num), 1)
#     third_num = round(random.uniform(-100, sec_num), 1)
#     four_num = round(random.uniform(-100, third_num), 1)
#     return [first_num, sec_num, third_num, four_num]


def seq_non_increasing():
    """
    A function that making non increasing sequence
    :return: 4-digit list representing a non increasing series
    """
    first_num = 50
    sec_num = 21
    third_num = 21
    four_num = 10
    return [first_num, sec_num, third_num, four_num]


def seq_non_increasing_and_decreasing():
    """
       A function that making non increasing and non decreasing sequence
       :return: 4-digit list representing a non increasing and non decreasing series
       """
    return [21, 21, 21, 21]


def monotonicity_inverse(def_bool):
    """
    A function that receives a list of 4 Boolean organs and returns a list of four difference type of
     of final series(non increasing, strictly increasing, non decreasing, strictly decreasing)
    :param def_bool: list of 4 Boolean organs
    :return: A 4-number list that represents a final series respectively to the choose of the Boolean in the
             parameter def_bool (non increasing, strictly increasing, non decreasing, strictly decreasing)
    """
    if def_bool == [True, False, False, False]:
        return seq_non_decreasing()
    elif def_bool == [True, True, False, False]:
        return seq_strictly_increasing()
    elif def_bool == [True, False, True, False]:
        return seq_non_increasing_and_decreasing()
    elif def_bool == [False, False, True, False]:
        return seq_non_increasing()
    elif def_bool == [False, False, True, True]:
        return seq_strictly_decreasing()
    elif def_bool == [False, False, False, False]:
        return [0, 1, 0, 1]
    else:
        return


def primes_for_asafi(n):
    """
    helping asafi find the primes number until n
    :param n: until this number that we find the primes.
    :return: list of primes until n for asafi
    """
    if n == 0:
        return []
    list_of_primes = [2]
    optional_num = 3

    while len(list_of_primes) < n:
        modulo = True
        for prime in list_of_primes:
            if optional_num % prime == 0:
                optional_num += 1
                modulo = False
                break
        if modulo:
            it_is_a_prime = optional_num
            list_of_primes.append(it_is_a_prime)
            optional_num += 1
    return list_of_primes


def sum_of_vectors(vec_lst):
    """
    function that doing the sum operation in vector space
    :param vec_lst: list of vectors
    :return: vector that is the sum of the vectors
    """
    if not vec_lst:
        return
    elif not vec_lst[0]:
        return []

    the_sum_vec = []
    for i in range(len(vec_lst[0])):
        i_coordinate = 0
        for j in range(len(vec_lst)):
            i_coordinate += vec_lst[j][i]
        the_sum_vec.append(i_coordinate)
    return the_sum_vec


def num_of_orthogonal(vectors):
    """
    function that checked for orthogonal vectors in list of vectors
    :param vectors: the list of the vector
    :return: the sum of the orthogonal vectors
    """
    list_vec_to_change = vectors[:][:]
    the_sum = 0
    for vec_1 in list_vec_to_change:
        for vec_2 in list_vec_to_change:
            if vec_2 == vec_1:
                continue
            if not inner_product(vec_1, vec_2):
                the_sum += 1
        del list_vec_to_change[0]
    return the_sum
