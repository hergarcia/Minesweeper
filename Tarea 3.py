from board import create_board


def get_all_the_mines(board):
    lst_coord_dict = []
    for index_y, filas in enumerate(board, start=1):
        for index_x, mina in enumerate(filas, start=1):
            if mina:
                coord_dict = {
                    "x": index_x,
                    "y": index_y
                }
                lst_coord_dict.append(coord_dict)
    return lst_coord_dict


def get_mines_around(board, x, y):
    mines_dict = get_all_the_mines(board)
    count = 0
    if mines_dict.count({"x": (x + 1), "y": y}) > 0:
        count += 1
    if mines_dict.count({"x": (x - 1), "y": y}) > 0:
        count += 1
    if mines_dict.count({"x": x, "y": (y + 1)}) > 0:
        count += 1
    if mines_dict.count({"x": x, "y": (y - 1)}) > 0:
        count += 1
    if mines_dict.count({"x": (x + 1), "y": (y + 1)}) > 0:
        count += 1
    if mines_dict.count({"x": (x - 1), "y": (y - 1)}) > 0:
        count += 1
    if mines_dict.count({"x": (x + 1), "y": (y - 1)}) > 0:
        count += 1
    if mines_dict.count({"x": (x - 1), "y": (y + 1)}) > 0:
        count += 1
    return count

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


board = create_board(1)
print(is_mine(board, 3, 3))