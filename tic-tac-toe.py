def print_greeting():
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


# Перед началом игры приводит все в исходное состояние
def init_game():
    global game_board, free_cells, player
    game_board = [[' '] * 3 for i in range(3)]
    free_cells = [(i, j) for i in range(3) for j in range(3)]
    player = playerX


def print_board(board):
    # Напечатать первой строкой ось координат
    print()
    print("  | 0 | 1 | 2 ")
    print("--+---+---+---")
    for i in range(len(board)):
        print(str(i) + " | ", end="")
        print(" | ".join(board[i]))
        if i == len(board) - 1:
            break
        print("--+---+---+---")
    print()


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


# Проверяет, что игрок pl является победителем на игровом поле board
def is_winner(pl, board):
    # Можно посчитать символы игрока pl в каждой строке, столбце и
    # диагоналях. Если хоть где-то три символа игрока, то игрок
    # победил

    # Проверяем количество символов игрока в каждом столбце
    check_cols = any([
        [game_board[i][0] for i in range(3)].count(pl) == 3,
        [game_board[i][1] for i in range(3)].count(pl) == 3,
        [game_board[i][2] for i in range(3)].count(pl) == 3,
    ])

    # Проверяем количество символов игрока в каждой строке
    check_rows = any([
        game_board[0].count(pl) == 3,
        game_board[1].count(pl) == 3,
        game_board[2].count(pl) == 3,
    ])

    # Проверяем количество символов игрока на диагонали
    # слева направо
    check_main_diag = all([
        game_board[0][0] == pl,
        game_board[1][1] == pl,
        game_board[2][2] == pl,
    ])

    # Проверяем количество символов игрока на диагонали
    # справа налево
    check_other_diag = all([
        game_board[0][2] == pl,
        game_board[1][1] == pl,
        game_board[2][0] == pl,
    ])

    return any([check_rows, check_cols,
                check_main_diag, check_other_diag])


def game_loop():
    while True:
        # Вывести текущее состояние игрового поля
        print_board(game_board)

        global player
        print(f"Ход игрока {player}")

        # Запросить ввод координат клетки
        cell = ask_cell_coord()

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
        if is_winner(player, game_board):
            # Есть победитель
            # Вывести сообщение о победителе и выйти
            print_board(game_board)
            print(f" *** Игрок {player} победил! ***")
            print()
            break

        if not free_cells:
            # Нет свободных клеток
            # Вывести сообщение о ничьей и выйти
            print_board(game_board)
            print(" *** Ничья! ***")
            print()
            break

        # Передать ход другому игроку
        player = playerX if player == playerO else playerO


#
# Игровой процесс
#
print_greeting()
s = ""
while s != 'q':
    s = input("Введите 's', чтобы начать или 'q', чтобы выйти: ")
    if s == 's':
        print_help()
        init_game()
        game_loop()
