# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП.
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока.
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random

print("Добро пожаловать в игру Mortal Kombat! (версия ООП)".upper())

class Person():
	def __init__(self, name, health, damage, armor):
		self.name = name
		self.health = health
		self.damage = damage
		self.armor = armor
		print(self.name, self.health, self.damage, self.armor)

	# метод имитации ущерба от удара с учетом защиты
	def damage_calculation(self, strength):
		self.strength = strength
		if self.strength > self.armor:
			self.force = self.strength - self.armor
			return self.force
		else:
			return 0

	# метод генерации силы удара
	def attack_calculation(self):
		self.strength = random.randint(1, self.damage)
		print(self.strength)
		return self.strength

class Player(Person):
	pass

class Enemy(Person):
	pass

class Fight():
	def __init__(self, health1, force1, health2, force2):
		self.health1 = health1
		self.force1 = force1
		self.health2 = health2
		self.force2 = force2

	def fight(self):
		while self.health1 > 0 and self.health2 > 0:
			self.health2 -= self.force1
			print("Противник получает урон", self.force1)
			self.health1 -= self.force2
			print("Игрок получает урон", self.force2)
		return self.health1, self.health2





player1 = Player('Игрок1', 100, 40, 20)
enemy2 = Enemy('Враг2', 100, 40, 20)

player1.strength = player1.attack_calculation()
player1.force = player1.damage_calculation(player1.strength)

enemy2.strength = enemy2.attack_calculation()
enemy2.force = enemy2.damage_calculation(enemy2.strength)

fight = Fight(player1.health, player1.force, enemy2.health, enemy2.force)
player1.health, enemy2.health = fight.fight()

if player1.health > enemy2.health:
	print(f"Игрок {player1.name} победил с {player1.health} очками жизни, против {enemy2.name} c {enemy2.health} очками жизни.")
else:
	print(f"Игрок {enemy2.name} победил с {enemy2.health} очками жизни, против {player1.name} c {player1.health} очками жизни.")

