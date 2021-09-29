from unittest import TestCase

from board import convert_board_to_2d, get_initial_parameters, generate_board_1d, create_board


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



