# B5.6. Итоговое практическое задание
# Игра: Крестики - Нолики
# Студент: Кулагин Станислав
# Поток: FWP_123

# Инициализация игрового поля
area = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

# Выбор маркера: крестик или нолик
marker1 = input("Крестик(Х) или Нолик(О)?: ").lower()
marker2 = None
if marker1 == "x":
    marker2 = "o"
elif marker1 == "o":
    marker2 = "x"
else:
    print("Увы, я не знаю такого маркера =(")
    marker1 = input("Крестик(Х) или Нолик(О)?: ").lower()

print(f"Вы играете — {marker1}, аппонент играет — {marker2} \n")

# Ввод координаты
def input_step(marker=marker1):
    xy = str(input(f"Введите координату для ({marker}) — в формате ХY: "))

    # Проверка правильности координаты
    if xy and len(xy) == 2 and xy.isdigit():
        x, y = int(xy[0]), int(xy[1])

        if x > 2:
            print("Неверное значение Х")
            return input_step()
        elif y > 2:
            print("Неверное значение Y")
            return input_step()
        else:
            print(f"Координаты: X — {x}, Y — {y} \n")
            check_step(x, y, marker)
    else:
        print("Ошибочка ¯\_(ツ)_/¯ Попробуйте снова...")
        return input_step()


# Проверка каждого шага
def check_step(x, y, marker):

    # Установка маркера по заданной координате
    if area[y][x] == "":
        area[y][x] = marker
    else:
        print("Упс! Поле уже занято ¯\_(ツ)_/¯ Попробуйте снова...")
        input_step(marker)

    # Переключение очередности маркера
    marker = (marker2 if marker == marker1 else marker1)

    # Проверка шага на ничью
    if any("" in empty for empty in area):

        # Проверка шага на выигрыш
        for i in range(len(area)):

            # Проверка рядов по горизонтали
            if area[i][0] == area[i][1] == area[i][2] == "x":
                print(f"=== !!! УРА !!! Выиграли КРЕСТИКИ :D ===")
                return output_area(area)
            elif area[i][0] == area[i][1] == area[i][2] == "o":
                print(f"=== !!! УРА !!! Выиграли НОЛИКИ :D ===")
                return output_area(area)

            # Проверка рядов по вертикали
            elif area[0][i] == area[1][i] == area[2][i] == "x":
                print(f"=== !!! УРА !!! Выиграли КРЕСТИКИ :D ===")
                return output_area(area)
            elif area[0][i] == area[1][i] == area[2][i] == "o":
                print(f"=== !!! УРА !!! Выиграли НОЛИКИ :D ===")
                return output_area(area)

            # Проверка рядов по диагонали
            elif area[0][0] == area[1][1] == area[2][2] == "x" or area[2][0] == area[1][1] == area[0][2] == "x":
                print(f"=== !!! УРА !!! Выиграли КРЕСТИКИ :D ===")
                return output_area(area)
            elif area[0][0] == area[1][1] == area[2][2] == "o" or area[2][0] == area[1][1] == area[0][2] == "o":
                print(f"=== !!! УРА !!! Выиграли НОЛИКИ :D ===")
                return output_area(area)
            else:
                pass
    else:
        print("=== !!! УРА !!! Победила ДРУЖБА ¯\_(ツ)_/¯ ===")
        return output_area(area)

    output_area(area)
    return input_step(marker)


# Вывод игрового поля
def output_area(a):
    print("  0 1 2")
    for i in range(len(a)):
        print(i, end=" ")
        for j in range(len(a)):
            if a[i][j]:
                print(a[i][j], end=" ")
            else:
                print("-", end=" ")
        print(" ")
    print(" ")

output_area(area)
input_step()