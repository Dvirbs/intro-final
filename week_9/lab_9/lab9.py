class Student:
    def __init__(self, name: str, grades_list: list):
        self.__name = name
        self.__grades_list = grades_list
        self.__average_grade = sum(self.__grades_list) / len(self.__grades_list)

    def get_grade_avg(self):
        return self.__average_grade

    def get_name(self):
        return self.__name


class ClassRoom:
    def __init__(self, student_type: list):
        self.__student_type = student_type

    def __str__(self):
        result = "["
        for i, student in enumerate(self.__student_type):
            if i < len(self.__student_type)-1:
                result += "(" + "'{}'".format(student.get_name()) + ", " + str(student.get_grade_avg()) + "), "
            else:
                result += "(" + "'{}'".format(student.get_name()) + ", " + str(student.get_grade_avg()) + ")"

        result += "]"
        return result


yossi = Student("Yossi", [100, 90, 95])
amer = Student("Amer", [100, 90, 95])
lst = [yossi, amer]

yossi.get_grade_avg()
class_room = ClassRoom(lst)
print(class_room)
