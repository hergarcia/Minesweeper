import math
from random import shuffle

def get_initial_parameters(level):

    if 1 > level or level > 10:
        print("Debe elegir un nivel del 1 al 10")
        return

    time = (int((math.sqrt(level) * 100)))
    long = (int(level * 5))
    width = (int((level * 5) * (16 / 9)) + 10)
    mines = int(long * width * 0.15)
    return (time, width, long, mines)


def generate_board_1d(size, mines):
    range_cantidad_false = range(size - mines)
    range_cantidad_true = range(mines)
    lista = [True for _ in range_cantidad_true]
    lista2 = [False for _ in range_cantidad_false]
    lista.extend(lista2)
    shuffle(lista)
    return lista


def convert_board_to_2d(ls, k):
    lista1 = []
    for j in range(int(len(ls) / k)):
        lista1.append(ls[j * k:(j * k) + k]),
    return lista1

def create_board(level):
    (time, width, long, mines) = get_initial_parameters(level)
    size = int(width * long)
    ls = generate_board_1d(size, mines)
    k = long
    board_2d = convert_board_to_2d(ls, k)
    return board_2d

def is_mine(board, x, y):
    if 0 <= y < len(board) and 0 <= x < len(board[0]):

        return board[y][x]

if __name__ == '__main__':
    level = int(input("Elija un nivel del 1 al 10: "))
    board = create_board(level)
    print(is_mine(board, 2, 3))
