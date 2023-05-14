class Complex:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b


    def __str__(self):
        if self.b < 0:
            return str(str(self.a) + str(self.b) + 'i')
        else:
            return str(str(self.a) + ' + '+str(self.b) + 'i')


    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)


    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)


    def __mul__(self, other):
        return Complex(self.a * other.a, self.b * other.b)


    def __truediv__(self, other):
        return Complex(round(self.a / other.a, 2), round(self.b / other.b, 2))


    def module(self):
        return(round(pow((pow(self.a, 2) + pow(self.b, 2)), 1/2), 2))
    
if __name__=='__main__':
    a = Complex(5, 15)
    b = Complex(2, -7)

    print('Addition: ', a + b)

    print('Substract: ', a - b)

    print('Product: ', a * b)

    print('Difference: ', a / b)

    print('Module: ', Complex.module(a))