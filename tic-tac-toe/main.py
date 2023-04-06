# Создаем игровую доску при помощи dictionary

theBoard = {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' После каждого хода мы будем перерисовывать игровую доску,
для этого создаем функцию printBoard'''


def print_board(board: int) -> None:
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

# Основная функция игры


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(theBoard)
        print("Твой ход, " + turn + ". Куда походить?")

        move = int(input())

        if move not in range(10):
            raise TypeError("lalalala")
        if not isinstance(move, int):
            raise TypeError("lolololo")

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Это поле уже занято.\nКуда походить?")
            continue

        # После 5го хода проверяем, не выиграл ли игрок Х или О
        if count >= 5:
            if theBoard[1] == theBoard[2] == theBoard[3] != '':  # проверяем верхний ряд
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break
            elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':  # проверяем средний ряд
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break
            elif theBoard[7] == theBoard[8] == theBoard[9] != ' ':  # проверяем нижний ряд
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break
            elif theBoard[1] == theBoard[4] == theBoard[6] != ' ':  # проверяем первый столбец
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break
            elif theBoard[2] == theBoard[5] == theBoard[7] != ' ':  # проверяем средний столбец
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break
            elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':  # проверяем правый ряд
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили ****")
                break
            elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':  # проверяем диагональ 1-5-9
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break
            elif theBoard[3] == theBoard[5] == theBoard[7] != ' ':  # проверяем диагональ 3-5-9
                print_board(theBoard)
                print("\nИгра окончена!")
                print(" **** " + turn + " победили **** ")
                break

        # Если никто не победил, а ходы кончились, объявляем "Ничью"
        if count == 9:
            print("\nИгра окончена ВНИЧЬЮ")

        # Тут мы будем менять X и O после каждого хода

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


game()
