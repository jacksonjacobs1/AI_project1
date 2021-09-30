from EightPuzzle import BoardNode
import numpy as np
from queue import PriorityQueue
from itertools import count


class AStar:
    # --------INIT--------- #
    def __init__(self, game_node: BoardNode, h):
        self.unique = count()

        self.h = h
        self.node = game_node
        self.frontier = PriorityQueue()
        self.frontier.put((self.node.f(self.h), next(self.unique), self.node))
        self.reached = {}
        key = self.node.get_node_state().flatten().tostring()
        self.reached[key] = game_node
        self.moves = []

    # ---------- GETTERS AND SETTERS ----------- #
    def get_node(self):
        return self.node

    def get_frontier(self):
        return self.frontier

    def get_reached(self):
        return self.reached

    def get_moves(self):
        return self.moves

    def append_move(self, move):
        self.moves.append(move)

    def is_reached(self, node: BoardNode):
        key = node.get_node_state().flatten().tostring()
        if self.get_reached().get(key) is not None:
            return True

    # ---------- GENERAL METHODS ----------- #

    def a_star(self):
        while self.get_frontier().not_empty:
            node: BoardNode = self.get_frontier().get()[2]
            self.append_move(node.get_action())
            if node.is_goal():
                print(self.get_moves())
                print(len(self.get_moves()))
                print('solved!')
                node.print_state()
                return node
            children = self.expand(node)
            for child in children:
                s = child.get_node_state()
                key = s.flatten().tostring()
                matched_child = self.get_reached().get(key)
                if matched_child is None or (matched_child.get_path_cost() > child.get_path_cost()):
                    self.get_reached()[key] = child
                    self.get_frontier().put((child.f(self.h), next(self.unique), child))
        print(self.get_moves())
        print(len(self.get_moves()))
        return None

    @staticmethod
    def expand(node: BoardNode):
        """

        :return: an array of node children of the current state.
        """
        directions = node.valid_directions()
        child_states = []
        for d in directions:
            new_state = node.move(node.get_node_state(), node.find_blank(), d)
            new_node = BoardNode(new_state, node, d, node.get_path_cost() + 1)
            child_states.append(new_node)

        return child_states
