import prompt
import random


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def victory(a, name):
    if a == 'Correct!':
        return print(f'Congratulations, {name}! \n\n')
    else:
        return print(f'\nGame over, {name}\n\n')


def great_answer(num_1, num_2, operator):
    if operator == '-':
        res = num_1 - num_2
        return res
    elif operator == '+':
        res = num_1 + num_2
        return res
    else:
        res = num_1 * num_2
        return res


def logic_even():
    name = welcome_user()
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

    victory(a, name)


def logic_calc():
    name = welcome_user()
    print('What is the result of the expression?')

    count = 0
    while count != 3:
        num_1 = random.randint(5, 70)
        num_2 = random.randint(5, 20)
        lst = ['-', '+', '*']
        operator = random.choice(lst)
        print(f'Question: {num_1} {operator} {num_2}')
        answer = prompt.string('Your answer: ')
        great_reply = great_answer(num_1, num_2, operator)

        if operator == '-' and answer == str(num_1 - num_2):
            a = 'Correct!'
            print(a)
            count += 1
        elif operator == '+' and answer == str(num_1 + num_2):
            a = 'Correct!'
            print(a)
            count += 1
        elif operator == '*' and answer == str(num_1 * num_2):
            a = 'Correct!'
            print(a)
            count += 1
        else:
            a = f"'{answer}' is wrong answer;(.\
Correct answer was '{great_reply}.\nLet\'s try again, {name}!'"
            print(a)
            count = 3
    victory(a, name)
