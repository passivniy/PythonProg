import pytest
from labs.task7.Lytvynov_Task7 import Complex


@pytest.fixture()
def param_a():
	return Complex(5, 15)


@pytest.fixture()
def param_b():
	return Complex(2, -7)


def test_for_add(param_a, param_b):
	actual = param_a + param_b
	expected = '7 + 8i'
	assert actual == expected


def test_for_sub(param_a, param_b):
	actual = param_a - param_b
	expected = '3 + 22i'
	assert(str(actual)) == expected


def test_for_mul(param_a, param_b):
	actual = param_a * param_b
	expected = Complex(10, 105)
	assert actual == expected


def test_for_truediv(param_a, param_b):
	actual = param_a / param_b
	expected = '2.5 - 2.14i'
	assert(str(actual)) == expected


def test_for_module(param_a, param_b):
	actual = param_a.module()
	expected = '15.81'
	assert (str(actual)) == expected


def test_for_str(param_a, param_b):
	actual = Complex.__str__(param_a)
	expected = '5 + 15i'
	assert str(actual) == expected
