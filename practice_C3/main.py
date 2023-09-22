"""Докинг"""

import formula

circle = int(input("Введите радиус круга: "))
square_w, square_h = int(input("Введите длину: ")), int(input("Введите ширину: "))

print("Круг больше") if formula.circle_area(circle) > formula.square_area(square_w, square_h) else print("Квадрат больше")