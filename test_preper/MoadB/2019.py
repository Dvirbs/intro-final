######################2019a1#############################


############Q1################
import copy
from typing import *
def make_closed(dict1: Dict):
    dic = copy.deepcopy(dict1)
    for key, value in dict1.items():
        if value in dic:
            continue
        else:
            dic.pop(key)
    return dic

############Q2################
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def weave(a, b):
    current_node = Node(a[0])
    starter = current_node
    a = a[1:]
    current_lst = b
    while a and b:
        prev = current_node
        cur = Node(current_lst[0])
        prev.next(cur)
        current_node = cur
        current_node.prev = prev
        b = b[1:]
        current_lst = a
    return starter


############Q3################


def has_x_peaks(lst, x):
    counter_lst = list()
    prev = None
    helper(lst, prev, counter_lst)
    print(counter_lst)

    return len(counter_lst) == x


def helper(lst, prev, counter):
    print(counter)
    if prev == None:
        if lst[0] > lst[1]:
            counter.append(lst[0])
        prev = lst[0]
        lst = lst[1:]
    if len(lst) == 1:
        if prev < lst[-1]:
            counter.append(lst[0])
        print(counter)
        return
    elif len(lst) > 1:
        if lst[0] >= prev and lst[0] >= lst[1]:
            counter.append(lst[0])
        helper(lst[1:], prev, counter)


#print(has_x_peaks([1, 3, 4, 4, 2, 8, 4, 9], 4))

############Q4################

def find_valley(lst):
    index_lst = []
    prev = None
    helper(lst, prev, index_lst)
    return len(index_lst)


def helper(lst, prev, index_lst):
    if not lst:
        return index_lst
    if prev and len(lst) > 1:
        if prev >= lst[0] and lst[0] <= lst[1]:
            return index_lst
    print(index_lst)
    index_lst.append([lst[0]])
    helper(lst[1:], lst[0], index_lst)


#print(find_valley([7, 5, 4, 3, 2, 7, 9, 10]))


############Q5################


def make_stack():
    stack = list()
    def inner(*arg):
        if arg:
            stack.append(arg)
            return
        else:
            return stack.pop()
    return inner

# s = make_stack()
# s(1)
# s(2)
# s(3)
#
# print(s())
# print(s(), s())



######################2019B#############################


############Q1################

def is_magic_square(mat):
    col_lst = zeros(len(mat[0]))
    ideal = sum(mat[0])
    for i, row in enumerate(mat):
        if sum(row) != ideal:
            print('it is here ')
            return False
        for j, pix in enumerate(row):
            print('col_lst= ', col_lst)
            print('ideal= ', ideal)
            col_lst[j] += pix
            if i == mat[-1]:
                if col_lst[j] != ideal:
                    print('no! it is here! ')

                    return False
    return True


def zeros(n):
    lst = []
    for i in range(n):
        lst.append(0)
    return lst
############################      O(n^2)         #######################

#print(is_magic_square([[1, 3], [1, 1]]))


############Q2################
class Node:
    def __init__(self, root, left= None, right = None):
        self.root, self.left, self.right = root, left, right

def scramble(root):
    leafs_for_me = []
    helper(root, 0, leafs_for_me, True)
    return leafs_for_me

def helper(root, counter, leafs, flag):
    if root.left == root.right == None:
        return root
    elif counter%2 == 0 and flag:
        flag = False
        if root.left == None:
            root.right == root.left
            root.right == None
        elif root.right == None:
            root.left == root.right
            root.left == None
        else:
            root.left, root.right = root.right, root.left
    leafs.append(helper(root.left, counter + 1, leafs, True))
    leafs.append(helper(root.right, counter + 1, leafs, True))
    return leafs


my_beutifull_tree = Node(Node(1),Node(2),Node(3))
#print(scramble(my_beutifull_tree))




############Q5################
class DropWhile:
    pass



##############Q6##############
class Shelf:
    def __iner__(self):
        self.things = dict()

    def place_item_on(self, item, thing):
        if thing == self:
            self.things[item] = [item]
        elif thing != self:
            if thing in self.things:
                self.things[item] = self.things.pop(thing) + [item]
        else:
            raise ValueError

    def remove(self, thing):
        if thing in self.things:
            prev = self.things[thing][-2]
            self.things[prev] = self.things.pop(thing)[:-1]
        else:
            raise ValueError

    def __str__(self):
        to_print = ""
        for value, key in self.things.items():
            lst = value[::-1]
            to_print += "a "
            while lst:
                to_print += str(lst[0])
                lst = lst[1:]




######################201b1#############################


#########################Q1########################
def describe_str(st1):
    seq = same_char_helper(str1, 0)
    if len(st1)-1 < seq:
        return str(st1[0]) + str(seq)
    return str(st1[0]) + str(seq) + describe_str(str1[seq:])



######################Q3#########################
class Car:
    def __init__(self, size, ide):
        self.size = size
        self.ide = ide


def insert(car):
    size = car.size
    ind = 0

    while ind + 1 < len(self.park_list):
        while size != 0:
            if self.park_list[ind] == None:
                size -= 1
            else:
                size = car.size
            ind += 1
        return True
    return False

    for i in range(car.size):
        self.park_list[ind] = car.ide
        ind -= 1


