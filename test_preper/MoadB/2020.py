#########################2020-a2 #######################
##########################Q1######################

def min_chars(s1, s2):
    return helper(s1, s2, len(s1))


def helper(s1, s2, first_len):
    if not s1:
        return first_len
    elif s1 in s2:
        return first_len - len(s1)
    return min(helper(s1[1:], s2, first_len), helper(s1[:-1], s2, first_len))


# print(min_chars("cdef", "abzdef"))


##########################Q2######################
class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def shift(head, k):
    if k == 0:
        return head.data
    return shift(head.next, k - 1)


head = Node(10, Node(20, Node(30, Node(40, Node(50, Node(60))))))


# print(shift(head, 3))


###########################Q3#########################
def count_substrs(word):
    lst = list()
    helper(word, lst)
    return len(lst)


def helper(word, lst):
    print(word)
    if not word:
        return
    elif word[0] == word[-1]:
        lst.append(word)
    for ind, value in enumerate(word):
        helper(word[ind:-1], lst)
    print(lst)
    return


# print(count_substrs('abcab'))


################ 2020 C2 #####################

################### B1 ####################
def inter(intvals):
    lst = list()
    helper(intvals, lst, (-100000, 100000))
    return lst

# def helper(intvals, lst, overlap):
#     if not intvals:
#         return len(lst)
#     if overlap[0] < intvals[0][0] and intvals[0][1] < overlap[1]:
#         next_overlap = overlap
#         lst.append(intvals[0])
#     elif overlap[0] < intvals[0][0] and intvals[0][1] > overlap[1]:
#         next_overlap = (intvals[0][0], overlap[1])
#         lst.append(intvals[0])
#     elif overlap[0] > intvals[0][0] and intvals[0][1] < overlap[1]:
#         next_overlap = (overlap[0], intvals[0][1])
#         lst.append(intvals[0])
#     else:
#         next_overlap = overlap
#     return max(helper(intvals[1:], lst + [intvals[0]], next_overlap), helper(intvals[1:], lst, overlap))


# intvals = [(3, 8), (2, 4), (99,5666), (0, 5), (2, 7), (1, 8), (4.1, 4.8)]
# print(inter(intvals))


def inter(intvals):
    lst = list()
    helper(intvals, lst, intvals[0])
    return lst

def helper2(intvals, lst, )