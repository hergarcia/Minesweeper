from board import create_board, get_mines_around, get_initial_parameters


def discover_clear_cells(board, x, y, visited=[]):
    num = get_mines_around(board, x, y)
    (time, width, long, mines) = get_initial_parameters(1)
    if x < long:
        if num == 0:

            resultado.append({
                "x": x,
                "y": y,
                "numero": num
            })
            x += 1
            return discover_clear_cells(board, x, y, visited=[])
        else:
            resultado.append({
            "x": x,
            "y": y,
            "numero": num
            })
        return resultado
    else:
        return resultado

resultado = []
board = create_board(1)
print(discover_clear_cells(board, 0, 0, visited=[]))