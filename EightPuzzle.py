import numpy as np

class Board:
    def __init__(self):
        self.boardstate = np.zeros((3,3))

    def print_state(self):
        for i in range(0, 9, 3):
            print(self.boardstate[i: i+3])




#%%
import numpy as np
print(np.zeros((3,3), dtype=int))
