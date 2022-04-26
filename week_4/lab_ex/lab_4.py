

def largest_and_smallest(num1, num2, num3):
    """
    function find the minimum and maximum
    :return: the biggest one and the smaller one.
    """
    return min(num1, num2, num3), max(num1, num2, num3)


def init_board():
    num_match_raws = int(input("please choose the number of raws: "))
    board = []
    for i in range(num_match_raws):
        heap = int(input("choose number of match in the raw's {} : ".format(i+1)))
        board.append(heap)
    return board


def get_next_player():
    board = init_board()
    raw_choose = int(input("please choose number of raw : "))
    num_of_match = int(input("please choose number of match to take: "))
    if 0 < raw_choose:
        board[raw_choose] -= num_of_match
    return board


def print_board():
    print(get_next_player())


get_next_player()

