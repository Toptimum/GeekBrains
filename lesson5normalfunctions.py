import os


# функция перехода в папку
def go_to_folder():
	print("\nВыполним переход в другую папку.")
	name_folder = input("Введите название папки: ")

	try:
		os.chdir(os.getcwd() + "\\" + name_folder)
		print("Мы перешли в папку и теперь находимся в", os.getcwd())
	except FileNotFoundError:
		print("К сожалению, такой папки не существует.")

# функция вывода содержимого папки
def content_folder():
	print(f"\nВыводим содержимое текущей папки {os.getcwd()}:")
	if os.listdir(path="."):
		print(os.listdir(path="."))
	else:
		print("Папка пуста.")

# функция удаления папки
def delete_folder():
	print("\nУдалим папку.")
	name_folder = input("Введите название папки для удаления: ")

	try:
		os.rmdir(os.getcwd() + "\\" + name_folder)
		print("Папка успешно удалена.")
		content_folder()
	except:
		print("К сожалению, папка не пуста или она не существует.")

# функция создания новой папки
def create_folder():
	print("\nСоздадим новую папку.")
	name_folder = input("Введите название новой папки: ")

	try:
		os.mkdir(os.getcwd() + "\\" + name_folder)
		print("Папка успешно создана.")
		content_folder()
	except FileExistsError:
		print("К сожалению, папка с таким названием уже существует.")


#go_to_folder()
#content_folder()
#delete_folder()
#create_folder()
