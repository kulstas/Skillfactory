# C2.8. Итоговое задание
# Игра: Морской бой
# Студент: Кулагин Станислав
# Поток: FWP_123

# ============================================
import random as rnd

# ============================================
# ИСКЛЮЧЕНИЯ
# ============================================

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Выход за пределы доски!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли сюда!"

class BoardWrongExeption(BoardException):
    pass

# ============================================
# ВНУТРЕННЯЯ ЛОГИКА ИГРЫ
# ============================================


class Dot:
    """Класс, описывающий собственный тип данных - точку координат"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    """Класс, описывающий корабли"""
    def __init__(self, pos, size, rotate=""):
        self.pos = pos
        self.size = size
        self.rotate = rotate
        self.lives = size

    # метод возвращает все точки корабля
    @property
    def dots(self):
        ship_dots = []
        _pos = self.pos
        if self.rotate == "G":  # если установлен флаг G — ставим горизонтально
            for i in range(self.size):
                ship_dots.append(Dot(_pos.x + i, _pos.y))
        elif self.rotate == "V":  # если установлен флаг V — ставим вертикально
            for i in range(self.size):
                ship_dots.append(Dot(_pos.x, _pos.y + i))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    """Класс, описывающий игровые доски"""
    def __init__(self, hid=False, size=6):
        # занятые точки
        self.dot_busy = []
        # спискок точек всех кораблей доски
        self.ships = []
        # сокрытие доски
        self.hid = hid
        # живые корабли
        self.liveShips = None
        # размерность доски
        self.size = size

        # заполнение клеток поля
        self.area = [["O"] * size for _ in range(size)]

    # установка корабля
    def add_ship(self, ship):
        # проверяем все точки корабля на выход за пределы доски
        for i in ship.dots:
            if self.out(i) or i in self.dot_busy:
                raise BoardWrongExeption()
        for i in ship.dots:
            self.area[i.x][i.y] = "■"
            self.dot_busy.append(i)

        self.ships.append(ship)
        self.contour(ship)

    # метод обводки корабля слоем в 1 клетку
    def contour(self, ship, verb=False):
        _contour = []
        for i in ship.dots:
            _contour.append(Dot(i.x - 1, i.y - 1))
            _contour.append(Dot(i.x + 1, i.y - 1))
            _contour.append(Dot(i.x - 1, i.y + 1))
            _contour.append(Dot(i.x + 1, i.y + 1))
            _contour.append(Dot(i.x - 1, i.y))
            _contour.append(Dot(i.x + 1, i.y))
            _contour.append(Dot(i.x, i.y - 1))
            _contour.append(Dot(i.x, i.y + 1))

        for i in _contour:
            if not(self.out(i)) and i not in self.dot_busy:
                if verb:
                    self.area[i.x][i.y] = "."
                self.dot_busy.append(i)

    # вывод доски в строковом виде
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.area):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

        # else:
        #     print(f'===> {ship.size}-палубный корабль успешно установлен! <===')

    # метод проверки выхода точки за пределы доски
    def out(self, dot):
        if not(0 <= dot.x < self.size) or not(0 <= dot.y < self.size):
            return True
        else:
            return False

    # метод для определения выстрела
    def shot(self, s):
        if self.out(s):
            raise BoardOutException()  # возбуждаем исключение выхода за пределы поля

        if s in self.dot_busy:
            raise BoardUsedException()  # возбуждаем исключение выстрела по занятой точке

        self.dot_busy.append(s)

        for _ship in self.ships:
            if _ship.shooten(s):
                _ship.lives -= 1
                self.area[s.x][s.y] = "X"
                if _ship.lives == 0:
                    self.liveShips -= 1
                    self.contour(_ship, verb=True)
                    print("Ура! Корабль уничтожен полностью :D")
                    return False  # повтор хода не требуется
                else:
                    print("Ура! Попадание :)")
                    return True  # повтор хода

        self.area[s.x][s.y] = "T"  # помечаем промах
        print("Эх! Мимо :(")
        return False

    def begin(self):
        self.dot_busy = []  # обнуляем список занятых точек

# ============================================
# ВНЕШНЯЯ ЛОГИКА ИГРЫ
# ============================================

class Player:
    """Класс, описывающий действия всех игроков"""
    def __init__(self, self_board, enemy_board):
        self.self_board = self_board
        self.enemy_board = enemy_board

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_board.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    """Класс, дополняющий методы для ИИ"""
    def ask(self):
        _shot = Dot(rnd.randint(0, 5), rnd.randint(0, 5))
        print(f"Координаты: {_shot.x + 1} {_shot.y + 1}")
        return _shot

class User(Player):
    """Класс, дополняющий методы для Юзера"""
    def ask(self):
        while True:
            _shot = input("Введите 2 координаты выстрела в формате X Y: ").split()

            if len(_shot) != 2:
                print("Необходимо указать именно 2 координаты X Y")
                continue

            x, y = _shot

            if not (x.isdigit()) or not (y.isdigit()):
                print("Необходимо ввести целые числа!")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=6):
        self.size = size
        user_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True

        # добавляем игроков
        self.ai = AI(ai_board, user_board)
        self.user = User(user_board, ai_board)

        self.user.self_board.liveShips = self.ai.self_board.liveShips = len(self.ships_sizes)

    def try_add_ship(self):
        self.ships_sizes = [3, 2, 2, 1, 1, 1, 1]
        _board = Board(size=self.size)
        attempts = 0
        for s in self.ships_sizes:
            while True:
                attempts += 1
                if attempts > 2000:  # количество попыток в бесконечном цикле
                    return None
                _ship = Ship(Dot(rnd.randint(0, self.size), rnd.randint(0, self.size)), s, rnd.choice(["G", "V"]))
                try:
                    _board.add_ship(_ship)
                    break
                except BoardWrongExeption:
                    pass

        _board.begin()
        return _board

    def random_board(self):
        _board = None
        while _board is None:
            _board = self.try_add_ship()
        return _board

    def greet(self):
        print("--------------------------")
        print(">>>    ДА НАЧНЕТСЯ     <<<")
        print(">>>    МОРСКОЙ БОЙ     <<<")
        print("--------------------------")
        print("Формат ввода координат: X Y")
        print(">>> X - номер строки  <<<")
        print(">>> Y - номер столбца   <<<")

    def loop(self):
        step = 0
        while True:
            print("---------------------------")
            print(">>> ДОСКА ПОЛЬЗОВАТЕЛЯ <<<")
            print(f"> Осталось кораблей: {self.user.self_board.liveShips} <")
            print(self.user.self_board)
            print("---------------------------")
            print(">>> ДОСКА КОМПЬЮТЕРА <<<")
            print(f"> Осталось кораблей: {self.ai.self_board.liveShips} <")
            print(self.ai.self_board)
            print("---------------------------")
            if step % 2 == 0:
                print("Ход пользователя ...")
                repeat = self.user.move()
            else:
                print("Ход компьютера ...")
                repeat = self.ai.move()
            if repeat:
                step -= 1

            if self.ai.self_board.liveShips == 0:
                print("---------------------")
                print("ПОБЕДИЛ ПОЛЬЗОВАТЕЛЬ!")
                break

            if self.user.self_board.liveShips == 0:
                print("---------------------")
                print("ПОБЕДИЛ КОМПЬЮТЕР!")
                break
            step += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()