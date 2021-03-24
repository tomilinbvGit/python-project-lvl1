#!/usr/bin/env python


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')

    for i in range(0, 3):
        step = random.randint(1, 101)
        start = random.randint(1, 101)
        num = random.randint(0, 9)

        se = [i for i in range(start, start + ((step * 9) + 1), step)]
        q = se[num]
        se[num] = '..'

        print('Question: {}'.format(se))
        check = prompt.integer('Your answer: ')

        if check == q:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n".format(check, q),
                  "Let's try again, {}!".format(name))
            break

        if i == 2:
            print('Congratulations, {}'.format(name))


if __name__ == '__main__':
    main()
