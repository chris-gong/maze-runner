from random import randint
from copy import deepcopy
from MazeRunner import MazeRunner

class SimulatedAnnealing():
    
    def __init__(self,runner,search_function,*args):
        self.runner = runner
        if not self.start_maze(search_function,*args):
            pass # Error no solvable maze generated in 100 trials with func
        self.original_maze = self.runner.maze
        self.generate_harder_maze()
        
    def start_maze(self,search_function,*args):
        solution = None
        trials = 0
        nodes_expanded = 0
        while(solution is not None):
            solution,nodes_expanded = search_function(*args)
            self.runner.generate_maze()
            trials += 1
            if trials is 100 and solution is None:
                    return False
        self.current_state = (runner.maze,nodes_expanded)
        return True
        
    def temperature_schedule(self):
        pass

    def generate_neighbors(self):
        maze = self.current_state[0]
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
                        neighbors.append(new_maze)
            else:
                pass
        if neighbors is []:
            return None
        else:
            return neighbors
        
    def generate_harder_maze(self):
        while(True):
            neighbors = self.generate_neighbors()
            return

if __name__ == '__main__':
    runner = MazeRunner(20,.2)
    simulated_annealing = SimulatedAnnealing(runner,runner.a_star,runner.get_euclid_dist)
    
                