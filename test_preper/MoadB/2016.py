######################2016A#############################


############Q1################
# def compress(lst):
#     if not lst:
#         return
#     new_lst = [(lst[0],1)]
#     new_index = 0
#     for item in lst[1:]:
#         last_item = new_lst[new_index][0]
#         item_count = new_lst[new_index][1]
#         if item == last_item:
#             new_lst[new_index] = (item, item_count + 1)
#         else:
#             new_index += 1
#             new_lst.append((item,1))
#     return new_lst
#
# print(compress(['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']))

#########################Q2####################
# def count_sums(a, s):
#     if s == 0:
#         return 1
#     if len(a) == 0 or s < 0:
#         return 0
#     else:
#         counter = 0
#         counter += count_sums(a[1:], s - a[0])
#         counter += count_sums(a[1:], s)
#     return counter
# print(count_sums([3,5,8,9,11,12,20], 20))
# print(count_sums([3,5], 8))


#########################Q3####################

# class Student:
#     All_Students = list()
#     def __init__(self, name):
#         self.name = name
#         self.grades = list()
#         All_Students.append(self)


#     def add_grade(new_grade):
#         self.__grades.append(new_grade)

#     def get_average():
#         if not self.__grades:
#             print('there is no grades')
#         else:
#             return sum(self.__grades)/ len(self.__grades)

# def get_student_by_name(name):
#     for student in Student.All_Students:
#         if student.name == name:
#             return student

#########################Q4####################


# def aggregate(f):
#     lst = list()
#     def inner(x):
#         lst.append(f(x))
#         return lst
#     return inner

# def f(x):
#     return x*2
# h = aggregate(f)
# print(h(7))
# print(h(5))
# print(h(7))


######################2016B#############################


############Q1################
# def split(string: str):
#     if string == '':
#         return ""
#     lst = ['']
#     i = 0
#     counter = 0
#     while i != len(string):
#         if string[i] != ' ':
#             lst[counter] += string[i]
#             i +=1
#         else:
#             i +=1
#             if lst[-1] != '':
#                 lst.append('')
#                 counter +=1
#     if lst[-1]== "":
#         del lst[-1]
#     return lst
# print(split("     abc   d  ef     ghi "))

############Q2################


#############????????????????###############

# def cartesian_product(lst):
#     return helper(lst, '', [])


# def helper(lst, cur, new_lst):
#     if not lst:
#         new_lst.append(cur)
#         return
#     for lst_i in lst:
#         for item in lst_i:
#             print('cur= ', cur)
#             print('item= ', item)
#             new_cur = cur + item
#             helper(lst[1:], new_cur, new_lst)

#     return new_lst

# print(cartesian_product([['a', 'b'], ['c', 'd', 'e']]))

#############????????????????###############


############Q3################


# class MultiDict:
#     dic = []
#     def __init__(self):
#         return
#     def add(self, key, val):
#         self.dic.append((key, val))
#     def has_val(self, key, val):
#         for tup in self.dic:
#             if tup[0] == key and tup[1] == val:
#                 return True
#         return False


# m = MultiDict()
# m.add("a", 1)
# print(m.has_val('a',1))
# print(m.has_val('a',12))