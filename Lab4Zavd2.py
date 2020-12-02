class Rectangle:
    def __init__(self, length=10, width=10):
        self.rectangle_setter(length, width)

    def rectangle_setter(self, length, width):
        if length <= 100 and width <= 100:
            self._length = length
            self._width = width
        else:
            print('Ошибка, по условию задачи длинна и ширина должны быть не более 100 см')

    def perimeter(self):
        return 2 * (self._length + self._width)

    def square(self):
        return self._length * self._width

    def rectangle_getter(self):
        print('Периметр:', self.perimeter())
        print('Площа :', self.square())


a = 20
b = 10
rectangle = Rectangle(length=20, width=10)
print("Сторона a - "+ str(rectangle._length))
print("Сторона b - "+ str(rectangle._width))
print("--------------")
rectangle.rectangle_getter()