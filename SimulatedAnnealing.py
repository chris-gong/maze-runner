import MazeRunner
import random
from copy import deepcopy

class SimulatedAnnealing():
    
    def __init__(self,dim,prob,search_function,*args):
        runner = MazeRunner(dim,prob)
        self.original_maze = self.maze_runner.maze
        solution = None
        while(solution is not None):
            solution,nodes_expanded = runner.search_function(*args)
            runner.generate_maze()
        
            
            
            
        
        
    def TemperatureFunction(self):
        pass
    
    def GenerateNeighbors(self,maze):
        neighbors = []
        dim = self.runner.dim
        row_index = random.randint(0,dim-1)
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