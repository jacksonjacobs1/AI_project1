import unittest
from EightPuzzle import Board


class MyTestCase(unittest.TestCase):

    def test_set_and_get_state(self):
        b = Board()
        b.__setstate__([[1, 1, 1], [1, 1, 1], [1, 1, 1]], blank_spot=None)
        self.assertEqual([[1, 1, 1], [1, 1, 1], [1, 1, 1]], b.__getstate__())

    def test_move(self):
        b = Board()
        b.__setstate__([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 0]], blank_spot=(2, 2))

        # testing valid moves
        new_state, new_blank = b.move(b.__getstate__(), b.get_blank_spot(), 'left')
        b.__setstate__(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 6],
                          [7, 0, 8]], b.__getstate__())

        new_state, new_blank = b.move(b.__getstate__(), b.get_blank_spot(), 'right')
        b.__setstate__(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 0]], b.__getstate__())

        new_state, new_blank = b.move(b.__getstate__(), b.get_blank_spot(), 'up')
        b.__setstate__(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 0],
                          [7, 8, 6]], b.__getstate__())

        new_state, new_blank = b.move(b.__getstate__(), b.get_blank_spot(), 'down')
        b.__setstate__(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 0]], b.__getstate__())

    def test_h1(self):
        self.assertEqual(0, Board.h1([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
        self.assertEqual(1, Board.h1([[1, 0, 2], [3, 4, 5], [6, 7, 8]]))
        self.assertEqual(2, Board.h1([[1, 2, 0], [3, 4, 5], [6, 7, 8]]))

    def test_h2(self):
        self.assertEqual(0, Board.h2([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
        self.assertEqual(1, Board.h2([[1, 0, 2], [3, 4, 5], [6, 7, 8]]))
        self.assertEqual(2, Board.h2([[1, 4, 2], [3, 0, 5], [6, 7, 8]]))

    def test_is_goal(self):
        board = Board()
        board.__setstate__([[0,1,2],[3,4,5],[6,7,8]], (0,0))
        self.assertTrue(board.is_goal())
        board.__setstate__([[1,0,2],[3,4,5],[6,7,8]], (0,1))
        self.assertFalse(board.is_goal())



if __name__ == '__main__':
    unittest.main()
