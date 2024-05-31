class Shape:
    def perimeter(self, height, width):
        self.width = width
        self.height = height

    def area(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    pass




class Rectangle(Shape):
    pass
