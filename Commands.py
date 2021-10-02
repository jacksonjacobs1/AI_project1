from EightPuzzle import BoardNode
from Searches import AStar, LocalBeam
import numpy as np

np.random.seed(2021)
b1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
b2 = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
b3 = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]

# --------------TESTING A*------------- #
b = BoardNode(b3, parent=None, action=None, path_cost=0)
search = AStar(b, 'h1', max_nodes=10000)
search.solve_a_star()

b_hard = BoardNode(b1, parent=None, action=None, path_cost=0)
b_hard.randomize_state(30)
search = AStar(b_hard, 'h2', max_nodes=10000)
search.solve_a_star()

# --------------TESTING LOCAL BEAM---------------- #
b = BoardNode(b3, None, None, 0)
b.randomize_state(n=20)
search = LocalBeam(b, 10, 10000)
search.solve_beam()
























