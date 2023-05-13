from labs.task4.Lytvynov_Task4 import polindrom


def test_for_f_polindrom():
    input_param = '1221'
    result = 'Polindrom'
    actual = polindrom(input_param)
    assert result == actual


if __name__ == '__main__':
    test_for_f_polindrom()