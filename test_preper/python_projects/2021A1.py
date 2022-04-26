# 1
def foo(n):
    lst = []
    for i in range(n):
        lst.append(i)
        lst = lst[::-1]
    return lst


print(foo(9))


# 2
def transdice(vec):
    sp = {index: value for index, value in enumerate(vec) if value != 0}
    return sp


vec = [0, 0, 6, 0, 3, 6]
print(transdice(vec))

# 3

log(n)

# 4

dict[int, callable[[str], callable[[], str]]]

# 5
a = 5

tuple2 = (2, (1, (0, ())), (1, (0, ())), (2, (1, (0, ())), (1, (0, ()))), (2, (1, (0, ())), (1, (0, ()))))
res = (3, tuple2)

b = 9


# 6

def combination_lock(*args):
    def inner(x):
        if x != args[0]:
            return False

        def inner_2(y):
            if y != args[1]:
                return False

            def inner_3(z):
                if z != args[2]:
                    return False

                def inner_4(w):
                    if w != args[3]:
                        return False

        return True

    return inner


# def inner_helper(x,lst):
#     if x!=lst[0]:
#         return False
#     return inner_helper(x,lst[1:])

f = combination_lock(1, 2, 3, 4)
print(f(1)(2)(3)(4))


# 7
def find_range(dict_list):
    world_dict = {}
    the_list = []

    for dict_i in dict_list:
        world_dict, the_list = world_dict_maker(dict_i, world_dict, the_list)

    return world_dict, sorted(the_list)


def world_dict_maker(dict_i, world_dict, the_list):
    for key in dict_i:
        maxi = mini = dict_i[key]
        if key not in world_dict:
            the_list.append(key)
            world_dict[key] = [mini, maxi]
        else:
            print(mini)
            print(world_dict[key][0])
            if world_dict[key][0] > mini:
                world_dict[key] = mini
            elif maxi > world_dict[key][1]:
                world_dict[key] = maxi
    return world_dict, the_list


dict_list = [{'glope': 4, 'is': 7, 'best': 10}, {'glope': 2, 'best': 6}, {'glope': 1, 'is': 2}, {'dippy': 2}]
print(find_range(dict_list))

# 8
Noa

# SECTION b
# 1
o(N ^ 2)


# 2
def f(start, end, step):
    print(start, end=' ')
    if start < end:
        f(start + step, end, step)
        print(start - step, end=' ')


f(1, 12, 3)
# 3
O(N ^ 2)
# 4
l = ['abcd', 'efgh', 'wixy', 'zopm']

# 5
N + 1 + 2 + 3 + 4 + 5 + 6 + 7 + ... + N
