from rectangle import Rectangle, Square, RectangleNew, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(1)
circle_2 = Circle(2)

rect_3 = RectangleNew(3, 4, 11, 22)
rect_4 = RectangleNew(12, 5, 20, 30)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())


print(rect_3, rect_3.get_area())
print(rect_4, rect_4.get_area())