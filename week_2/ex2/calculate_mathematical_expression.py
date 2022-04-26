#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: help ironman and friends to calculate
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################
def calculate_mathematical_expression(num1, num2, string):
    """
    A function that calculates mathematical expression between two numbers and an action that separates them.
    :param num1: the first number
    :param num2: the second number
    :param string: string that is one of elementary arithmetic
    :return: the solution of the calculation
    """
    if string != "+" and string != "-" and string != "+" and string != ":" and string != "*":
        return
    else:
        if string == "+":
            return num1+num2
        elif string == "-":
            return num1-num2
        elif string == "*":
            return num1*num2
        elif string == ":":
            if num2 == 0:
                return
            else:
                return num1/num2


def calculate_from_string(string):
    """
    A function that get a mathematical exercise as a string and returns its solution
    :param string: string of two numbers and elementary_arithmetic action
    :return: the solution of the calculation
    """
    num1, elementary_arithmetic, num2 = string.split(" ")
    return calculate_mathematical_expression(float(num1), float(num2), elementary_arithmetic)



