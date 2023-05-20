from labs.task8_9.Lytvynov_Task8_9 import greeting, number_of_sides, func_for_serial_numbers, days_in_month, \
    leap_ordinary, calculate, money_function, chess, from_ten_to_two, from_two_to_ten


def test_for_f_greeting_full():
    f_param = ['admin', 'Name']
    actual = greeting(f_param)
    expected = ['Hello Admin,I hope you\'re well..', 'Name, thank you for logging in again..']
    assert actual == expected


def test_for_f_greeting_empty():
    f_param = []
    actual = greeting(f_param)
    expected = 'We need to find some users!'
    assert actual == expected


def test_for_f_n_of_sides_positive():
    f_param = 4
    actual = number_of_sides(f_param)
    expected = '4 sides it is : Quadrilateral'
    assert actual == expected


def test_for_f_n_of_sides_negative():
    f_param = 9
    actual = number_of_sides(f_param)
    expected = 'Error... Number of sides must be from 3 to 6'
    assert actual == expected


def test_for_f_serial_numbers():
    f_param = [1, 2, 3, 4]
    actual = func_for_serial_numbers(f_param)
    expected=['1st', '2nd', '3rd', '4th']
    assert actual == expected


def test_for_f_days_in_m():
    f_param = 'february'
    actual = days_in_month(f_param)
    expected = '28/29'
    assert actual == expected


def test_for_f_leap_year_t():
    f_param = 1916
    actual = leap_ordinary(f_param)
    expected = 'Leap year'
    assert actual == expected


def test_for_f_leap_year_f():
    f_param = 1915
    actual = leap_ordinary(f_param)
    expected = 'Ordinary year'
    assert actual == expected


def test_for_f_calculate_plus():
    assert calculate(5, 15, '+') == '5 + 15 = 20'


def test_for_f_calculate_minus():
    assert calculate(5, 15, '-') == '5 - 15 = -10'


def test_for_f_calculate_div():
    assert calculate(5, 10, '/') == '5 / 10 = 0.5'


def test_for_f_calculate_mod():
    assert calculate(5, 10, 'mod') == '5 % 10 = 5'


def test_for_f_calculate_pow():
    assert calculate(5, 2, 'pow') == '5 ^ 2 = 25'


def test_for_f_money_t():
    assert money_function(20) == 'Номінал : Двадцять гривень    Зображен : Іван Франко'


def test_for_money_f():
    assert money_function(39) == 'Uncorrect value!'


def test_for_money_f():
    assert chess(5, 'd') == '[5, d]: White'


def test_for_f_from_ten_to_two():
    assert from_ten_to_two(375) == '101110111'


def test_for_f_from_two_to_ten():
    assert from_two_to_ten('101110111') == 375

