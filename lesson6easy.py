# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
 
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car():
	def __init__(self, name, color, speed, is_police):
		self.name = name
		self.color = color
		self.speed = speed
		self.is_police = is_police
		self.status_car = 'Гражданская'
		if self.is_police:
			self.status_car = 'Полицейская'

	def go(self):
		print(f"\n{self.status_car} машина {self.name} поехала со скоростью {self.speed} км/ч.")

	def stop(self):
		print(f"{self.name} {self.color} цвета остановилась.")

	def turn(self, direction):
		self.direction = direction
		print(f"О нет, машина {self.name} повернула {self.direction}!")

class TownCar(Car):
	pass

class SportCar(Car):
	pass

class WorkCar(Car):
	pass

class PoliceCar(Car):
	pass


common_car = Car('Жигули', 'желтого', 60, False)
common_car.go()
common_car.stop()
common_car.turn('направо')

kia_car = TownCar('Kia', 'серого', 70, False)
kia_car.go()
kia_car.stop()
kia_car.turn('налево')

bmw_car = SportCar('BMW', 'красного', 120, False)
bmw_car.go()
bmw_car.stop()
bmw_car.turn('направо')

mercedes_car = WorkCar('Mercedes-Benz', 'черного', 100, False)
mercedes_car.go()
mercedes_car.stop()
mercedes_car.turn('направо')

ford_car = PoliceCar('Ford', 'белого', 130, True)
ford_car.go()
ford_car.stop()
ford_car.turn('налево')
