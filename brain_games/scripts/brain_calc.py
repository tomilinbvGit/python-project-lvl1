#!/usr/bin/env python


import prompt
import random


# flake8: noqa: C901
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('What is the result of the expression?')

    for i in range(0, 3):
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        symbol = random.choice(['+', '-', '*'])

        print('Question: {0} {1} {2}'.format(value1, symbol, value2))
        check = prompt.integer('Your answer: ')

        if symbol == '+':
            sum = value1 + value2
            if sum == check:
                print('Correct!')
            else:
                print("{0} is wrong answer ;(. Correct answer was {1}\n".format(check, sum),
                      "Let's try again, {}!".format(name))
                break
        elif symbol == '-':
            minus = value1 - value2
            if minus == check:
                print('Correct!')
            else:
                print("{0} is wrong answer ;(. Correct answer was {1}\n".format(check, minus),
                      "Let's try again, {}!".format(name))
                break
        elif symbol == '*':
            multiplication = value1 * value2
            if multiplication == check:
                print('Correct!')
            else:
                print("{0} is wrong answer ;(. Correct answer was {1}\n".format(check, multiplication),
                      "Let's try again, {}!".format(name))
                break

        if i == 2:
            print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
