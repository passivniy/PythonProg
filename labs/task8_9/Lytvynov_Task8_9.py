import random
from collections import defaultdict
from import_modules.validator import set_values, set_value

POLYGONS = {3: 'Triangle',
            4: 'Quadrilateral',
            5: 'Pentagon',
            6: 'Hexagon'}

MONTHS = {'January': 31, 'February': '28/29', 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
          'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

MONEY = {20: 'Двадцять гривень/Іван Франко',
         50: 'П\'ятдесять гривень/Михайло Грушевський',
         100: 'Сто гривень/Тарас Шевченко',
         200: 'Двісті гривень/Леся Українка',
         500: 'П\'ятсот гривень/Григорій Сковорода',
         1000: 'Тисяча Гривень/Владимир Вернадський'}

CHESS_LIST = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def greeting(array_users):
    if not array_users:
        return 'We need to find some users!'
    return ['Hello Admin,I hope you\'re well..' if i.lower() == 'admin' else
            f'{i}, thank you for logging in again..' for i in array_users]


def number_of_sides(count):
    return f'{count} sides it is : {POLYGONS[count]}' if count in POLYGONS else \
        'Error... Number of sides must be from 3 to 6'


def func_for_serial_numbers(array_for3):
    numbs = {1: '1st', 2: '2nd', 3: '3rd'}
    return [numbs.get(i, f'{i}th') for i in array_for3]


def days_in_month(month):
    return MONTHS.get(month.title(), 'Invalid value')


def leap_ordinary(year):
    return 'Leap year' if year % 4 == 0 and year % 100 != 0 else 'Ordinary year'


def calculate(x, y, act):
    operations = {
        '+': f'{x} + {y} = {x + y}',
        '-': f'{x} - {y} = {x - y}',
        '/': f'{x} / {y} = {x / y}' if y != 0 else 'Error: Division by zero!',
        'mod': f'{x} % {y} = {x % y}',
        'pow': f'{x} ^ {y} = {pow(x, y)}',
        'div': f'{x} // {y} = {x // y}'
    }
    return operations.get(act, 'Invalid operation')


def money_function(number):
    return str('Номінал : ' + str(MONEY[number][:(MONEY[number].find('/'))]) + '    Зображен : ' + str(
        MONEY[number][(MONEY[number].find('/')) + 1:])) if number in MONEY else 'Uncorrect value!'


def chess(pos1, pos2):
    return f'[{pos1}, {pos2}]: Black' if (CHESS_LIST[pos2] + pos1) % 2 == 0 else f'[{pos1}, {pos2}]: White'


def from_ten_to_two(value):
    result = ''
    while value != 0:
        value, remainder = divmod(value, 2)
        result += str(remainder)
    return str(result[::-1])


def from_two_to_ten(value):
    return sum(int(i) * pow(2, len(value) - idx) for idx, i in enumerate(value, 1))


def rock_paper_scissors(value):
    options = ['rock', 'paper', 'scissors']

    if value not in options:
        return f'Value Erorr, your value not in : {options}'

    x = value
    y = random.choice(options)

    if x == y:
        return 'Draw,try again!'

    return 'You are winner!' if x == 'rock' and y == 'scissors' or x == 'scissors' and y == 'paper' or x == 'paper' \
                                and y == 'rock' else 'You are loss.'


if __name__ == '__main__':
    print(greeting(['Danyil']))

    print(number_of_sides(7))

    print(func_for_serial_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print('Even' if int(input('Enter your value for even or odd : ')) % 2 == 0 else 'Odd')

    print(days_in_month(str(input('Month: '))))

    print(leap_ordinary(int(input('Year must be between 1900 to 3000 : '))))

    summ = 0
    value = 10
    while int(value) != 0:
        value = set_value(int)
        summ += int(value)
    print(summ)

    x, y = set_values()
    act = str(input(f'Enter action with ({x}, {y}) : '))
    print(calculate(x, y, act))

    print(money_function(20))

    print(chess(5, 'd'))

    print('In decimal : 375, in binary : ', from_ten_to_two(375))

    print('In binary : 101110111, in decimal : ', from_two_to_ten('101110111'))

    print(rock_paper_scissors(random.choice(['rock', 'paper', 'scissors']))
