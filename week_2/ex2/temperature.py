#################################################################
# FILE : temperature.py
# WRITER : Dvir , Dvirbs , 204270243
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A function that receives a certain threshold value
# and temperature measurements of three days and returns if in two out of
# the three days the temperature was really high above the threshold.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED:
# NOTES:
#################################################################
def is_vormir_safe(temp, day1, day2, day3):
    """A function that receives a certain threshold value
       and temperature measurements of three days and and check
       if in two out of the three days the temperature was really high above the threshold.
    :param temp: threshold value
    :param day1: temperature measurements day 1
    :param day2: temperature measurements day 2
    :param day3: temperature measurements day 3
    :return: True if it was high above the threshold and False if is not
    """
    if temp < day1 and (temp < day2 or temp < day3):
        return True
    elif temp < day2 and (temp < day1 or temp < day3):
        return True
    elif temp < day3 and (temp < day2 or temp < day1):
        return True
    return False






