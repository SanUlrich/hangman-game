import random

from pictures import HANGMANPICS
from words import WORDS


def get_word(words: list):
    secret_word = random.choice(words)
    return secret_word.lower()


def check_guess(letter):
    if len(letter) != 1:
        print('Введите ОДНУ букву.')
    elif not letter.isalpha():
        print('Введите одну БУКВУ.')
    else:
        return letter.lower()


def retry():
    ans = input('Сыграть еще? (д/н): ')
    if ans.lower() in ['д', 'да', 'y', 'yes', 'da']:
        start_game(get_word(WORDS))


def start_game(word):
    word_form = list('_' * len(word))
    secret_word = list(word)
    guessed_letters = []
    out_of_tries = False
    fails = 0

    while word_form != secret_word and not out_of_tries:
        print(HANGMANPICS[fails])
        print('"', ''.join(word_form).upper(), '"')
        guess = check_guess(input('Введите букву: '))

        if guess is not None:
            if guess in guessed_letters:
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

        for k, v in enumerate(secret_word):
            if v in guessed_letters:
                word_form.pop(k)
                word_form.insert(k, v)

    if not out_of_tries:
        print(HANGMANPICS[fails])
        print('"', ''.join(secret_word).upper(), '"')
        print('Победа!')


def main():
    print('Добро пожаловать на виселицу!')
    secret_word = get_word(WORDS)
    start_game(secret_word)
    retry()


if __name__ == '__main__':
    main()
