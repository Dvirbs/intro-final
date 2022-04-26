def combinition_lock(*args):
    return helper(args, 0, True)


def helper(tup, i, can_succeed):
    def inner(x):
        print(tup)
        if len(tup) == i + 1:
            return tup[i] == x and can_succeed
        else:
            return helper(tup, i + 1, tup[i] == x and can_succeed)

    return inner


f = combinition_lock(1, 5, 5, 7, 10)
print(f(1)(5)(5)(7)(11))




##################################### Q2 ################################
def find_range(dict_list):
    if not dict_list:
        return {}, []
    all_dic = dict()
    all_values = list()
    for dic in dict_list:
        for value, key in dic.items():
            if key not in all_values:
                all_values.append(key)
                all_dic[value] = [value, value]
            else:
                cur_min = all_dic[value][0]
                cur_max = all_dic[value][1]
                all_dic[value] = [min(value, cur_min ), max(value, cur_max)]
    return (all_dic, all_values.sort())




################### Q?? #######################

class MyKeyError(Exception):
    pass


class MultiSet:
    def __init__(self):
        self.set = list()

    def insert(self, item):
        if item not in self.set:
            self.set.append(item)
        else:
            i = self.set.index(item)
            self.set.append(self.set[i])

    def extend(self, iterable):
        for it in iterable:
            self.insert(it)

    def remove(self, item):
        if item in self.set:
            self.set.remove(item)
        else:
            raise MyKeyError()

    def __str__(self):
        string = ', '.join(map(str, self.set))
        return '{' + string + '}'

    def __iter__(self):
        return self


m = MultiSet()
m.insert('a')
m.insert('a')
m.insert('b')
m.insert('b')
m.insert('b')
m.insert('c')
m.extend([1, 2, 3])

print(m)
m.remove('blga')

##################################### 2021 B ###################
# 6
def depth_check(f):
    counter = 0

    def inner(*args, **kargs):
        counter += 1
        res = f(args, kargs)
        return res, len(counter)

    return inner


@depth_check
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(7))


##################### Q2


def find_path(root, k):
    if root == None:
        return None
    lst = list()
    helper(root, k, lst)
    return lst


def helper(root, k, lst)
    if k - root.data == 0 and is_leaf(root):
        lst.append(root.data)
        return
    elif is_leaf(root):
        lst = []
        return
    lst.append(root.data)
    k -= root.data
    helper(root.left, k, lst)
    helper(root.right, k, lst)


def is_leaf(root):
    if root.left == root.right == None:
        return True


######## Q3 ##########
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vac_num = 0
        self.spuse = None

    def get_vac_num(self):
        return self.vac_num

    def set_vac_num(n):
        self.vac_num += n

    def get_age():
        return self.age

    def get_name():
        return self.name

    def marry(spuse):
        if spuse == None or \
                spuse.get_spouse() != self.get_name() or \
                self.spuse != spuse.get_name():
            raise Exception
        else:
            if self.spuse = spuse:
                return
            else:
                self.spuse = spuse
                spuse.marry(self)


class VaccinationCenter:
    vaccine_total = 50

    def __init__(self, min_age):
        self.min_age = min_age

    def set_age_limit(min_age):
        self.min_age = min_age

    def give_vaccine(person):
        if is_eligible(person):
            person.set_vac_num += 1
            self.vaccine_total -= 1
            return True
        else:
            return False

    def is_eligible(person):
        if person.get_age() < self.min_age:
            return False
        else:
            return true





