import numpy as np

class Board:
    def __init__(self):
        self.boardstate = np.zeros((3,3))

    def print_state(self):
        print(self.boardstate)




#%%
import numpy as np
print(np.zeros((3,3), dtype=int))
