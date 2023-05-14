from labs.task4.Lytvynov_Task4 import polindrom


def test_for_f_polindrom_true():
    input_param = '1221'
    result = 'Polindrom'
    actual = polindrom(input_param)
    assert result == actual


def test_for_f_polindrom_false():
    input_param = '683'
    result = 'Not polindrom'
    actual = polindrom(input_param)
    assert result == actual


if __name__ == '__main__':
    test_for_f_polindrom_true()

    test_for_f_polindrom_false()
