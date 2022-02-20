def greeting():
    #    ("123456789_123456789_123456789_123456789_123456789_123456789_12")
    print("+------------------------------------------------------------+")
    print("|                     Крестики-нолики                        |")
    print("+------------------------------------------------------------+")


def print_help():
    #    ("123456789_123456789_123456789_123456789_123456789_123456789_12")
    print("+------------------------------------------------------------+")
    print("| Игра происходит на игровом поле 3 х 3 клетки. Первый ход   |")
    print("| делает игрок с символом 'Х'. Ход осуществляется путем      |")
    print("| ввода координат клетки. Начало координат находится в левом |")
    print("| верхнем углу                                               |")
    print("+------------------------------------------------------------+")


# Символы игроков. И игрок, делающий ход
playerX = 'X'
playerO = 'O'
player = playerX


# Игровое поле
# Квадрат 3х3. Первоначально каждая клетка игрового воля занята
# символом ' '(пробел). По ходу игры этот символ будет заменен
# на символы игроков: 'X' или 'O'.
game_board = [
    [' ']*3,
    [' ']*3,
    [' ']*3,
]


# Список свободных ячеек игрового поля. Первоначально все ячейки будут
# свободны. По ходу игры отсюда будут удаляться элементы. Когда список
# опустеет, игра закончится.
free_cells = [(i, j) for i in range(3) for j in range(3)]


def print_board(board):
    # Напечатать первой строкой ось координат
    print("  | 0 | 1 | 2 ")
    print("--+---+---+---")
    for i in range(len(board)):
        print(str(i) + " | ", end="")
        print(" | ".join(board[i]))
        if i == len(board) - 1:
            break
        print("--+---+---+---")


# Просит пользователя ввести координаты клетки, пока не будет ввведено
# значение в пределах игрового поля
def ask_cell_coord():
    while True:
        row = int(input("Введите номер строки: "))
        if 0 <= row <= 2:
            break
        else:
            print("За пределами игрового поля")
            print("Повторите ввод")

    while True:
        col = int(input("Введите номер столбца: "))
        if 0 <= col <= 2:
            break
        else:
            print("За пределами игрового поля")
            print("Повторите ввод")
    print("Введено ", row, col)
    return row, col


def game_loop():
    while True:
        # Вывести текущее состояние игрового поля
        print_board(game_board)

        # Запросить ввод координат клетки
        cell = ask_cell_coord()

        global player
        # Проверить, что клетка свободна
        if cell in free_cells:
            # Клетка свободна
            # Занять ее символом игрока, который делает ход
            game_board[cell[0]][cell[1]] = player
            free_cells.remove(cell)
        else:
            print("Позиция занята. Выберите другую позицию")
            continue

        # Если
        #     Есть победитель
        #     Вывести сообщение о победителе и выйти
        # Иначе если
        #     Нет свободных клеток
        #     Вывести сообщение о ничьей и выйти
        #
        # Передать ход другому игроку
        player = playerX if player == playerO else playerO


#
# Игровой процесс
#
greeting()
s = ""
while s != 'q':
    s = input("Введите 's', чтобы начать или 'q', чтобы выйти: ")
    if s == 's':
        print_help()
        game_loop()
