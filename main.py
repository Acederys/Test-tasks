# Создайте класс People, конструктор* которого принимает аргумент name — имя человека.
# Класс должен содержать метод get_name, который возвращает имя заглавными буквами.
# * Метод __init__(), который мы изучили в первом уроке про классы, называется конструктором.

class People:
    def __init__(self,name):
        self.name= name
    def get_name(self):
        return self.name.upper()
name = People("Kate")
print(name.get_name())

# Создайте объект people класса People, а затем выведете на экран имя человека заглавными буквами с помощью метода get_name.

class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.upper()
people = People("Jon")
print(people.get_name())

# Сайт предназначен для мужчин от 20 до 30 лет включительно.
# Отфильтруйте список people, чтобы в нем осталась только целевая аудитория сайта.
# Результат должен быть помещен в переменную my_people.

people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]

males = [x for x in people if x["sex"] == "m"]
my_people = filter(lambda x: x["sex"]== "m" and x["age"]>=20 and x["age"]<=30, people)
print(my_people)
# Создайте функцию map, которая добавит к каждой комнате в списке rooms элемент с именем square содержащий её площадь.
rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]

# def add_square_to_room(room):
#     room["square"] = room["length"] * room["width"]
#     return room
# rooms = map(add_square_to_room, rooms)

rooms = map(lambda x: dict(square=x["length"] * x["width"], **x), rooms) #высчитали площадь каждой комнаты
print(rooms)

# В списке digits содержатся строки с числами.
# Эти строки содержат ошибки: лишние пробелы, неправильные разделители целой и десятичной части и тд.
# Создайте функцию, которая сначала исправит ошибки в строках, а затем преобразует каждую строку в вещественное число.
# Примените эту функцию ко всем элементам digits с помощью map.
# digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]
# не верно
# digits[3] = digits[3].replace(".",",")
# print(digits[3])
#
# def replaced(x):
#         x.replace(".",",")
#
# right_digits = list(map(replaced, digits))
# print(right_digits)



