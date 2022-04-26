# write your code here.

# you can use help() to find out about builtin modules or functions.

# pressing Ctrl-,  (Control-Comma) on your keyboard will let you change some
# settings for coderunner, including the addition of (very basic) autocomplete.


# def in_text(string,text):
#     if string=='' or string==text=='':
#         return True
#     elif text=='':
#         return False
#     if string[0] == text[0]:
#         return True
#     if in_text(string,text[1:]):
#         return in_text(string[1:], text[1:])
#     else:
#         return False

# print(in_text("0Asd0A23B57C15D32w","ABC"))

#       third Quiestion

# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.head = head

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

# def add_to_sorted(L1,L2):
#     while true:
#         if not L2.head:
#             L1.head = L1.next
#         L1_orginal_head = L1.head
#         L2_orginal_next = L2.next
#         if L2.data < L1.data or L1.head==None:
#             L1.head = L2.head
#             L2.next = L1_orginal_head
#         L2.head = L2_orignal_next

#               Moad A
#              Q1

# def seq_fib(n,t,k):
#     lst = []
#     for i in range(t-1):
#         lst.append(0)
#     lst.append(k)
#     if len(lst)>=n+1:
#         return lst[n]
#     else:
#         while True:
#             if len(lst)==n+1:
#                 return lst[-1]
#             lst.append(sum(lst[-t:]))

# print(seq_fib(4,2,1))

#                   Q2

def tree(root, subtrs=None):
    return [root, [] if subtrs is None else subtrs]


def root(tr):  # accepts a tree: tr
    return tr[0]


def subtrs(tr):  # accepts a tree: tr
    return tr[1]


def two_levels(irgun, name):
    pass


#                       Q9

# def go_digit(n,m):
#     if not n and not m:
#         return []
#     elif not n:
#         return m
#     elif not m:
#         return n
#     else:
#         str_1num = ''
#         str_2num = ''
#         for num in n:
#             str_1num += str(num)
#         for num in m:
#             str_2num += str(num)
#         final = int(str_1num) + int(str_2num)
#         print('final', final)
#         numbers_sum = []
#         for digit in str(final):
#             numbers_sum.append(digit)
#         return numbers_sum


# print(go_digit([1,2,3],[]))


#                   Q10

def max_classes_helper(schedule, maxim):
    if not schedule:
        return maxim

    time = schedule[0][1][1] - schedule[0][1][0]
    return (max_classes_helper(schedule[1:0], maxim + time) +
            max_classes_helper(schedule[1:0], maxim + time))




