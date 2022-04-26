import boggle_board_randomizer
from boggle_gui import BoggleGUI
from game import Game


class BoggleControl:
    """
    this class is the game control. it connects the logic part and the gui.
    it has board, game(the model) and gui.
    """
    def __init__(self):
        self.board = boggle_board_randomizer.randomize_board()  # 2D list representing the board
        self._game = Game(self.board)   # a game(model)  object
        self.gui = BoggleGUI(self.board)    # a gui object

        # this part connects functions in the model and the gui for each button with the next function.
        for button_location in self.gui.get_button_chars():
            self.gui.set_button_commend(button_location, self.create_button_action(button_location))
        self.gui.set_display('')

    def create_button_action(self, button_location):
        """
        this function creates function that calling functions in
        the model and the gui for button in the gui.
        """
        # (-1, -1) representing the add_word button
        if button_location == (-1, -1):
            def add_word_func():
                # calling the add_word model's function which returns a tuple:
                # (if the word is legal, the word)
                legal, possible_word = self._game.add_word()
                if legal:
                    # if the word was added before possible word would be None.
                    if possible_word:
                        # updating the score in the gui and the taken words list in the gui.
                        self.gui.count_score(self._game.get_score())
                        self.gui.set_taken_word_list(possible_word)
                else:
                    # updating the wrong words list in the gui.
                    self.gui.set_wrong_word_list(possible_word)
                # setting the display for the next word
                self.gui.set_display('')
            return add_word_func

        # the button is a letter cube
        def letter_func():
            # calling the model function that works on the button's location and returns the current display
            display = self._game.bottom_clicked(button_location)
            # updating the display in the gui
            self.gui.set_display(display)
        return letter_func

    def run(self):
        # running the gui's main_loop
        self.gui.run()


if __name__ == '__main__':
    BoggleControl().run()
