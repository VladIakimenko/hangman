from random import choice
import os

def read_words(path='words_list.txt'):
    words_list = []
    with open(path, 'r') as filehandle:
        for line in filehandle:
            for word in line.split():
                words_list.append(word)
    return words_list


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_hangman(stage):
    with open(f'hangman_pics/stage{stage}.txt', 'r') as filehandle:
        for line in filehandle:
            print(line[:-1])


def main(words):
    word = choice(words)
    stage = 0
    missing_letters = ''
    correct_letters = ''
    game_over = False
    display_word = ''.join(['_ ' for c in word])

    while True:
        cls()
        print(f'{" " * ((99 - len(display_word)) // 2)}'
              f'{display_word}')
        show_hangman(stage)

        if not game_over:
            if display_word.replace(' ', '') == word:
                print(f'{" " * ((99 - 7) // 2)}you win')
                break
            print(f'{" " * ((99 - len(missing_letters) - 17) // 2)}'
                  f'missing letters: {missing_letters}')
            letter = input(f'{" " * ((99 - 16) // 2)}'
                           f'open letter ... ').strip().lower()
            letter = letter[0] if len(letter) > 1 else letter
        else:
            print(f'{" " * ((99 - 9) // 2)}game over')
            break

        if letter in word:
            correct_letters += letter
            display_word = ''.join(['_ ' if c not in correct_letters
                                    else c + ' ' for c in word])
        else:
            missing_letters += f' {letter}'
            stage += 1
            if stage == 6:
                display_word = ' '.join(word)
                game_over = True

    global finished
    finished = input('"q" to quit, any key to continue... ')


# entry
os.system('mode 99,35')

words_list = read_words('words_list.txt')

finished = ''
while finished not in ('q', 'quit'):
    main(words_list)
