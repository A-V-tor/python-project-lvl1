import prompt
import random
from functools import reduce


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


def find_common_divisor(a, b):
    lst_a = []
    lst_b = []
    new_lst = []
    d = 2
    while d * d <= a:
        if a % d == 0:
            lst_a.append(d)
            a //= d
        else:
            d += 1
    if a > 1:
        lst_a.append(a)
    d = 2
    while d * d <= b:
        if b % d == 0:
            lst_b.append(d)
            b //= d
        else:
            d += 1
    if b > 1:
        lst_b.append(b)
    res = lst_a if len(lst_a) < len(lst_b) else lst_b
    for i in res:
        if i in lst_a and i in lst_b:
            new_lst.append(i)
    return reduce(lambda x, y: x*y, new_lst)


def logic_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count != 3:
        num = random.randint(0, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')

        if num % 2 == 0 and answer == 'yes':
            a = 'Correct!'
            print(a)
            count += 1
        elif num % 2 != 0 and answer == 'no':
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
            a = f"'{answer}' is wrong answer ;(.\
Correct answer was '{great_reply}'.\nLet\'s try again, {name}!'"
            print(a)
            count = 3
    victory(a, name)


def logic_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count != 3:
        num_1 = random.randrange(5, 150, 5)
        num_2 = random.randrange(5, 100, 5)
        print(f'Question: {num_1} {num_2}')
        answer = prompt.string('Your answer: ')

        if answer == str(find_common_divisor(num_1, num_2)):
            a = 'Correct!'
            print(a)
            count += 1
        else:
            a = f"\'{answer}\' is wrong answer ;(.\
Correct answer was '{find_common_divisor(num_1, num_2)}'.\
\nLet\'s try again, {name}!"
            print(a)
            count = 3
    victory(a, name)
