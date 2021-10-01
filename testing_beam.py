#%%
from EightPuzzle import BoardNode
from Searches import LocalBeam

#%%
b1 = [[0,1,2],[3,4,5],[6,7,8]]
b2 = [[1,0,2],[3,4,5],[6,7,8]]
b3 = [[1,4,2],[3,0,5],[6,7,8]]

#%%
b = BoardNode(b3, None, None, 0)
b.randomize_state(n=20)
search = LocalBeam(b, 10, 10000)
search.solve_beam()