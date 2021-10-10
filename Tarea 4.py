from board import create_board, get_mines_around, get_initial_parameters


def discover_clear_cells1(board, x, y, visited=[]):
    num = get_mines_around(board, x, y)
    (time, width, long, mines) = get_initial_parameters(1)
    if x >= 0 and x <= long:
        if num == 0:

            resultado.append({
                "x": x,
                "y": y,
                "numero": num
            })
            x += 1
            return discover_clear_cells1(board, x, y, visited=[])
        else:
            resultado.append({
            "x": x,
            "y": y,
            "numero": num
            })
        return resultado
    else:
        return resultado

def discover_clear_cells2(board, x, y, visited=[]):
    num = get_mines_around(board, x, y)
    (time, width, long, mines) = get_initial_parameters(1)
    if x >= 0 and x <= long:
        if num == 0:

            resultado.append({
                "x": x,
                "y": y,
                "numero": num
            })
            x -= 1
            return discover_clear_cells2(board, x, y, visited=[])
        else:
            resultado.append({
            "x": x,
            "y": y,
            "numero": num
            })
        return resultado
    else:
        return resultado


def discover_clear_cells3(board, x, y, visited=[]):
    num = get_mines_around(board, x, y)
    (time, width, long, mines) = get_initial_parameters(1)
    if y >= 0 and y <= width:
        if num == 0:

            resultado.append({
                "x": x,
                "y": y,
                "numero": num
            })
            y += 1
            return discover_clear_cells3(board, x, y, visited=[])
        else:
            resultado.append({
            "x": x,
            "y": y,
            "numero": num
            })
        return resultado
    else:
        return resultado

def discover_clear_cells4(board, x, y, visited=[]):
    num = get_mines_around(board, x, y)
    (time, width, long, mines) = get_initial_parameters(1)
    if y >= 0 and y <= width:
        if num == 0:

            resultado.append({
                "x": x,
                "y": y,
                "numero": num
            })
            y -= 1
            return discover_clear_cells4(board, x, y, visited=[])
        else:
            resultado.append({
                "x": x,
                "y": y,
                "numero": num
            })
        return resultado
    else:
        return resultado

def discover_clear_cells(board, x, y, visited=[]):
    # disc1 = discover_clear_cells1(board, x, y, visited=[])
    # disc2 = discover_clear_cells2(board, x, y, visited=[])
    # disc3 = discover_clear_cells3(board, x, y, visited=[])
    # disc4 = discover_clear_cells4(board, x, y, visited=[])
    resultado_total = discover_clear_cells1(board, x, y, visited=[]).append(discover_clear_cells2(board, x, y, visited=[]))
    return resultado_total


resultado = []
board = create_board(1)
print(discover_clear_cells1(board, 2, 5, visited=[]))