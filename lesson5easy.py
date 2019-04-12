# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

try:
	for num in range(1,10):
		os.mkdir(os.getcwd() + "/" + "dir_" + str(num))
	print("Успешно создано 9 папок.")
except:
	print("Не удалось создать новые папки - возможно, они уже существуют.")

print(os.listdir())


# Задача-2:
# Напишите скрипт, отображающий ПАПКИ текущей директории.

print("\nВыводим только папки текущей директории:")

for path, dirs, files in os.walk(os.getcwd()):
  for folder in dirs:
	  print(folder)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

print(f"\nПрограмма запущена из файла {__file__} - создадим его копию.")

shutil.copyfile(__file__, __file__ + " - копия")

print("Содержимое текущей папки:", os.listdir())
