#!/usr/bin/env python


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')

    for i in range(0, 3):
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)

        print('Question: {0} {1}'.format(value1, value2))
        check = prompt.integer('Your answer: ')

        while value1 != 0 and value2 != 0:
            if value1 > value2:
                value1 = value1 % value2
            else:
                value2 = value2 % value1

        result = value1 + value2

        if check == result:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;"
                  "(. Correct answer was '{}'.\n".format(check, result),
                  "Let's try again, {}!".format(name))
            break
        if i == 2:
            print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
