# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте, пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# класс игрушки и ее характеристики/атрибуты
class Toy():
	def __init__(self, name, character, material, color):
		self.name = name
		self.character = character
		self.material = material
		self.color = color

# класс фабрики и ее методы работы
class Factory():
	def buying_materials(self, material): # имитация закупки необходимых материалов
		self.material = material
		print(f"\nЗакупили {self.material}.")

	def buying_paints(self, color): # имитация закупки необходимых красок
		self.color = color
		print(f"Закупили краски {self.color}.")

	def sewing_toys(self, name, character, material, color): # имитация процесса создания игрушки
		self.name = name
		self.character = character
		self.material = material
		self.color = color
		print(f"Создали игрушку {self.name} ({self.character}) из {self.material} {self.color} цвета.")


idea_toy1 = Toy('Вуди Прайд', 'кукла-ковбой', 'дерево', 'коричневый')
toy1 = Factory()
toy1.buying_materials(idea_toy1.material)
toy1.buying_paints(idea_toy1.color)
toy1.sewing_toys(idea_toy1.name, idea_toy1.character, idea_toy1.material, idea_toy1.color)

idea_toy2 = Toy('Базз Лайтер', 'астрорейнджер', 'пластмасса', 'белый с зеленым')
toy2 = Factory()
toy2.buying_materials(idea_toy2.material)
toy2.buying_paints(idea_toy2.color)
toy2.sewing_toys(idea_toy2.name, idea_toy2.character, idea_toy2.material, idea_toy2.color)

idea_toy3 = Toy('Булзай', 'игрушечный конь', 'дерево', 'оттенки коричневого')
toy3 = Factory()
toy3.buying_materials(idea_toy3.material)
toy3.buying_paints(idea_toy3.color)
toy3.sewing_toys(idea_toy3.name, idea_toy3.character, idea_toy3.material, idea_toy3.color)


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
