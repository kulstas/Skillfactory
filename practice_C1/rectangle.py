class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def __eq__(self,other):
        return self.width==other.width and self.height==other.height

class Square:
    def __init__(self, a):
        self.a = a
    def get_area_square(self):
        return self.a ** 2


class Circle:
    def __init__(self, a):
        self.a = a
    def get_area_circle(self):
        return (self.a ** 2) * 3.14

class RectangleNew:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rentagle: {self.width, self.height, self.x, self.y}"

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height