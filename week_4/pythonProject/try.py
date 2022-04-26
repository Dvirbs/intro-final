import hangman_helper


def update_word_pattern(word, pattern, letter):
    """
    :param word: the word that the player need to guess
    :param pattern: The current pattern
    :param letter: the letter
    :return: updated pattern containing the same letter
    """
    if letter in word:
        index_list = [i for i in range(len(word)) if word[i] == letter]
        pattern_as_lst = list(pattern)
        for i in index_list:  # How to do it in on sentence
            pattern_as_lst[i] = word[i]
        new_pattern = ''
        for i in pattern_as_lst:
            new_pattern += i
        return new_pattern
    return pattern


def check_for_another_loop(score, pattern, the_word):
    if score == 0 or pattern == the_word:
        return False
    else:
        return True


def won_function(pattern, the_word):
    if pattern == the_word:
        return True
    else:
        return False


def run_single_game(words_list, score):
    """
    runs one game of the game hangman
    :return: The number of points of the player at the end of the game
    """
    the_word = hangman_helper.get_random_word(words_list)
    print(the_word)
    wrong_guess_lst = []
    pattern = '_' * len(the_word)
    msg = '*******     lets start to play hangman!     *******'

    while check_for_another_loop(score, pattern, the_word):
        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
        (input_type, player_input) = hangman_helper.get_input()

        if input_type == hangman_helper.LETTER:
            if len(player_input) > 1 or not player_input.isalpha() or not player_input.islower() or player_input == '!':
                print('\n********     your input is not correct, lets try again       ********')
            elif player_input in wrong_guess_lst or player_input in pattern:
                print('\n********     you choose this letter already /: lets try again        ********')
            else:
                score -= 1
                if player_input in the_word:
                    pattern = update_word_pattern(the_word, pattern, player_input)
                    n = the_word.count(player_input)
                    score += ((n * (n + 1)) // 2)
                    msg = "\n*******     Excellent Guess! let's try another one     *******"
                else:
                    wrong_guess_lst.append(player_input)
                    msg = "\n*******     Wrong Guess! You should try another one     *******"

        elif input_type == hangman_helper.WORD:
            score -= 1
            if player_input == the_word:
                n = pattern.count('_')
                score += (n * (n + 1)) // 2
                pattern = the_word

            else:
                wrong_guess_lst.append(player_input)
                msg = "\n*******\t try another guess *******\t"
        elif input_type == hangman_helper.HINT:
            score -= 1
            new_word_list = filter_words_list(words_list, pattern, wrong_guess_lst)
            n = len(new_word_list)
            if hangman_helper.HINT_LENGTH < n:
                short_word_list = []
                for i in range(0, hangman_helper.HINT_LENGTH):
                    short_word_list.append(new_word_list[(i*n)//hangman_helper.HINT_LENGTH])
                hangman_helper.show_suggestions(short_word_list)
            else:
                hangman_helper.show_suggestions(new_word_list)

    if score == 0:
        msg = '***********\nyou lose this time. The word that you needed to guess was {}\n ***********'.format(the_word)
        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
    if won_function(pattern, the_word):
        msg = '******************************\n you won! \n******************************'
        hangman_helper.display_state(pattern, wrong_guess_lst, score, msg)
    return score


def create_index_letters_dic(pattern):
    """
    creating dictionary with the the index and value of pattern notes
    :return: the dictionary
    """
    dic = {}
    pattern_lst = list(pattern)
    for note in pattern_lst:
        if note != '_':
            dic[note] = pattern.find(note)
    return dic


def find_same_length(word1, word2):
    """
    find if two words have the same length
    :return: True if does and False if not
    """
    if len(word1) == len(word2):
        return True
    else:
        return False


def find_same_letters_pattern(pattern, word):
    """
    function that find if all the letter in the pattern are similar to word
    :return: True if it the same and False if not
    """
    pattern_note_lst = list(pattern)
    word_letters_lst = list(word)
    if find_same_length(pattern, word):
        for i in range(len(pattern_note_lst)):
            if pattern_note_lst[i] != '_' or pattern_note_lst[i] == word_letters_lst[i]:
                return True
            else:
                return False
    else:
        return False


def letter_right_place(pattern, word):
    """
    find if there are letters that are in the pattern that are in wrong place in wanted filter word
    :return: True if does not found in right place and False if did found
    """
    pattern_index_letters_dic = create_index_letters_dic(pattern)
    lst_of_the_filter_word_letters = list(word)
    for index, value in enumerate(pattern):
        print('the index is: ', index)
        print("THE VALUE IS: ", value)
        if index <= len(lst_of_the_filter_word_letters) and value != '_':
            print("WE WNETERED IF AND REMOCEl:, ", lst_of_the_filter_word_letters[index])
            del lst_of_the_filter_word_letters[index]
    print("finished first loop")
    for val in pattern_index_letters_dic.values():
        print("value in patternd: ", value)
        if val in lst_of_the_filter_word_letters:
            return False
    return True


print(letter_right_place('a_b_c_', 'aabdce'))

def wrong_letters(wrong_guess_lst, word):
    """
    find if there are letters in wrong_guess_lst that are in word
    :return: True if does not and False if does
    """
    for letter in wrong_guess_lst:
        if letter in word:
            return False
    return True


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    getting list of words and pattern and match the previous pattern and guesses to the word list
    :param words: the ist of words
    :param pattern: the pattern
    :param wrong_guess_lst: the latters that are not correct
    :return: list of word after matching with the same order
    """
    new_words_list = []
    for word in words:
        if (find_same_length(word, pattern) and find_same_letters_pattern(pattern, word) and
                letter_right_place(pattern, word) and wrong_letters(wrong_guess_lst, word)):
            new_words_list.append(word)
    return new_words_list


def main():
    """

    :return:
    """
    num_of_games = 1
    while True:
        words_list = hangman_helper.load_words('C:/Google One/University/Third year/Intro/week_4/pythonProject/words.txt')
        score = run_single_game(words_list, hangman_helper.POINTS_INITIAL)
        if 0 < score:
            msg = "you played {} games until now, your total score is {}. want to play again?".format(num_of_games, score)
            decision = hangman_helper.play_again(msg)
            if decision:
                num_of_games += 1
            else:
                return
        elif score == 0:
            msg = "you played {} games until now, your total score is 0. want to play again?".format(num_of_games)
            decision = hangman_helper.play_again(msg)
            if decision:
                num_of_games = 1
                score = hangman_helper.POINTS_INITIAL
                score = run_single_game(words_list, score)
            else:
                return


if __name__ == '__main__':
    # main()
