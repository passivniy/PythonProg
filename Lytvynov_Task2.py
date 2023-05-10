print('''Danyil Lytvynov
Task_2 IKM-221D''')


def set_values():
	while True:
		try:
			return list(map(int, input().split()))
		except ValueError:
			print('Uncorrect value.')


x, y, z = set_values()

print((x + z / 8) / (18.2 - pow(3.8, y) + 19.3))
