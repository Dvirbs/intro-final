#################################################################
# FILE : quadratic_equation.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: function that calculate the solution for quadratic equation
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################
import math


def discriminant(a, b, c):
    """
    calculate the discriminant
    :return: the solution of the discriminant
    """
    return math.pow(b, 2) - 4 * a * c


def quadratic_equation(a, b, c):
    """
    calculate the solution for quadratic equation for all condition
    :param a: the leading coefficient of x^2 in quadratic equation
    :param b: the coefficient if x in quadratic equation
    :param c: the constant coefficient in quadratic equation
    :return: solution and None  if only one solution
             2 solution if there are 2.
             None if we dont get solution
    """
    dis = discriminant(a, b, c)
    if dis >= 0:
        sol1 = (-b + math.sqrt(dis)) / (2 * a)
        sol2 = (-b - math.sqrt(dis)) / (2 * a)
        if dis == 0:
            return sol1, None
        else:
            return sol1, sol2
    else:
        return None, None


def quadratic_equation_user_input():
    """
    ask the user for quadratic equations a, b and c and and solve it
    :return: prints the equation solutions to the screen
    """
    a, b, c = input("Insert coefficients a, b, and c: ").split()
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return
    sol1, sol2 = quadratic_equation(a, b, c)
    if sol1 and sol2:
        print("The equation has 2 solutions:", sol1, "and", sol2)
    elif sol1:
        print("The equation has 1 solution:", sol1)
    else:
        print("The equation has no solutions")


