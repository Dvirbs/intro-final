# Section B

# Q 1
def all_increasing(lst):
    print(all_increasing_helper(lst, []))


def all_increasing_helper(lst, res):
    print(lst)
    if len(lst) == 0:
        res = res + [lst]
        return
    for i in range(len(lst) + 1):
        return all_increasing_helper(lst[:-i], res)

all_increasing([1,4,3,2])



#Q2
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        node4 = Node('b')
        node3 = Node('a', node4)
        node2 = Node('b', node3)
        self.__head = Node('a', node2)
        self.__tail = None

    def is_repetative(self, lst):
        flag = True
        while flag:

            for num in lst:
                if self.__head == None:
                    if num:
                        return True
                        break
                    else:
                        return False
                        break

                #print('num:', num)
                #print(' self.__head.data',  self.__head.data)
                if num != self.__head.data:
                    #print("num != self.__head=True")
                    return False
                    break
                self.__head = self.__head.next
        return True


myList = LinkedList()
print(myList.is_repetative(['a', 'b']))
myList = LinkedList()

print(myList.is_repetative(['a', 'b', 'a']))

#Q3
def find_discontinuity(lst):
    for i in range(len(lst)):
        if lst[i + 1] < lst[i]:
            new_lst = lst[i + 1:] + lst[:i + 1]
            break

    return new_lst


lst = [10, 11, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find_discontinuity(lst))


#Q4

def inverse(f, N):
    def inner(x):
        for i in range(0, N):
            if f(i) == x:
                return i

    return inner


def f(x):
    return (x + 1) % 7


g = inverse(f, 7)
print(g(3))

#Q5 #TODO return to this bad sol of my
class Range2D:

    def __init__(self, x, y):
        self._X = [i for i in range(x)]
        self._Y = [i for i in range(y)]
        self._points = []

    def __iter__(self):
        for y in self._Y:
            for x in self._X:
                self._points.append((x, y))

    def __next__(self):
        for point in self._points:
            return point


rect1 = Range2D(3, 2)
for point in rect1:  # iterate over all points in the Range2D
    print(point, end=" ")

#Q6
def most_common(lst):
    dic = {}
    max = [-len(lst), '_']
    for item in lst:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
        if max[0] < dic[item]:
            max[1] = item

    return max[1]


lst = ["alice", "bob", "alice", "carol", "carol", "alice"]

print(most_common(lst))



# 2017 A2
#q1
def function_power(f, n):
    def inner(x):
        res = f(x)
        for i in range(n-1):
            res = f(res)

        return res
    return inner

def f(x):
    return 2*x
g = function_power(f, 3)

print(g(10))


