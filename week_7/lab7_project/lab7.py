def print_reversed(n):
    if n < 1:
        return n
    else:
        print(n)
        return print_reversed(n - 1)


def rec_sum(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return n + rec_sum(n - 1)


def exp_n_x(n, x):
    if n < 0:
        return
    elif n == 0:
        return 1
    else:
        return rec_sum(x*(1/factorial(n)))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)




x = exp_n_x(7, 4 / 5)
print(round(x, 5))
