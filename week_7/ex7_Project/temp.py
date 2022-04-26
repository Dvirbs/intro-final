# def count_sums(a, s):
#     collections = list()
#     helper(a, s, collections, list())
#     return len(collections)
#
#
# def helper(a, s, collection, temp):
#     if s == 0:
#         collection.append(temp)
#         return
#     elif len(a) == 0 or s < 0:
#         temp = list()
#         return 0
#     else:
#         helper(a[1:], s - a[0], collection, temp + [a[0]])
#         helper(a[1:], s, collection, temp)
#     return collection


# print(count_sums([3, 5], 8))
# print(count_sums([3, 5, 8, 9, 11, 12, 20], 20))
#
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


# print(count_sums([3, 5, 8, 9, 11, 12, 20], 20))
# print(count_sums([3, 5], 8))
def cartesian_product(lst: list[list]):
    return helper(lst, '', [])


def helper(lst, cur, new_lst):
    if not lst:
        new_lst.append(cur)
        return
    for lst_i in lst:
        for item in lst_i:
            print('cur= ', cur)
            print('item= ', item)
            new_cur = cur + item
            helper(lst[1:], new_cur, new_lst)

    return new_lst


print(cartesian_product([['a', 'b'], ['c', 'd', 'e']]))
