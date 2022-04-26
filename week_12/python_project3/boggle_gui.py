import tkinter as tki
from typing import Dict, List, Any
import boggle_board_randomizer


BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth": 1,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}
BOARD = boggle_board_randomizer.randomize_board()
INITIAL_SCORE = 0


class BoggleGUI:
    """
    the boggle gui of the game
    """
    _buttons: Dict[tuple, tki.Button] = {}

    def __init__(self, board) -> None:

        # initial parameters
        self._board = board
        self._click_add_word = None
        self._taken_word_list = []
        self._wrong_word_list = []
        self._word_clicked = False
        self._score = INITIAL_SCORE

        # initial the main root and frame
        self.initial_the_root()

        # right frame
        self.right_frame()

        # left frame
        self.left_frame()

        # Timer
        # the timer is the most changeable functio and this is way we want to leave it in the init
        # that it will be comfortable to control

        def countdown(count):
            """
            the function the count down by count
            :param count:
            :return:
            """
            label['text'] = 'Time Remaining ( harry up! ) : ' + str(count)
            if count > 0:
                self._main_window.after(1000, countdown, count - 1)
        label = tki.Label(self._main_window)
        label.place(x=35, y=15)
        countdown(180)
        self._main_window.after(182000, self._main_window.destroy)

        # Score
        self._score_label = tki.Label(self._main_window, text='Your Score is 0')
        self._score_label.place(x=800, y=15)
        button = tki.Button(self._main_window, text='ADD WORD', command=self.add_word_clicked)
        self._buttons[(-1, -1)] = button
        button.pack(side=tki.TOP, pady=5)

        self._main_window.bind("<Key>", self._key_pressed)

    def initial_the_root(self):
        root = tki.Tk()
        root.title('boggle')
        root.resizable(False, False)  # nobody can change the height and length
        self._main_window = root
        self._text = ''
        self._latter_location = None
        self._display_label = tki.Label(self._main_window, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=10, relief="ridge")
        self._display_label.pack(side=tki.TOP, fill=tki.BOTH)
        self._outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)



    def right_frame(self):
        """
        creating the right frame of the gui
        """
        right_frame = tki.Frame(self._outer_frame)
        right_frame.grid(row=0, column=2)
        self._bottom_right = tki.Label(right_frame, text=self._taken_word_list, height=20, width=50, bg='green')
        self._bottom_right.pack(side=tki.BOTTOM, fill=tki.Y, expand=True)
        self._middle_frame = tki.Frame(self._outer_frame)
        self._middle_frame.grid(row=0, column=1)
        self._create_buttons_in_middle_frame()

    def left_frame(self):
        left_frame = tki.Frame(self._outer_frame)
        # left_frame.pack(side=tki.RIGHT, fill=tki.BOTH, expand=True)
        left_frame.grid(row=0, column=0)

        self._bottom_left = tki.Label(left_frame, text=self._wrong_word_list, height=20, width=50, bg='red')
        self._bottom_left.pack(side=tki.BOTTOM, fill=tki.Y, expand=True)

    def timer(self):
        pass



    def count_score(self, score):
        """
        function that count the score
        """
        # change text in label
        self._score = score
        self._score_label['text'] = 'Your Score is ' + str(self._score)

    def get_root(self):
        """
        get the root of the main window
        :return:
        """
        return self._main_window

    def set_taken_word_list(self, word: str) -> None:
        """
        append word the word list of of the correct word
        :param word: str of word
        :return: None
        """
        self._taken_word_list.append(word)
        self._bottom_right['text'] = self._taken_word_list

    def set_wrong_word_list(self, word: str) -> None:
        """
        append word the word list of of the wrong word
        :param word: str of word
        :return: None
        """
        self._wrong_word_list.append(word)
        self._bottom_left['text'] = self._wrong_word_list

    def add_word_clicked(self):
        """
        set flag of word clicked to True
        :return:
        """
        self._word_clicked = True

    def get_word_clicked(self):
        """
        get the flag the tell if the botton word clicked is pushed
        :return:
        """
        return self._word_clicked

    def set_word_clicked(self):
        """
        set the word clicked to False
        """
        self._word_clicked = False

    def set_flag_add_word(self) -> None:
        """
        set flag to add word to False
        :return:
        """
        self._click_add_word = False

    def get_latter_location(self):
        """
        get the letter location
        :return:
        """
        return self._latter_location

    def run(self) -> None:
        """
        run the main loop
        """
        self._main_window.mainloop()

    def set_display(self, display_text: str) -> None:
        """
        the the display text by the parameter display_text
        """
        self._display_label["text"] = display_text

    def set_text(self, latter):
        """
        set text bottom by latter
        :param latter: can be empty string or latter
        """
        self._text = latter

    def set_empty_display_label(self) -> None:
        """
        set empty display
        :return:
        """
        self._display_label['text'] = ''

    def set_display_by_click(self) -> None:
        """
        set display by clicked of the player
        :return:
        """
        self._display_label["text"] += self._text
        print(self._display_label["text"])
        if self._display_label["text"] in self._word_list:
            self._taken_word_list.append(self._display_label['text'])
            self._display_label['text'] = ''
            self._bottom_right["text"] = str(self._taken_word_list)
            print(self._taken_word_list)

    def set_button_commend(self, button_name: str, cmd) -> None:
        """
        the the bottom commend
        :param button_name: the botton that we want to control
        :param cmd: the commend
        :return:
        """
        self._buttons[button_name].configure(command=cmd)

    def get_button_chars(self) -> List[str]:
        """
        get the button chars
        :return:
        """
        return list(self._buttons.keys())

    def get_button_location(self, button_name):
        """
        get the button location
        """
        info = self._buttons[button_name].grid_info()
        return info["row"], info["column"]

    def _create_buttons_in_middle_frame(self) -> None:
        """
        create buttons in middle frame
        :return:
        """

        for i in range(4):
            tki.Grid.columnconfigure(self._middle_frame, i, weight=1)  # type: ignore

        for i in range(4):
            tki.Grid.rowconfigure(self._middle_frame, i, weight=1)  # type: ignore

        # board_list = self._board_list()
        self._make_button(self._board[0][0], 0, 0)
        self._make_button(self._board[0][1], 0, 1)
        self._make_button(self._board[0][2], 0, 2)
        self._make_button(self._board[0][3], 0, 3)
        self._make_button(self._board[1][0], 1, 0)
        self._make_button(self._board[1][1], 1, 1)
        self._make_button(self._board[1][2], 1, 2)
        self._make_button(self._board[1][3], 1, 3)
        self._make_button(self._board[2][0], 2, 0)
        self._make_button(self._board[2][1], 2, 1)
        self._make_button(self._board[2][2], 2, 2)
        self._make_button(self._board[2][3], 2, 3)
        self._make_button(self._board[3][0], 3, 0)
        self._make_button(self._board[3][1], 3, 1)
        self._make_button(self._board[3][2], 3, 2)
        self._make_button(self._board[3][3], 3, 3)

    def _make_button(self, button_char: str, row: int, col: int, command=None,
                     rowspan: int = 1, columnspan: int = 1):
        """
        make button
        :param button_char: str with the button char
        :param row: the row of the button
        :param col: the collumn of the button
        :param command: the command of it
        :param rowspan: how much span of the raw
        :param columnspan: how much span of the collumn
        :return:
        """
        button = tki.Button(self._middle_frame, text=button_char, command=command, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[(row, col)] = button

        def _on_enter(event: Any) -> None:
            """
            create the background when we enter to button
            """
            button['background'] = BUTTON_HOVER_COLOR
            self._text = button['text']

        def _on_leave(event: Any) -> None:
            """
            create the background when we leave button
            """
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", _on_enter)
        button.bind("<Leave>", _on_leave)
        return button

    def _key_pressed(self, event: Any) -> None:  # TODO check if we need this func
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
        if event.char in self._buttons:
            self._simulate_button_press(event.char)
            return event.char
        # elif event.keysym == "Return":
        # self._simulate_button_press("=")

    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR

        print(self._latter_location)
