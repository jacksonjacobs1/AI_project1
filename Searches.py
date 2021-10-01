from EightPuzzle import BoardNode
import numpy as np
from queue import PriorityQueue
from itertools import count

class Iterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.current = None
    def __next__(self):
        try:
            self.current = next(self.iterator)
        except StopIteration:
            self.current = None
        finally:
            return self.current

class AStar:
    # --------INIT--------- #
    def __init__(self, game_node: BoardNode, h, max_nodes):
        self.unique = Iterator(count)   # different from self.state_count because it also increments for some revisited nodes
        self.maxNodes = max_nodes

        self.h = h
        self.node = game_node
        self.frontier = PriorityQueue()
        self.frontier.put((self.node.f(self.h), next(self.unique), self.node))
        self.reached = {}
        key = self.node.get_node_state().flatten().tostring()
        self.reached[key] = game_node
        self.moves = []

        self.state_count = 1    # only the root node has been reached

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

    def get_max_nodes(self):
        return self.maxNodes

    def get_unique(self):
        return self.unique

    # ---------- GENERAL METHODS ----------- #

    def solve_a_star(self):
        print('initial board state: ')
        self.get_node().print_state()
        while self.get_frontier().not_empty:
            if self.get_max_nodes() <= self.get_unique().current:
                raise IndexError('max nodes reached.')
            node: BoardNode = self.get_frontier().get()[2]
            self.append_move(node.get_action())
            if node.is_goal():
                print('solved!')
                print(f'list of moves: {self.get_moves()}')
                print(f'number of moves: {len(self.get_moves())}')
                node.print_state()
                return node
            children = expand(node)
            for child in children:
                s = child.get_node_state()
                key = s.flatten().tostring()
                matched_child = self.get_reached().get(key)
                if matched_child is None:   # count the number of distinct states reached.
                    self.state_count += 1
                if matched_child is None or (matched_child.get_path_cost() > child.get_path_cost()):
                    self.get_reached()[key] = child
                    self.get_frontier().put((child.f(self.h), next(self.unique), child))
        print(self.get_moves())
        print(len(self.get_moves()))
        return None


def expand(node: BoardNode) -> [BoardNode]:
    """

    :return: an array of node children of the current state.
    """
    directions = node.valid_directions()
    child_nodes = []
    for d in directions:
        new_state = node.move(node.get_node_state(), node.find_blank(), d)
        new_node = BoardNode(new_state, node, d, node.get_path_cost() + 1)
        child_nodes.append(new_node)
    return child_nodes


class LocalBeam:
    # ----------INIT----------- #
    def __init__(self, game_node: BoardNode, k, max_nodes):
        self.unique = Iterator(count)
        self.maxNodes = max_nodes

        self.root = game_node
        self.beams = []
        self.moves = []     # filled with arrays that contain the logged moves of their respective beam.
        self.all_children = PriorityQueue()

        for i in range(k):  # for each beam
            beam = BoardNode(game_node.get_node_state().copy(), parent=None, action=None, path_cost=0) # initialize each beam
            logged_moves = beam.randomize_state(10, reset_state=False)     # branch beam state
            self.moves.append(logged_moves)         # for beam state i, log its moves away from the root.
            self.beams.append(beam)        # append beam to beams array

    # ----------GETTERS AND SETTERS---------- #
    def get_beams(self):
        return self.beams

    def get_moves(self):
        return self.moves

    def get_root(self):
        return self.root

    def get_all_children(self):
        return self.all_children

    def get_max_nodes(self):
        return self.maxNodes

    def get_unique(self):
        return self.unique

    # ----------GENERAL METHODS------------ #
    def solve_beam(self):

        root = self.get_root()
        print('initial board state: ')
        root.print_state()
        if root.is_goal():                      # checks whether root state was already solved
            print('Puzzle was already solved!')
            return root

        while True:     # Main iteration of local beam search.
            if self.get_max_nodes() <= self.get_unique().current:
                raise IndexError('max nodes reached.')
            for i in range(len(self.beams)):    # for each beam runs sequentially, not in parallel.
                beam_children = expand(self.get_beams()[i])
                for child in beam_children:
                    if child.is_goal():             # checks for the goal state being reached.
                        print('solved!')
                        print(f'list of moves: {self.get_moves()[i]}')
                        print(f'number of moves: {len(self.get_moves())[i]}')
                        child.print_state()
                        return child
                    self.get_all_children().put((child.f('h2'), next(self.unique), i, child))    # place each child in the priority queue.
            for i in range(len(self.beams)):   # for each beam
                best_child_entry = self.get_all_children().get()   # pop best child

                best_child = best_child_entry[3]
                parent_move_log = self.get_moves()[best_child_entry[2]].copy()
                this_action = best_child.get_action()
                child_move_log = parent_move_log
                child_move_log.append(this_action)

                self.get_beams()[i] = best_child      # set beam equal to best child
                self.get_moves()[i] = child_move_log

