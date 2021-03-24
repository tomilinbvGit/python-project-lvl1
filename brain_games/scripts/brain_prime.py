#!/usr/bin/env python


import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(0, 3):
        value = random.randint(1, 101)
        print('Question: ', value)
        check = prompt.string('Your answer: ')

        if value == 2 and check == 'yes':
            print('Correct!')
        elif value == 2 and check == 'no':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n",
                  "Let's try again, {}!".format(name))
            break
        elif (value % 2 == 0 or value % 3 == 0 or value % 5 == 0) and check == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n",
                  "Let's try again, {}!".format(name))
            break
        elif (value % 2 != 0 or value % 3 != 0) and check == 'yes':
            print('Correct!')
        elif (value % 2 == 0 or value % 3 == 0 or value % 5 == 0) and check == 'no':
            print('Correct!')

        if i == 2:
            print('Congratulations, {}'.format(name))



if __name__ == '__main__':
    main()
