#   Section A

# Q1
# -> O(n)

# -> O(log(N))

# Q2

# -> lamda(*args, **kwargs) : 6

# Q3  #TODO

def even_odd(lst):
    return [even_num for even_num in lst[:] if even_num % 2 == 0]


lst_e = [5, 4, -6, 9, 7]
print(even_odd(lst_e))


# Q4

# source = [1,2]
# source[1] = [1,2]
# source = [1,[1,2]]
# j = 0
# i =0
# x = [[source]]
# i = 1
# x = [[source, source]]
# n = 10
# i = n
# x  = [[[1,[1,2]]*n]]
# j=1
# x = [[[1,[1,2]]*n], [[1,[1,2]]*n]]
# j = 2
# x = [[[1,[1,2]]*n], [[1,[1,2]]*n], [[1,[1,2]]*n]]
# j = n
# x = [[    *n], [[1,[1,2]]*n], [[1,[1,2]]*n], ...., [1,[1,2]]*n]]
# z = [[[1,[1,2]]*n], [[1,[1,2]]*n], [[1,[1,2]]*n], [[1,[1,2]]*n], [[1,[1,2]]*n], ]
# A >>  N+3

# B >> N

# 5


# 6
def depth_check(f):
    counter = 0

    def inner(x):
        return

    return inner


# 7

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def find_path(root: Node, k: int):
    if root is None:
        return None

    if root.left == root.right is None:
        if root.data == k:
            return [root.data]
        else:
            return None
    return find_path_helper(root, k, [])


def find_path_helper(node, k, lst):
    if node is None:
        return
    if node.left == node.right is None:
        if k == 0:
            return lst
        else:
            return

    return find_path_helper(node.left, k - node.data, lst.append(node.data)) + find_path_helper(node.right,
                                                                                                k - node.data,
                                                                                                lst.append(node.data))


# 8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vac_num = 0
        self.partner = None

    def get_vac_num(self):
        return self.vac_num

    def set_vac_num(self, n):
        self.vac_num = n

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_partner_name(self):
        return self.partner

    def marry(self, spouse):
        if spouse is None or spouse.spouse != self.name or self.partner.name != spouse.name:
            raise Exception
        else:
            if self.partner.name == spouse.get_partner_name():
                return
            else:
                self.partner = spouse
                spouse.marry = self


class VacinationCenter:
    def __init__(self, min_age):
        self.min_age = min_age
        self.vaccine_total = 0

    def set_age_limit(self, min_age):
        self.min_age = min_age


def give_vaccine(self, person):
    if self.vaccine_total > 0 and (
            person.get_age() > self.min_age or person.partner.get_vac_num() > 0 or person.get_vac_num() > 0):
        self.vaccine_total -= 1
        person.set_vac_num(person.get_vac_num() + 1)
    return


# Section B


# Q1
# 4/ lst1[lambda item: lst1.index(item)]


# Q2
# לא ידעתי איך לעקוב אחריה בצורה טובה ולא ניסיתי גם

# Q3
x = [(5, 4), (6, 3)]
y = [item for item in tup for tup in x]
y = [item for tup in x for super_items in tup for item in super_items]
for tup in x:
    for item in tup:
        item.append

tup = (5, 4)
item =5
y = [5, ]

# 6
def get_ingredient(final_item, recipes):
    for tup in recipes:
        ingredients = tup[0]
        recipe_results = tup[1]
        recipes_dict = fulfill_recipes_dict(ingredients, recipe_results, {})
        pure_ingredients = {recipes_dict[final_item]}
    for ingredient in recipes_dict[final_item]:
        if ingredient in recipes_dict:
            pure_ingredients.remove(ingredient)
            pure_ingredients.add(recipes_dict[ingredient])
            # need to add another condiatiuon that check if that run agian on the pure_ingredients and check if they have there not pure items


def fulfill_recipes_dict(ingredients, recipe_results, recipes_dict):
    for res in recipe_results:
        if res not in recipes_dict:
            recipes_dict[res] = ingredients
    return recipes_dict


# Q7
def find_prefix_sum(lst):
    return find_prefix_sum_helper(lst)


def find_prefix_sum_helper(lst, maxi= None):
    if len(lst) == 1:
        if maxi is None:
            return lst[0]
        elif maxi < lst[0]:
            return lst
        else:
            return lst[:-1]
    return find_prefix_sum_helper(lst[1:], lst[0]) + find_prefix_sum_helper(lst[:], maxi)


