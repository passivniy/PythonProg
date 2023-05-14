from labs.task7.Lytvynov_Task7 import Complex

PARAM_A = Complex(5, 15)
PARAM_B = Complex(2, -7)


def test_for_add():
	actual = PARAM_A+PARAM_B
	expected = '7 + 8i'
	assert str(actual) == expected


def test_for_sub():
	actual = PARAM_A-PARAM_B
	expected = '3 + 22i'
	assert(str(actual)) == expected


def test_for_mul():
	actual = PARAM_A*PARAM_B
	expected = '10-105i'
	assert(str(actual)) == expected


def test_for_truediv():
	actual = PARAM_A/PARAM_B
	expected = '2.5-2.14i'
	assert(str(actual)) == expected


def test_for_module():
	actual = PARAM_A.module()
	expected = '15.81'
	assert (str(actual)) == expected


def test_for_str():
	actual = Complex.__str__(PARAM_A)
	expected = '5 + 15i'
	assert str(actual) == expected


if __name__ == '__main__':
	test_for_add()

	test_for_sub()

	test_for_mul()

	test_for_truediv()

	test_for_module()

	test_for_str()
