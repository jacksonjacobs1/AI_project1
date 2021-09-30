import numpy
import numpy as np
import pandas as pd
import math


class BoardNode:
    # ---------INIT---------- #
    def __init__(self, node_state, parent, action, path_cost):
        self.node_state = np.array(node_state)
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    # ---------GETTERS AND SETTERS---------- #
    def set_node_state(self, node_state):
        """
        :param node_state: a two-dimensional python array
        :return: None
        """
        self.node_state = np.array(node_state)

    def get_node_state(self):
        return self.node_state

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_path_cost(self):
        return self.path_cost

    # ---------GENERAL METHODS-------------- #
    def print_state(self):
        state = pd.DataFrame(self.get_node_state())
        print(state)

    def find_blank(self):
        state = self.get_node_state()
        for r in range(state.shape[0]):
            for c in range(state.shape[1]):
                if state[r][c] == 0:
                    return r, c

    def valid_directions(self):
        blank_spot = self.find_blank()
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
        self.set_node_state([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        for i in range(n):
            direction_list = self.valid_directions()
            direction = direction_list[np.random.randint(len(direction_list))]
            new_state = self.move(self.get_node_state(), self.find_blank(), direction)
            self.set_node_state(new_state)

    def is_goal(self):
        state = self.get_node_state().flatten()
        for i in range(len(state)):
            if state[i] != i:
                return False
        return True

    @staticmethod  # might eventually make these static methods non-static
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
        state_copy = np.array(state, copy=True)  # this makes a new object instead of referencing the address.

        if direction == 'left':
            temp = state_copy[blank_row][blank_col - 1]
            state_copy[blank_row][blank_col - 1] = 0
            state_copy[blank_row][blank_col] = temp

        elif direction == 'right':
            temp = state_copy[blank_row][blank_col + 1]
            state_copy[blank_row][blank_col + 1] = 0
            state_copy[blank_row][blank_col] = temp

        elif direction == 'up':
            temp = state_copy[blank_row - 1][blank_col]
            state_copy[blank_row - 1][blank_col] = 0
            state_copy[blank_row][blank_col] = temp

        elif direction == 'down':
            temp = state_copy[blank_row + 1][blank_col]
            state_copy[blank_row + 1][blank_col] = 0
            state_copy[blank_row][blank_col] = temp

        else:
            raise NameError("Unaccepted input. Try 'up', 'down', 'left', or 'right.")

        return state_copy

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
        """
        Implementation of the h2 heuristic that sums up the manhattan distances of each tile from its correct place
        :param state:
        :return:
        """
        output_sum = 0

        for row in range(len(state)):
            for col in range(len(state[0])):
                elem = state[row][col]

                y_dist = np.abs(row - int(math.floor(elem / 3)))
                x_dist = np.abs(col - elem % 3)

                if elem != 0:
                    output_sum += (y_dist + x_dist)
        return output_sum
