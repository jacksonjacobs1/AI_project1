from EightPuzzle import BoardNode
from Searches import AStar, LocalBeam
import numpy as np

np.random.seed(2021)
# --------------TESTING A*------------- #
b1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
b2 = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
b3 = [[1, 4, 2], [3, 0, 5], [6, 7, 8]]

b = BoardNode(b3, None, None, 0)
search = AStar(b, 'h1')
search.solve_a_star()

b_hard = BoardNode(b1, None, None, 0)
b_hard.randomize_state(30)
b_hard.print_state()
search = AStar(b_hard, 'h2')
search.solve_a_star()

# --------------TESTING LOCAL BEAM---------------- #
np.random.seed(2021)

b = BoardNode(b3, None, None, 0)
b.randomize_state(n=20)
search = LocalBeam(b, 10, 100000)
search.solve_beam()
