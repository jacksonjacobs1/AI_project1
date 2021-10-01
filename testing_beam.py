#%%
from EightPuzzle import BoardNode
from Searches import LocalBeam
import numpy as np

#%%
b1 = [[0,1,2],[3,4,5],[6,7,8]]      # already the solved state
b2 = [[1,0,2],[3,4,5],[6,7,8]]      # one move away from the goal state
b3 = [[1,4,2],[3,0,5],[6,7,8]]      # two moves away from the goal state

#%%
np.random.seed(2021)

b = BoardNode(b3, None, None, 0)
b.randomize_state(n=20)
search = LocalBeam(b, 10, 100000)
search.solve_beam()