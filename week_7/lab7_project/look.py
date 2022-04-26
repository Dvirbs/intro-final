def zero_4_all(n, k):
    if n == 0 and k == 0:
        return True


def only_k_left(n, k):
    if k > 0 and n == 0:
        return True


def only_n_left(n, k):
    if n > 0 and k == 0:
        return True


def both_can_step(n, k):
    if k > 0 and n > 0:
        return True


def rec_path(n, k, path, lst):
    if zero_4_all(n, k):
        lst.append(path)
    if only_k_left(n, k):
        rec_path(n, k - 1, path + "u", lst)
    if only_n_left(n, k):
        rec_path(n - 1, k, path + "r", lst)

    if both_can_step(n, k):
        rec_path(n - 1, k, path + 'r', lst)
        rec_path(n, k - 1, path + 'u', lst)


def up_and_right(n, k, l):
    path = ''
    rec_path(n, k, path, l)


Lst = []

up_and_right(2, 1, Lst)
