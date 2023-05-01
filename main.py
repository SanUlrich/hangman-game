import random

from pictures import HANGMANPICS
from words import WORDS


def get_word(words: list):
    """
    Select random word from list
    :param words: list of words
    :return: random word from list
    """
    secret_word = random.choice(words)
    return secret_word.lower()


def check_guess(letter: str):
    """
    Check that input is just one letter
    :param letter: input string
    :return: one letter (str) in lowercase
    """
    if len(letter) != 1:
        print('Введите ОДНУ букву.')
    elif not letter.isalpha():
        print('Введите одну БУКВУ.')
    else:
        return letter.lower()


def retry():
    """
    Ask user for retry.
    :return: call start_game() with random word if answer is 'yes'
    """
    ans = input('Сыграть еще? (д/н): ')
    if ans.lower() in ['д', 'да', 'y', 'yes', 'da']:
        start_game(get_word(WORDS))


def start_game(word: str):
    """
    Main game loop. Wile game is on: wait for user input (some letter).
    :param word: random word (str)
    :return: win/loss. Ask for retry
    """

    word_form = list('_' * len(word))   # Make field for input letters like " _____ "
    secret_word = list(word)    # Convert secret word to list for ease of comparison
    guessed_letters = []    # List with user input letters
    out_of_tries = False    # Loss check
    fails = 0   # Count of failed attempts

    while word_form != secret_word and not out_of_tries:
        print(HANGMANPICS[fails])
        print('"', ''.join(word_form).upper(), '"')
        guess = check_guess(input('Введите букву: '))   # Returns one letter or None

        if guess is not None:
            if guess in guessed_letters:    # If the entered letter has already been
                print(f'Буква "{guess.upper()}" уже была.')
            elif guess not in set(secret_word):
                print(f'Буквы "{guess.upper()}" в слове нет.')
                guessed_letters.append(guess)
                fails += 1
                out_of_tries = (fails >= len(HANGMANPICS)-1)
                if out_of_tries:
                    print(HANGMANPICS[fails])
                    print('"', ''.join(secret_word).upper(), '"')
                    print('Повешен!')
            else:
                print(f'Буква "{guess.upper()}" есть в слове.')
                guessed_letters.append(guess)

        # Setting a letter in its place in the word field
        for k, v in enumerate(secret_word):
            if v in guessed_letters:
                word_form.pop(k)
                word_form.insert(k, v)

    # Victory check
    if not out_of_tries:
        print(HANGMANPICS[fails])
        print('"', ''.join(secret_word).upper(), '"')
        print('Победа!')


def main():
    """
    Launch game.
    :return:
    """
    print('Добро пожаловать на виселицу!')
    secret_word = get_word(WORDS)   # Get random word
    start_game(secret_word) # Start
    retry()


if __name__ == '__main__':
    main()
