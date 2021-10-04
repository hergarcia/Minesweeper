from unittest import TestCase
from random import randint
from board import convert_board_to_2d, get_initial_parameters, generate_board_1d, create_board, is_mine, get_all_the_mines, get_mines_around

class Test(TestCase):
    def test_get_initial_parameters(self):
        # given
        level = 2

        # when
        res = get_initial_parameters(level)

        # verify
        self.assertEqual(res, (141, 27, 10, 40))

    def test_get_initial_parameters_wrong_level(self):
        # given
        level = -15

        # when
        res = get_initial_parameters(level)

        # verify
        self.assertIsNone(res)

    def test_generate_board_1d(self):
        # given
        level = 2
        (time, width, long, mines) = get_initial_parameters(level)
        size = int(width * long)

        # when
        res = generate_board_1d(size, mines)

        # verify
        self.assertEqual(mines, res.count(True))
        self.assertEqual(size - mines, res.count(False))
        self.assertEqual(size, len(res))

    def test_convert_board_to_2d_l2(self):
        # given
        board_1d = [True, False]

        # when
        res = convert_board_to_2d(board_1d, 1)

        # verify
        self.assertEqual(res, [[True], [False]])

    def test_convert_board_to_2d_l8(self):
        # given
        board_1d = [True, False, True, False, False, True, False, True]

        # when
        res = convert_board_to_2d(board_1d, 2)

        # verify
        self.assertEqual(res, [[True, False], [True, False], [False, True], [False, True]])

    def test_create_board(self):
        # given
        level = 3
        (time, width, long, mines) = get_initial_parameters(level)

        # when
        board = create_board(level)

        # verify
        self.assertEqual(width, len(board))
        mines_count = 0
        for row in board:
            self.assertEqual(long, len(row))
            mines_count += row.count(True)
        self.assertEqual(mines, mines_count)

    def test_is_mine(self):
        # given
        x = 1
        y = 2
        board_2d = [[True, False], [True, False], [False, True], [False, True]]

        # when
        res = is_mine(board_2d, x, y)

        # verify
        self.assertEqual(res, {'mina': True, 'lista': [{'x': 0, 'y': 0}, {'x': 0, 'y': 1},{'x': 1, 'y': 2}, {'x': 1, 'y': 3}], 'numero': 0})

    def test_is_mine2(self):
        # given
        x = 2
        y = 2
        board_2d = [[True, False], [True, False], [False, True], [False, True]]

        # when
        res = is_mine(board_2d, x, y)

        # verify
        self.assertIsNone(res)

    def test_get_all_the_mines(self):
        # given
        level = randint(1, 10)
        (time, width, long, mines) = get_initial_parameters(level)
        board_2d = [[True, False, False], [False, True, False], [False, True, True], [True, False, True], [False, False, False]]

        # when
        board = create_board(level)
        res = get_all_the_mines(board_2d)
        res2 = get_all_the_mines(board)

        # verify
        self.assertEqual(res, [{'x': 0, 'y': 0}, {'x': 1, 'y': 1},{'x': 1, 'y': 2}, {'x': 2, 'y': 2}, {'x': 0, 'y': 3}, {'x': 2, 'y': 3}])
        self.assertEqual(len(res2), mines)

    def test_get_all_the_mines_False(self):
        # given
        board_2d_False = [[False, False], [False, False], [False, False], [False, False], [False, False]]

        # when
        resF = get_all_the_mines(board_2d_False)

        # verify
        self.assertEqual(resF, [])


    def test_get_mines_around(self):
        # given
        level = randint(1, 10)
        x = 1
        y = 0

        # when
        board_2d = [[True, False, False], [False, True, False], [False, True, True], [True, False, True], [False, False, False]]
        res = get_mines_around(board_2d, x, y)

        # verify
        self.assertEqual(res, 2)


    def test_get_mines_around2(self):
        # given
        level = randint(1, 10)
        (time, width, long, mines) = get_initial_parameters(level)
        x = randint(0, long)
        y = randint(0, width)

        # when
        board = create_board(level)
        res = get_mines_around(board, x, y)

        # verify
        self.assertIsNotNone(res)
        self.assertIn(res, range(0, 8))