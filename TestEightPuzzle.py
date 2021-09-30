import unittest
from EightPuzzle import BoardNode


class MyTestCase(unittest.TestCase):

    def test_set_and_get_state(self):
        b = BoardNode()
        b.set_node_state([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertEqual([[1, 1, 1], [1, 1, 1], [1, 1, 1]], b.get_node_state())

    def test_move(self):
        b = BoardNode()
        b.set_node_state([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 0]])

        # testing valid moves
        new_state = b.move(b.get_node_state(), b.find_blank(), 'left')
        b.set_node_state(new_state)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 6],
                          [7, 0, 8]], b.get_node_state())

        new_state, new_blank = b.move(b.get_node_state(), b.find_blank(), 'right')
        b.set_node_state(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 0]], b.get_node_state())

        new_state, new_blank = b.move(b.get_node_state(), b.find_blank(), 'up')
        b.set_node_state(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 0],
                          [7, 8, 6]], b.get_node_state())

        new_state, new_blank = b.move(b.get_node_state(), b.find_blank(), 'down')
        b.set_node_state(new_state, new_blank)
        self.assertEqual([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 0]], b.get_node_state())

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
        board.set_node_state([[0, 1, 2], [3, 4, 5], [6, 7, 8]], (0, 0))
        self.assertTrue(board.is_goal())
        board.set_node_state([[1, 0, 2], [3, 4, 5], [6, 7, 8]], (0, 1))
        self.assertFalse(board.is_goal())

    def test_find_blank(self):
        b = BoardNode([[1,1,2],[3,4,5],[0,7,8]], parent=None, action=None, path_cost=0)

        self.assertEqual((2,0), b.find_blank())



if __name__ == '__main__':
    unittest.main()
