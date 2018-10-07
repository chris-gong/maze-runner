from random import randint
from copy import deepcopy

class SimulatedAnnealing():
    
    def __init__(self,runner,search_function,*args):
        self.runner = runner
        if not self.start_maze():
            pass # Error no solvable maze generated in 100 trials with func
        self.original_maze = self.maze_runner.maze
        self.generate_harder_maze()
        
    def start_maze(self,search_function,*args):
        solution = None
        trials = 0
        while(solution is not None):
            solution,nodes_expanded = search_function(*args)
            self.runner.generate_maze()
            trials += 1
            if trials is 100 and solution is None:
                    return False
        self.current_state = (self.original_maze,nodes_expanded)
        return True
        
    def temperature(self, obj_change, prob, k):
        prob_of_acceptance = 1 / (1 + exp((obj_change/self.temp)))
        if prob_of_acceptance > prob:
            self.temp = self.temp * pow(0.95, k)
            return True
        else:
            return False

    
    def generate_neighbors(self,maze):
        neighbors = []
        dim = self.runner.dim
        row_index = randint(0,dim-1)
        for x1 in range(0,dim):
            if maze.grid[row_index][x1]:
                for x2 in range(0,dim):
                    if maze.grid[row_index][x2]:
                        continue
                    else:
                        if((row_index == 0 and x2 == 0) or
                            (row_index == dim-1 and x2 == dim-1)):
                            continue
                        new_maze = deepcopy(maze)
                        new_maze.grid[row_index][x2] = True
                        new_maze.grid[row_index][x1] = False
                        neighbors.append[new_maze]
            else:
                pass
        if neighbors is []:
            return None
        else:
            return neighbors
