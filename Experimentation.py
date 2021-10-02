from EightPuzzle import BoardNode
from Searches import AStar, LocalBeam
import numpy as np


def frac_solvable_puzzles(search):
    max_nodes_domain = [1000, 10000, 100000, 1000000]
    frac_solvable_states = np.zeros(len(max_nodes_domain), dtype=float)

    b = BoardNode([[],[],[]], None, None, 0)
    for n in range(len(max_nodes_domain)):
        max_nodes = max_nodes_domain[n]
        exceptions_caught = 0
        for i in range(50):
            b.randomize_state(n=100)

            if search == 'a_star':
                algorithm = AStar(b, 'h1', max_nodes=max_nodes)
                try:
                    algorithm.solve_a_star()
                except IndexError:
                    exceptions_caught += 1
            elif search == 'local_beam':
                algorithm = LocalBeam(b, 10, max_nodes=max_nodes)
                try:
                    algorithm.solve_beam()
                except IndexError:
                    exceptions_caught += 1

        frac_solvable_states[n] = float(50 - exceptions_caught)/float(50)

    return frac_solvable_states


def compare_solvability(max_nodes_lim):
    frac_solvable_states = np.zeros(3)
    b = BoardNode([], None, None, 0)
    max_nodes = max_nodes_lim
    for n in range(3):
        exceptions_caught = 0
        for i in range(50):
            b.randomize_state(100)

            if n == 0:
                algorithm = AStar(b,'h1', max_nodes=max_nodes)
                try:
                    algorithm.solve_a_star()
                except IndexError:
                    exceptions_caught += 1
            elif n == 1:
                algorithm = AStar(b, 'h2', max_nodes=max_nodes)
                try:
                    algorithm.solve_a_star()
                except IndexError:
                    exceptions_caught += 1
            elif n == 3:
                algorithm = LocalBeam(b, 10, max_nodes=max_nodes)
                try:
                    algorithm.solve_beam()
                except IndexError:
                    exceptions_caught += 1
        frac_solvable_states[n] = float(50 - exceptions_caught)/float(50)
    return frac_solvable_states

def h1_vs_h2():
    num_moves = dict(h1=[], h2=[])

    b = BoardNode([], None, None, 0)
    for h in ['h1', 'h2']:
        for i in range(50):
            b.randomize_state(n=20)
            search = AStar(b, h, max_nodes=100000)
            search.solve_a_star()
            num_moves[h].append(len(search.get_moves()))

    return np.mean(num_moves['h1']), np.mean(num_moves['h2'])


def var_sol_length():
    num_moves = dict(h1=[], h2=[], beam=[])

    b = BoardNode([], None, None, 0)
    for mode in ['h1', 'h2', 'beam']:
        for i in range(50):
            b.randomize_state(n=20)
            if mode == 'h1' or mode == 'h2':
                search = AStar(b, mode, max_nodes=100000)
                search.solve_a_star()
                num_moves[mode].append(len(search.get_moves()))
            elif mode == 'beam':
                search = LocalBeam(b, 10, 100000)
                search.solve_beam()
                num_moves[mode].append(len(search.get_moves()[0]))

    h1_var = np.std(num_moves['h1'])
    h2_var = np.std(num_moves['h2'])
    beam_var = np.std(num_moves['beam'])

    return h1_var, h2_var, beam_var
