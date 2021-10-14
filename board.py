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
        if board[y][x]:
            lista = get_all_the_mines(board)
            num = 0
        else:
            lista = []
            num = get_mines_around(board, x, y)

        is_mine_dict = {

            "mina": board[y][x],
            "lista": lista,
            "numero": num
        }
        return is_mine_dict


def get_all_the_mines(board):
    lst_coord_dict = []
    for index_y, filas in enumerate(board):
        for index_x, mina in enumerate(filas):
            if mina:
                coord_dict = {
                    "x": index_x,
                    "y": index_y
                }
                lst_coord_dict.append(coord_dict)
    return lst_coord_dict


def get_mines_around(board, x, y):
    def casos_validos(caso):
        (time, width, long, mines) = get_initial_parameters(level)
        if 0 <= caso[0] < width and 0 <= caso[1] < long:
            return True
        else:
            return False

    def minas_cercanas(casilla):
        if board[casilla[0]][casilla[1]]:
            return True
        else:
            return False

    lst_casos = [
        ((y + 1), x),
        ((y - 1), x),
        (y, (x + 1)),
        (y, (x - 1)),
        ((y + 1), (x + 1)),
        ((y - 1), (x - 1)),
        ((y + 1), (x - 1)),
        ((y - 1), (x + 1))
    ]
    lista_casillas_validas = list(filter(casos_validos, lst_casos))
    numero_minas_cercanas = len(list(filter(minas_cercanas, lista_casillas_validas)))
    return numero_minas_cercanas


if __name__ == '__main__':
    level = int(input("Elija un nivel del 1 al 10: "))
    board = create_board(level)
    resultado = []


def discover_clear_cells(board, x, y, visited=[]):
    def casos_validos(caso):
        (time, width, long, mines) = get_initial_parameters(1)
        if 0 <= caso[0] < width and 0 <= caso[1] < long:
            return True
        else:
            return False

    lst_casos = [
        ((y + 1), x),
        ((y - 1), x),
        (y, (x + 1)),
        (y, (x - 1)),
        ((y + 1), (x + 1)),
        ((y - 1), (x - 1)),
        ((y + 1), (x - 1)),
        ((y - 1), (x + 1))
    ]
    casillas_cercanas = list(filter(casos_validos, lst_casos))

    num1 = get_mines_around(board, x, y)
    visited.append((x, y))
    if num1 == 0 and visited.count((x, y)) < 2:
        for celda in casillas_cercanas:
            num2 = get_mines_around(board, celda[1], celda[0])
            if resultado.count({"x": celda[1], "y": celda[0], "numero": num2}) == 0: resultado.append({"x": celda[1], "y": celda[0], "numero": num2})
        for celda in casillas_cercanas:
            discover_clear_cells(board, celda[1], celda[0], visited)
    elif resultado.count({"x": x, "y": y, "numero": num1}) == 0: resultado.append({"x": x, "y": y, "numero": num1})
    return resultado

