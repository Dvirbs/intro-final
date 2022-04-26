#Q1
#
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# def linked_filter(f, lnk):
#     while True:
#         print(lnk.data)
#         if lnk.data is None:
#             return None
#         data = lnk.data
#         cann_add = f(data)
#         if cann_add:
#             new_lnk = lnk
#             break
#         lnk = lnk.next
#
#     while True:
#         if lnk.data is None:
#             return None
#             break
#         data = lnk.next.data
#         can_add = f(data)
#         if can_add:
#             new_lnk.next = lnk.next
#
#
# linked_filter(lambda x: (x + 1) % 2, Node(2, Node(3, Node(4, Node(5, Node(6))))))

#Q3
# def f3(n, x, y):
#     return helper(n, x, y, [])


# def helper(n, x, y, lst):
#     if n == 0:
#         return x
#     lst.append([helper(n - 1, x, y, lst)])
#
#     lst.append([helper(n - 1, y, x, lst)])
#     return lst
#
#
# print(f3(2, [3, '5'], 'xy'))
#


#Q5

def rotate_90_clock(mat):
    #mat = [[1, 2], [3, 4], [5, 6]]
    new_mat = []
    for row_i in range(len(mat[0])):
        new_mat.append([])
        #runing 2 times
        for col_i in range(len(mat)):
            new_mat[row_i].append(-1)
    n = len(mat) -1
    for i,row in enumerate(mat):
        for j, col in enumerate(row):
            new_mat[j][n-i] = col
    return new_mat




mat = [[1, 2], [3, 4], [5, 6]]
print(rotate_90_clock(mat))