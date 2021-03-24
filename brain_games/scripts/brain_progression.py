#!/usr/bin/env python


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What number is missing in the progression?')

    for i in range(0, 3):
        step = random.randint(1, 101)
        start = random.randint(1, 101)
        num = random.randint(0, 9)

        progression_list = [i for i in range(start, start + ((step * 9) + 1), step)]
        list_to_str = ''.join(progression_list)
        unknown = progression_list[num]
        progression_list[num] = '..'

        print('Question: {}'.format(list_to_str))
        check = prompt.integer('Your answer: ')

        if check == unknown:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n".format(check, unknown),
                  "Let's try again, {}!".format(name))
            break

        if i == 2:
            print('Congratulations, {}'.format(name))


if __name__ == '__main__':
    main()
