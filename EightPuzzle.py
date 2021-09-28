import numpy
import numpy as np
import pandas as pd
import math

class Board:
    def __init__(self):
        self.boardstate = np.zeros((3,3), dtype=int)
        self.blank_spot = (0,0)

    def __setstate__(self, state, blank_spot):
        self.boardstate = state
        self.blank_spot = blank_spot

    def __getstate__(self):
        return self.boardstate

    def get_blank_spot(self):
        return self.blank_spot

    def print_state(self):
        state = pd.DataFrame(self.__getstate__())
        print(state)

    def valid_directions(self):
        blank_spot = self.get_blank_spot()
        output = []

        if blank_spot[1] > 0:
            output.append('left')
        if blank_spot[1] < 2:
            output.append('right')
        if blank_spot[0] > 0:
            output.append('up')
        if blank_spot[0] < 2:
            output.append('down')

        return output

    def randomize_state(self, n):
        self.__setstate__([[0,1,2],[3,4,5],[6,7,8]], blank_spot=(0,0))
        for i in range(n):
            direction_list = self.valid_directions()
            direction = direction_list[np.random.randint(len(direction_list))]
            new_state, new_blank = self.move(self.__getstate__(), self.get_blank_spot(), direction)
            self.__setstate__(new_state, new_blank)

    @staticmethod
    def move(state, blank_spot, direction):
        """
        Shifts the blank tile (represented by a zero) in the specified direction.
        This method assumes the direction is valid. It is up to the methods that use "move" to select valid moves.

        :param state: the state to be manipulated
        :param blank_spot: the blank coordinates of that board
        :param direction: the direction to shift in
        :return: the manipulated board
        """
        blank_row = blank_spot[0]
        blank_col = blank_spot[1]
        state_copy = np.array(state, copy=True)

        if direction == 'left':
            temp = state_copy[blank_row][blank_col - 1]
            state_copy[blank_row][blank_col - 1] = 0
            state_copy[blank_row][blank_col] = temp
            new_blank = (blank_row, blank_col - 1)

        elif direction == 'right':
            temp = state_copy[blank_row][blank_col + 1]
            state_copy[blank_row][blank_col + 1] = 0
            state_copy[blank_row][blank_col] = temp
            new_blank = (blank_row, blank_col + 1)

        elif direction == 'up':
            temp = state_copy[blank_row - 1][blank_col]
            state_copy[blank_row - 1][blank_col] = 0
            state_copy[blank_row][blank_col] = temp
            new_blank = (blank_row - 1, blank_col)
        elif direction == 'down':
            temp = state_copy[blank_row + 1][blank_col]
            state_copy[blank_row + 1][blank_col] = 0
            state_copy[blank_row][blank_col] = temp
            new_blank = (blank_row + 1, blank_col)
        else:
            raise NameError("Unaccepted input. Try 'up', 'down', 'left', or 'right.")

        return state_copy, new_blank

    @staticmethod
    def h1(state):
        """
        function calculates the h1 heuristic by counting the number of out-of-place tiles
        :param state: The board state we would like to find a heuristic for
        :return: The heuristic value. Should be a value from 0-8
        """
        counter = 0
        arr = np.array(state).flatten()
        for i in range(len(arr)):
            if arr[i] != 0:
                if arr[i] != i:
                    counter += 1

        return counter

    @staticmethod
    def h2(state):
        output_sum = 0

        for row in range(len(state)):
            for col in range(len(state[0])):
                elem = state[row][col]

                y_dist = np.abs(row - int(math.floor(elem/3)))
                x_dist = np.abs(col - elem%3)

                if elem != 0:
                    output_sum += (y_dist + x_dist)
        return output_sum

