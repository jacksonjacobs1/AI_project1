from EightPuzzle import BoardNode
import numpy as np
from queue import PriorityQueue


class AStar:
    # --------INIT--------- #
    def __init__(self, game_node: BoardNode):
        self.node = game_node
        self.frontier = PriorityQueue()
        self.frontier.put((0, self.node))
        self.reached
        self.moves = []

    # ---------- GETTERS AND SETTERS ----------- #
    def get_node(self):
        return self.node

    def get_frontier(self):
        return self.fronterier

    def get_reached(self):
        return self.reached

    def get_moves(self):
        return self.moves

    # ---------- GENERAL METHODS ----------- #
    def f(self, h: str):
        """
        f(state) = g(state) + h(state)
        :param h: the heuristic function to use
        :return: the path_cost plus the heuristic
        """
        node = self.get_node()
        state = node.get_node_state()
        return node.get_path_cost() + (node.h1(state) if h == 'h1' else node.h2(state))

    def expand(self, node: BoardNode):
        """

        :return: an array of node children of the current state, ordered by their evaluation functions.
        """
        directions = node.valid_directions()
        child_states = []
        for d in directions:
            new_state = node.move(node.get_node_state(), node.find_blank(), d)
            child_states.append(BoardNode(new_state, node, d, node.get_path_cost() + 1))
