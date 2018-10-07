from random import randint
from copy import deepcopy
from MazeRunner import MazeRunner
from math import exp

class SimulatedAnnealing():
    
    def __init__(self,runner,search_function,*args):
        self.temp = 100
        self.runner = runner
        self.search_function = search_function
        if not self.start_maze(search_function,*args):
            return None # Error no solvable maze generated in 100 trials with func
        original_maze = self.current_state[0]
        self.generate_harder_maze(*args)
        self.runner.maze = self.current_state[0]
        print("Intiial Maze")
        print ("NODES EXPANDED INITIALLY = " + str(self.original_nodes_expanded))
        original_maze.render_maze()
        print("Final Maze")
        self.current_state[0].render_maze()
        solution,nodes_expanded = search_function(*args)
        print ("NODES EXPANDED FINAL = " + str(nodes_expanded))
        
        
    def set_current_state(self,new_state):
        self.runner.maze = new_state[0]
        self.current_state = new_state
        
    def start_maze(self,search_function,*args):
        solution = None
        trials = 0
        nodes_expanded = 0
        while(True):
            solution,nodes_expanded = search_function(*args)
            if(solution is not None):
                self.original_nodes_expanded = nodes_expanded
                self.set_current_state((runner.maze,nodes_expanded))
                return True
            self.runner.generate_maze()
            trials += 1
            if trials is 1000:
                return False
        return True
        
    def temperature(self, obj_change, prob, k):
        prob_of_acceptance = 1 / (1 + exp(((obj_change+1)/self.temp)))
        print("prob_of_acceptance"+str(prob_of_acceptance))
        if prob_of_acceptance > prob:
            self.temp = self.temp * pow(0.95, k)
            return True
        else:
            return False

    def generate_neighbors(self):
        maze = self.current_state[0]
        neighbors = []
        dim = self.runner.dim
        while(True):
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
            if neighbors is not []:
                return neighbors

    def generate_harder_maze(self,*args):
        num_restarts = 15
        while(True):
            original_maze = self.current_state[0]
            neighbors = self.generate_neighbors()
            best_neighbor = None
            for neighbor in neighbors:
                self.runner.maze = neighbor
                solution,nodes_expanded = self.search_function(*args)
                if solution is None:
                    continue
                if(best_neighbor is None or nodes_expanded > best_neighbor[1]):
                    best_neighbor = (neighbor,nodes_expanded)
            
            if best_neighbor is None: #all neighbors are unsolvable
                if num_restarts is not 0:
                    continue
                else:
                    return
                num_restarts -= 1
            else:
                if best_neighbor[1] > self.current_state[1]:
                    self.set_current_state(best_neighbor)
                else:
                    temp_check = self.temperature(self.current_state[1] - best_neighbor[1], 0.48, 3)
                    print("temp_check="+str(temp_check))
                    print(self.current_state[1] - best_neighbor[1])
                    if temp_check:
                        self.set_current_state(best_neighbor)
                    else:
                        return
        
        return
if __name__ == '__main__':
    runner = MazeRunner(25,.3)
    simulated_annealing = SimulatedAnnealing(runner,runner.a_star,runner.get_euclid_dist)
    #simulated_annealing = SimulatedAnnealing(runner,runner.dfs)
    pass
    
    
