# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def user(name='Имя', age = 21, city = 'Москва'):
	str_user = f"{name}, {age} год(а), проживает в городе {city}."
	return str_user

print(user())
print(user('Олег'))
print(user('Артем', 25))
print(user('Тарас', 31, 'Москва'))


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_numbers(num1 = 1, num2 = 2, num3 = 3):
	return max(num1, num2, num3)

print(max_numbers())
print(max_numbers(3))
print(max_numbers(3,2))
print(max_numbers(4,6,5))
print(max_numbers(123,456,789))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def f_max_string(*args):
	max_length = 0
	for arg in args:
		if len(arg) > max_length:
			max_length = len(arg)
			max_string = arg
	print(f"Самая длинная строка: {max_string}")

		
f_max_string('1', '23', '456')
f_max_string('Taras', 'Oleg', 'Alexander', 'Афродита', 'Клеопатра')
f_max_string('Первое предложение', 'Второе предложение', 'Третье предложение', 'Четвертое предложение')
