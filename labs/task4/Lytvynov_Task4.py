from import_modules.validator import set_value

print('''IKM-221D Task_4
Lytvynov Danyil''')


def polindrom(x: str):
   return 'Polindrom' if x == x[::-1] else 'Not polindrom'


if __name__ == '__main__':

   x = set_value()

   print(polindrom(x))