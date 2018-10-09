from random import randint, getrandbits
from copy import deepcopy
from MazeRunner import MazeRunner
from math import exp


class SimulatedAnnealing():

    def __init__(self, runner):
        self.temp = 100
        self.runner = runner
        if not self.start_maze():
            return None  # Error no solvable maze generated in 1000 trys

    class MazeState():
        def __init__(self, maze, search_prop):
            self.maze = maze
            self.solution = search_prop[0]
            if self.solution is None:
                self.solution_length = 0
            else:
                self.solution_length = len(self.solution)
            self.nodes_expanded = search_prop[1]
            self.max_fringe_size = search_prop[2]

        def __str__(self):
            return ("solution length: %d\
                    nodes expanded: %d\
                    max fringe size: %d\
                    " % (self.solution_length,
                         self.nodes_expanded, self.max_fringe_size))

    def generate_state(self, search_function, *args):
        search_prop = search_function(*args)
        new_state = self.MazeState(self.runner.maze, search_prop)
        return new_state

    def set_current_state(self, state):
        self.runner.maze = state.maze
        self.current_state = state

    def start_maze(self):
        trials = 0
        while(True):
            search_prop = self.runner.a_star(self.runner.get_manhatten_dist)
            if(search_prop[0] is not None):
                self.original_maze = self.runner.maze
                return True
            self.runner.generate_maze()
            trials += 1
            if trials is 1000:
                return False
        return True

    def reset_maze(self):
        self.runner.maze = self.original_maze

    def temperature(self, obj_change, prob, k):
        prob_of_acceptance = 1 / (1 + exp(((obj_change+1)/self.temp)))
        print("prob_of_acceptance: "+str(prob_of_acceptance))
        if prob_of_acceptance > prob:
            self.temp = self.temp * pow(0.95, k)
            return True
        else:
            return False

    def generate_neighbors(self):
        maze = self.current_state.maze
        neighbors = []
        dim = self.runner.dim
        while(True):
            row_bool = bool(getrandbits(1))
            if(row_bool):
                row_index = randint(0, dim-1)
                for x1 in range(0, dim):
                    if maze.grid[row_index][x1]:
                        for x2 in range(0, dim):
                            if maze.grid[row_index][x2]:
                                continue
                            else:
                                if((row_index == 0 and x2 == 0) or
                                   (row_index == dim-1 and x2 == dim-1)):
                                    continue
                                new_maze = deepcopy(maze)
                                new_maze.grid[row_index][x2] = True
                                new_maze.grid[row_index][x1] = False
                                neighbors.append(new_maze)
                if neighbors is not []:
                    return neighbors
            else:
                col_index = randint(0, dim-1)
                for x1 in range(0, ):
                    if maze.grid[x1][col_index]:
                        for x2 in range(0, dim):
                            if maze.grid[x2][col_index]:
                                continue
                            else:
                                if((col_index == 0 and x2 == 0) or
                                   (col_index == dim-1 and x2 == dim-1)):
                                    continue
                                new_maze = deepcopy(maze)
                                new_maze.grid[x2][col_index] = True
                                new_maze.grid[x1][col_index] = False
                                neighbors.append(new_maze)
                if neighbors is not []:
                    return neighbors

    def generate_harder_maze(self, prop, search_function, *args):
        self.reset_maze
        self.set_current_state(self.generate_state(search_function, *args))
        self.original_state = self.current_state
        num_restarts = 15

        def cmp_solution_length(state1, state2):
            return (state1.solution_length-state2.solution_length)

        def cmp_nodes_expanded(state1, state2):
            return (state1.nodes_expanded-state2.nodes_expanded)

        def cmp_max_fringe_size(state1, state2):
            return (state1.max_fringe_size-state2.max_fringe_size)
        prop_switch = {
                "solution_length": cmp_solution_length,
                "nodes_expanded": cmp_nodes_expanded,
                "max_fringe_size": cmp_max_fringe_size
                }
        prop_cmp = prop_switch.get(prop)
        while(True):
            neighbors = self.generate_neighbors()
            best_neighbor_state = None
            for neighbor in neighbors:
                self.runner.maze = neighbor
                neighbor_state = self.generate_state(search_function, *args)
                if neighbor_state.solution is None:
                    continue
                if(best_neighbor_state is None
                   or prop_cmp(neighbor_state, best_neighbor_state) > 0):
                    best_neighbor_state = neighbor_state
            if best_neighbor_state is None:  # all neighbors are unsolvable
                if num_restarts is not 0:
                    num_restarts -= 1
                    continue
                else:
                    return
            else:  # neighbors have solution
                if prop_cmp(best_neighbor_state, self.current_state) > 0:
                    self.set_current_state(best_neighbor_state)
                else:
                    temp_check = self.temperature(-prop_cmp(
                                                           best_neighbor_state,
                                                           self.current_state),
                                                  0.48, 2)
                    print(prop_cmp(best_neighbor_state, self.current_state))
                    if temp_check:
                        self.set_current_state(best_neighbor_state)
                    else:
                        return
        return


if __name__ == '__main__':
    runner = MazeRunner(30, .3)
    # simulated_annealing = SimulatedAnnealing(runner,runner.a_star,
    #                                          runner.get_euclid_dist)
    simulated_annealing = SimulatedAnnealing(runner)
    simulated_annealing.generate_harder_maze(
            "nodes_expanded",
            runner.a_star, runner.get_manhatten_dist)
    print(str(simulated_annealing.original_state))
    print(str(simulated_annealing.current_state))
    simulated_annealing.original_maze.render_maze()
    runner.render_solution(simulated_annealing.original_state.solution)
    simulated_annealing.current_state.maze.render_maze()
    runner.render_solution(simulated_annealing.current_state.solution)
