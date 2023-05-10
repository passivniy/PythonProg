print('''Danyil Lytvynov
Task_2 IKM-221D''')


def set_values():
	while True:
		try:
			return list(map(int, input().split()))
		except ValueError:
			print('Uncorrect value.')


def validate_zero_division():
	while True:
			x, y, z = set_values()
			if (18.2 - pow(3.8, y) + 19.3)!=0:
				return x,y,z


x, y, z = validate_zero_division()
print((x + z / 8) / (18.2 - pow(3.8, y) + 19.3))
