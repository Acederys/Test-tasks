# Создайте класс Point, который будет моделировать поведение точки в прямоугольной системе координат на плоскости.
#
# Конструктор класса должен принимать два аргумента x и y, которые отвечают за координаты точки.
#
# Изменение координат точки должно происходить с помощью свойств (property). Каждая координата должна быть отдельным свойством точки.
#
# Также нужно добавить метод set(x, y), с помощью которого можно изменить обе координаты.
#
# Значения координат должны храниться как float, однако класс должен принимать координаты
# представленные как числами (int, float), так и строками (str), которые можно преобразовать к float.
class Point:
    def __init__(self, x, y):
        self.set(x, y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = float(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = float(value)

    def set(self, x, y):
        self.x = x
        self.y = y

point = Point(12.34, "15.46")
print(type(point.x))
print(type(point.y))
point.x = "4"
point.y = 5.4
print(point.x)
print(point.y)
point.set(7, "99.8")
print(point.x)
print(point.y)

