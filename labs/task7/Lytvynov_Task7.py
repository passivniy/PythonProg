class Complex:
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f'{self.__a} - {abs(self.__b)}i' if self.__b < 0 else f'{self.__a} + {self.__b}i'

    def __eq__(self, other):
        return self.__a == other.__a and self.__b == other.__b

    def __add__(self, other):
        return Complex(self.__a + other.__a, self.__b + other.__b)

    def __sub__(self, other):
        return Complex(self.__a - other.__a, self.__b - other.__b)

    def __mul__(self, other):
        return Complex(self.__a * other.__a, self.__b * other.__b)

    def __truediv__(self, other):
        return Complex(round(self.__a / other.__a, 2), round(self.__b / other.__b, 2))

    def module(self):
        return round(pow((pow(self.__a, 2) + pow(self.__b, 2)), 1 / 2), 2)


if __name__ == '__main__':
    a = Complex(5, 15)
    b = Complex(2, -7)

    print('Addition: ', a + b)
    print('Substract: ', a - b)
    print('Product: ', a * b)
    print('Difference: ', a / b)
    print('Module: ', Complex.module(a))
