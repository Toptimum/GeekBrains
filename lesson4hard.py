# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]

# функция поиска пользователя по номеру карты
def get_person_by_card(card_number):
	for person in bank:
		if person['card'] == card_number:
			return person

# функция проверки пин-кода
def is_pin_valid(person, pin_code):
	if person['pin'] == pin_code:
		return True
	return False

# функция проверки баланса карты
def check_account(person):
	return round(person['money'], 2)

# функция снятия наличных
def withdraw_money(person, money):
	if person['money'] - money >= 0: # ошибка №3 - можно было снять только всю сумму
		person['money'] -= money
		return 'Вы сняли {} рублей.'.format(money)
	else:
		return f"На вашем счету недостаточно средств! Вы можете снять не больше {person['money']} руб."

# функция выбора действий пользователя
def process_user_choice(choice, person):
	if choice == 1: # ошибка №1 - меню не срабатывало из-за сравнения числа со строкой
		print(check_account(person))
	elif choice == 2: # ошибка №2 - сравнивали число и строку
		count = float(input('Сумма к снятию:'))
		print(withdraw_money(person, count))

# основная функция работы программы
def start():
	try:
		card_number, pin_code = input('Введите номер карты и пин-код через пробел: ').split()

		card_number = int(card_number)
		pin_code = int(pin_code)

		person = get_person_by_card(card_number)

		if person and is_pin_valid(person, pin_code):
			try: # теперь программа не будет ломаться при вводе числа с плавающей точкой
				while True:
					choice = int(input('Выберите пункт:\n'
									   '1. Проверить баланс\n'
									   '2. Снять деньги\n'
									   '3. Выход\n'
									   '---------------------\n'
									   'Ваш выбор:'))
					if choice == 3:
						break
					process_user_choice(choice, person)
			except ValueError:
				print("Ошибка ввода:\n- В работе с навигацией используйте цифры 1, 2 или 3.\n- При вводе дробных чисел используйте точку, а не запятую. Например, 123.45")
		else:
			print('Номер карты или пин-код введены не верно.')
	except:
		print("Ошибка ввода:\n- Номер карты и пин-код вводите через один пробел.")


start()
