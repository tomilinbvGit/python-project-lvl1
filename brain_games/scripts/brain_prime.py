#!/usr/bin/env python


import prompt
import random


# flake8: noqa: C901
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    prime_list = []

    for num in range(1, 101):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)

    for i in range(0, 3):
        value = random.randint(1, 101)
        print('Question: {}'.format(value))
        check = prompt.string('Your answer: ')

        if check not in ['yes', 'no']:
            print('Only "yes" or "no"!')
            break

        if value not in prime_list and check == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n",
                  "Let's try again, {}!".format(name))
            break
        elif value in prime_list and check == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.\n",
                  "Let's try again, {}!".format(name))
            break
        else:
            print('Correct!')

        if i == 2:
            print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
