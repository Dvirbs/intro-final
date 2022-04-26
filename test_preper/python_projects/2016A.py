# question 1
def compress(lst):
    tuple_lst = []
    for  index, item in enumerate(lst):
        if index == 0:
            tuple_lst.append((item,0))
        if item == tuple_lst[-1][0]:
            tuple_lst[-1] = (item,tuple_lst[-1][1]+1)
        else:
            tuple_lst.append((item,1))
    return tuple_lst
#lst = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a']
#print(compress(lst))


# question 2
def count_sums(a, s):
    return count_sum_helper(a, s, [])


def count_sum_helper(a, s, count: 0):
    if sum(a) < 0 or len(a) == 0:
        return
    if sum(a) == 0:
        count += 1
        print(count)
        return

    count_sum_helper(a, s, count)


print(count_sums([3, 5, 8, 9, 11, 12, 20], 20))
# question 3


# question 4
def aggregate(f):
    res_history = list()
    def inner(x):
        res = f(x)
        res_history.append(res)
        return res_history
    return inner

def f(x):
    return 2*x
h = aggregate(f)
print(h(7))
print(h(5))
print(h(7))

# question 4

def zipper(head1, head2):
    while head1:
        next_head1 = head1.next
        next_head2 = head2.next
        head1.next = head2
        head2.next = next_head1
        head1 = next_head1
        head2 = next_head2

    return
