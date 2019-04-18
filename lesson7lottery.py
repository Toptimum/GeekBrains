'''
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
	9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
	  16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
'''

import random
import copy
import os

# класс отвечает за работу с карточками
class LottoCard():
	
	# метод генерации карточки
	def generate_lotto_card(self):
		card = [] # используем простой список, потому что так проще
		
		# карточку наполняем только уникальными числами
		for i in range(27):
			number = random.randrange(1,91)
			while number in card:
				number = random.randrange(1,91)
			card.append(number)
			
		card.sort() # числа в карточке сортируем по возрастанию
		
		# добавим нулевые значения в карточку - это будут пустые значения при выводе
		for i in range(4):
			# генерируем по 4 уникальные позиции в каждой строке, куда запишем нули
			k1, k2, k3 = random.randrange(0,8), random.randrange(9,17), random.randrange(18,26)
			while card[k1] == 0 or card[k2] == 0 or card[k3] == 0:
				k1, k2, k3 = random.randrange(0,8), random.randrange(9,17), random.randrange(18,26)
			card[k1], card[k2], card[k3]  = 0, 0, 0
			
		return card

	# метод форматированного вывода карточки
	def print_lotto_card(self, name, card, pulled_out_kegs):
		self.name = name
		self.card = copy.deepcopy(card) # работаем с копией
		self.pulled_out_kegs = pulled_out_kegs

		# заменяем все нули пробелом
		for i in range(len(self.card)):
			if self.card[i] == 0:
				self.card[i] = ' '

		# зачеркиваем все выпавшие числа
		for i in range(len(pulled_out_kegs)):
			if pulled_out_kegs[i] in self.card:
				index = self.card.index(pulled_out_kegs[i])
				self.card[index] = '_'

		# выводим карточку
		print(f"\n*** {self.name.title()} ***")
		stroka = ''
		for i in range(len(self.card)):
			if i % 9 == 0:
				stroka += '\n'
			stroka += str(self.card[i]) + ' '
		print(stroka)
		
		if len(pulled_out_kegs) >= 15: # после выпадения 15 бочонков начинаем проверку победителя
			count = 0
			for i in range(len(pulled_out_kegs)):
				if pulled_out_kegs[i] in card:
					count += 1
			if count == 15:
				print(f"Есть победитель. Победила {self.name.upper()}!")
				exit()

# класс отвечает за мешок в лотерее
class BagLottery():

	# метод генерации нового мешка с бочонками
	def new_bag_lottery(self):
		new_bag_lottery = [num for num in range(1,91)]
		return new_bag_lottery

	# метод генерации случайного бочонка
	def random_keg(self, bag_lottery):
		k = random.randint(1, len(bag_lottery))
		new_keg = bag_lottery.pop(k-1)
		print(f"\nНовый бочонок № {new_keg} (в мешке осталось {len(bag_lottery)} шт.)")
		return new_keg

# класс пользователя
class Person():

	# метод зачеркивания чисел в карточке
	def cross_out_keg(self, user_card1, new_keg):
		self.user_card1 = user_card1
		self.new_keg = new_keg

		answer = input(f"\nЗачеркнуть число {self.new_keg} в вашей карточке? Введите y/n: ")
		if answer == 'y' and new_keg in user_card1:
			return 'continue'
		elif answer == 'n' and new_keg not in user_card1:
			return 'continue'
		else:
			print(f"\nК сожалению, вы ошиблись. Проверьте наличие числа {self.new_keg} в вашей карточке.")
			return 'the end'


user1 = Person()

lotto_card = LottoCard()
# генерируем карточки для пользователя и компьютера
user_card1 = lotto_card.generate_lotto_card()
computer_card2 = lotto_card.generate_lotto_card()

# создаем мешок с бочонками
obj_bag_lottery = BagLottery()
bag_lottery = obj_bag_lottery.new_bag_lottery()

pulled_out_kegs = [] # все выпавшие бочонки

game = 'continue'

while game == 'continue':

	os.system('cls') # очищаем консоль перед выводом 
	
	print("Играем в лотерею...")

	# выводим карточки в форматированном виде
	game = lotto_card.print_lotto_card("Карточка пользователя", user_card1, pulled_out_kegs)
	game = lotto_card.print_lotto_card("Карточка компьютера", computer_card2, pulled_out_kegs)
	
	print(f"\nРанее из бочонка выпали: {pulled_out_kegs}.")
	
	# достаем новый бочонок из мешка
	new_keg = obj_bag_lottery.random_keg(bag_lottery)
	pulled_out_kegs.append(new_keg)
	
	game = user1.cross_out_keg(user_card1, new_keg)

else:
	print("\nИгра завершена. До свидания.")
