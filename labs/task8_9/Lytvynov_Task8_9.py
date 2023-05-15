import random
from import_modules.validator import set_values,set_value

def greeting(array_users):
    result = []
    if len(array_users) == 0:
        return str('We need to find some users!')
    for i in array_users:
        if i.lower() == 'admin':
           result.append('Hello Admin,I hope you\'re well..')
        else:
           result.append(i+', thank you for logging in again..')
    return result


def number_of_sides(count):
    if count > 6 or count < 3: return str('Error... Number of sides must be from 3 to 6')
    else:
       lst = {'3': 'Triangle',
              '4': 'Quadrilateral',
              '5': 'Pentagon',
              '6': 'Hexagon'}
    return str(f'{count} sides it is : ' + lst[str(count)])


def func_for_serial_numbers(array_for3):
    result = []
    for i in array_for3:
       if i == 1:
           #print(str(i) + 'st')
           result.append(str(i) + 'st')

       elif i == 2:
           #print(str(i) + 'nd')
           result.append(str(i) + 'nd')

       elif i == 3:
           #print(str(i) + 'rd')
           result.append(str(i) + 'rd')

       else:
           #print(str(i) + 'th')
           result.append(str(i) + 'th')
    return result


def days_in_month(month):
    tpl = {'January': 31, 'February': '28/29', 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
         'September': 30, 'October': 31, 'November': 30, 'December': 31}
    return str(tpl[month.title()])


def leap_ordinary(year):
    if year % 4 == 0 and year % 100 != 0:
        return str('Leap year')
    else:
        return str('Ordinary year')


def calculate(x, y, act):
    if act == '+':
        return str(f'{x} + {y} = {x + y}')
    elif act == '-':
        return str(f'{x} - {y} = {x - y}')
    elif act == '/':
        try:
            return str(f'{x} / {y} = {x / y}')
        except ZeroDivisionError:
            return 'Error: Division by zero!'
    elif act == 'mod':
        return str(f'{x} % {y} = {x % y}')
    elif act == 'pow':
        return str(f'{x} ^ {y} = {pow(x, y)}')
    elif act == 'div':
        return str(f'{x} // {y} = {x // y}')


def money_function(number):
    lst = {20: 'Двадцять гривень/Іван Франко',
           50: 'П\'ятдесять гривень/Михайло Грушевський',
           100: 'Сто гривень/Тарас Шевченко',
           200: 'Двісті гривень/Леся Українка',
           500: 'П\'ятсот гривень/Григорій Сковорода',
           1000: 'Тисяча Гривень/Владимир Вернадський'}
    if number in lst:
        return str('Номінал : ' + str(lst[number][:(lst[number].find('/'))]) + '    Зображен : ' + str(lst[number][(lst[number].find('/')) + 1:]))
    else:
        return 'Uncorrect value!'


def chess(pos1, pos2):
    lst = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    x = str()
    for i in reversed(range(8)):
        print('')
        for j in reversed(range(8)):
            if i+j == 0 or (i + j) % 2 == 0:
                if pos1 == i+1 and lst[pos2] == j-1:
                    print('□', end=' ')
                    x = 'w'
                else:
                    print('w', end=' ')
            else:
                if pos1 == i and lst[pos2] == j:
                    print('■', end=' ')
                    x = 'b'
                else:
                    print('b', end=' ')
    return str('\nYour postition is :' + ' White' if x == 'w' else ' Black')


def from_ten_to_two(value):
    result = ''
    while value != 0:
        if value % 2 == 0:
            result += '0'
            value = value/2
        else:
            result += '1'
            value = (value-(value % 2)) / 2
    return str(result[::-1])


def from_two_to_ten(value):
    x = len(value)
    y = 1
    result = 0
    for i in value:
        result += int(i) * pow(2, x-y)
        y += 1
    return result


def rock_paper_scissors(value):
    lst = ['rock', 'paper', 'scissors']

    if value not in lst:
        return f'Value Erorr, your value not in : {lst}'

    x = value
    y = random.choice(lst)

    print(f'Your turn: {value}')
    print(f'Computers turn: {y}')

    if x == 'rock' and y == 'scissors':
        return 'You are winner!'

    elif x == 'scissors' and y == 'paper':
        return 'You are winner!'

    elif x == 'paper' and y == 'rock':
        return 'You are winner!'

    elif x == y:
        return 'Draw,try again!'

    else:
        return 'You are loss.'


if __name__ == '__main__':
    print(greeting(['Danyil']))

    print(number_of_sides(5))

    print(func_for_serial_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    print('Even' if int(input('Enter your value for even or odd : ')) % 2 == 0 else 'Odd')

    print(days_in_month(str(input('Month: '))))

    print(leap_ordinary(int(input('Year must be between 1900 to 3000 : '))))

    summ = 0
    value = 10
    while int(value) != 0:
        value = set_value()
        summ += int(value)
    print(summ)

    x, y = set_values()
    act = str(input(f'Enter action with ({x}, {y}) : '))
    print(calculate(x, y, act))

    print(money_function(20))

    print(chess(5, 'd'))

    print('In decimal : 375, in binary : ', from_ten_to_two(375))

    print('In binary : 101110111, in decimal : ', from_two_to_ten('101110111'))

    print(rock_paper_scissors(random.choice(['rock', 'paper', 'scissors'])))
