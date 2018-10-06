import MazeRunner
import random

class SimulatedAnnealing():
    
    def __init__(self,dim,prob,search_function,*args):
        self.runner = MazeRunner(dim,prob)
        solution,nodes_expanded = maze_runner.search_function(*args)
        self.original_maze = self.maze_runner.maze
        while(solution is not None):
            solution = maze_runner.search_function(*args)
            
        
        
    def TemperatureFunction(self):
        pass
    
    def GenerateNeighbors(self,maze):
        neighbors = []
        dim = self.runner.dim
        row_index = random.randint(0,dim-1)
        for x in range(0,dim):
            if maze.grid[row_index][x]