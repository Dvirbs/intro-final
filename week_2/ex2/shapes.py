#################################################################
# FILE : shapes.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: function Asks the user to select the form to calculate its area
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################
import math


def check_if_we_got_123(shape):
    """
    "The function check if the parameter shape is 1,2 or 3 and return True if does"
    :param shape: number to peak
    :return: True if the number 1, 2, 3 and False if isnt.
    """

    if shape == 1 or shape == 2 or shape == 3:
        return True
    return


def circ_area(radius):
    """
    "Calculating the area of circle"
    :param radius: radius
    :return: area of circle
    """
    return math.pi * math.pow(radius, 2)


def rect_area(edge1, edge2):
    """
    "Calculating the area of rectangle"
    :return: area of rectangle
    """
    return edge1 * edge2


def triangle_area(edge):
    """
    "Calculating the area triangle"
    :return: area triangle
    """
    return (math.sqrt(3)/4)*math.pow(edge, 2)


def shape_area():
    """
    function Asks the user to select the form to calculate its area,
    and then asks him for the appropriate inputs for the needs of the
    Calculating the area
    :return: eturns the area of the desired shape according to the data
    """
    shape = float(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))

    if not check_if_we_got_123(shape):
        return
    elif shape == 1:
        radius = float(input())
        return circ_area(radius)
    elif shape == 2:
        edge1 = float(input())
        edge2 = float(input())
        return rect_area(edge1, edge2)
    else:
        edge = float(input())
        return triangle_area(edge)











