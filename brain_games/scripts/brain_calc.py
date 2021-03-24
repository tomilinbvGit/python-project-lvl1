#!/usr/bin/env python


import prompt
import random


# flake8: noqa: C901
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')

    for i in range(0, 3):
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        symbol = random.choice(['+', '-', '*'])

        print('Question: {}{}{}'.format(value1, symbol, value2))
        check = prompt.integer('Your answer: ')

        if symbol == '+':
            if value1 + value2 == check:
                print('Correct!')
            else:
                print("{} is wrong answer ;(. Correct answer was {} + {}\n".format(check, value1, value2),
                      "Let's try again, {}!".format(name))
                break
        elif symbol == '-':
            if value1 - value2 == check:
                print('Correct!')
            else:
                print("{} is wrong answer ;(. Correct answer was {} - {} \n".format(check, value1, value2),
                      "Let's try again, {}!".format(name))
                break
        elif symbol == '*':
            if value1 * value2 == check:
                print('Correct!')
            else:
                print("{} is wrong answer ;(. Correct answer was {} * {}\n".format(check, value1, value1),
                      "Let's try again, {}!".format(name))
                break

        if i == 2:
            print('Congratulations, {}'.format(name))


if __name__ == '__main__':
    main()
