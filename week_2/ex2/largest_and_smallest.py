#################################################################
# FILE : largest_and_smallest.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: help ironman and friends to calculate the max and min of three numbers
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################
# I decided to choose (1, 1, 1) because it need to check what happen if all the numbers are the same.
# I decided to choose (1, 0, -1) because it need to check postive, nagtive and zero value.

def check_if_first_is_the_mini(num1, num2, num3):
    """
    Find if the first parmeter of the function, num1, is the minimum
    :param num1: the first number
    :param num2: the second number
    :param num3: the third number
    :return: True
    """
    if num1 <= num2 and num1 <= num3:
        return True
    else:
        return False


def maxi(number1, number2):
    """
    returns the maximum between two numbers
    :param number1: the first number
    :param number2: the second number
    :return: the maximum of the two numbers
    """
    if number2 < number1:
        return number1
    else:
        return number2


def largest_and_smallest(num1, num2, num3):
    """
    The function check which is the larget and the smallest number out of three
    :param num1: the first number
    :param num2: the second number
    :param num3: the third number
    :return: the largest number and the smallest number
    """
    if check_if_first_is_the_mini(num1, num2, num3):
        return maxi(num2, num3), num1
    elif check_if_first_is_the_mini(num2, num3, num1):
        return maxi(num1, num3), num2
    else:
        return maxi(num1,num2), num3


def check_largest_and_smallest():
    """
    this function check if the function largest_and_smallest works well with 5 diffrents states
    :return: True if it working and False if not
    """
    if not (17, 1) == largest_and_smallest(17, 1, 6):
        return False
    if not (17, 1) == largest_and_smallest(1, 17, 6):
        return False
    if not (2, 1) == largest_and_smallest(1, 1, 2):
        return False
    if not (1, 1) == largest_and_smallest(1, 1, 1):
        return False
    if not (1, -1) == largest_and_smallest(-1, 0, 1):
        return False
    return True




