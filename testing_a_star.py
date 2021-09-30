#%%
from EightPuzzle import BoardNode
from AStarSearch import AStar

#%% Board States
b1 = [[0,1,2],[3,4,5],[6,7,8]]
b2 = [[1,0,2],[3,4,5],[6,7,8]]
b3 = [[1,4,2],[3,0,5],[6,7,8]]

#%%
b = BoardNode(b3, None, None, 0)
search = AStar(b, 'h1')
search.a_star()

#%%
b_hard = BoardNode(b1, None, None, 0)
b_hard.randomize_state(30)
b_hard.print_state()
search = AStar(b_hard, 'h2')
search.a_star()