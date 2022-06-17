import prompt
import random


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def victory(a):
    if a == 'Correct!':
        return print('\nYour victory ')
    else:
        return print('\nGame over')


def logic():
    print('Welcome to the Brain games!')
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count != 3:
        num = random.randint(0, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if num % 2 == 0 and answer == 'Yes':
            a = 'Correct!'
            print(a)
            count += 1
        elif num % 2 != 0 and answer == 'No':
            a = 'Correct!'
            print(a)
            count += 1
        else:
            a = 'No correct'
            count = 3

    victory(a)
