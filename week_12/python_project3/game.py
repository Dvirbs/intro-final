from typing import *
from ex12_utils import path_find_word


def load_words(txt):
    """ loading words from a file to a list"""
    word_list = []
    with open(txt, 'r') as boggle_dict:
        for row in boggle_dict:
            word_list.append(row.rstrip('\n'))
        return word_list


class Game:
    """
    this class is the game model. it contains the complex logic.
    it has a current path, board, score, display, legal words and used words.
    it knows the rules of the game and do the all logistic part.
    """
    def __init__(self, board):
        self.__path: List[Tuple] = []   # the game current path
        self.__board = board    # 2D list representing the game's board
        self.__score = 0    # the user score, starting with 0
        self.__current_display: str = ''
        self.__words = set(load_words('boggle_dict.txt'))    # the legal words of the game
        self._taken_word_list = []  # the correct used words

    def set_game(self):
        """
        this function is called after a word has been guessed.
        it updates the display to be empty string and the path to be empty list.
        """
        self.__current_display = ''
        self.__path = []

    def add_word(self):
        """
        this function is called right after a word has been guessed.
        it checks if the word is legal and updates the game according to the results .
        """
        possible_word = path_find_word(self.__board, self.get_path())   # the word that came from the path
        word = possible_word in self.__words    # boolean value that present if the word is legal
        if word:
            # if the word has been guessed already
            if possible_word in self._taken_word_list:
                # the possible word is None so it won't count
                possible_word = None
            else:
                self.update_score()
                self._taken_word_list.append(possible_word)
        # setting the game for a new word
        self.set_game()
        # returns a tuple of boolean value(if the word legal) and the word
        return word, possible_word

    def get_path(self):
        return self.__path

    def get_score(self):
        return self.__score

    def update_score(self):
        """ updating the score according to the path's length"""
        self.__score += len(self.__path) ** 2

    def update_path(self, cell):
        """ upending the given cell to the current path """
        self.__path.append(cell)

    def is_clicked_possible(self, clicked):
        """ checking if the clicked cube is possible according to its length
        from the last cube in the current path or if it was clicked in this path before."""
        if clicked in self.__path:
            return False
        if len(self.__path) == 0:
            return True
        l_row, l_col = self.__path[-1]
        c_row, c_col = clicked
        if 0 <= abs(l_row - c_row) <= 1 and 0 <= abs(l_col - c_col) <= 1:
            return True

    def bottom_clicked(self, cell_location):
        """
        checking if the given clicked cube is possible to be contained
        in the path. if it is, updating the path and the display
        """
        if self.is_clicked_possible(cell_location):
            self.update_path(cell_location)
            y, x = cell_location
            self.__current_display += self.__board[y][x]

        return self.__current_display
