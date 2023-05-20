import pytest

from labs.task4.Lytvynov_Task4 import polindrom


@pytest.mark.parametrize('input_param, expected', [('1221', 'Polindrom'), ('683', 'Not polindrom')])
def test_for_f_polindrom(input_param, expected):
    actual = polindrom(input_param)
    assert expected == actual
