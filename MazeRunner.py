from MazeGenerator import MazeGenerator
from Fringe import StackFringe,QueueFringe,HeapFringe
from MazeNode import MazeNode
import numpy as np
import matplotlib.pyplot as plt
class MazeRunner():
    def __init__(self,maze):
        self.maze = maze
        pass
    def get_euclid_dist(self,loc):
        return self.maze.euclid_dist(loc)
        
    def get_manhatten_dist(self,loc):
        return self.maze.manhatten_dist(loc)
        
    def is_in_maze(self,loc):
        x = loc[0]
        y = loc[1]
        if x < 0 or x >= self.maze.dim:
            return False
        elif y < 0 or y >= self.maze.dim:
            return False
        else:
            return True
    def dfs(self):
        size = self.maze.dim
        goal = (size-1,size-1)
        path = {}
        closed = [[False for x in range(size)] for y in range (size)]
        solution = []
        fringe = StackFringe()
        fringe.push((0,0))
        closed[0][0]=True
        move_vectors=[(0,-1),(-1,0),(0,1),(1,0)]
        path_found = False
        while not fringe.is_empty():
            cur_loc = fringe.pop()
            print(cur_loc)
            if cur_loc == goal:
                path_found = True
                break
            for move in move_vectors:
                new_loc = tuple(sum(x) for x in zip(cur_loc,move))
                x = new_loc[0]
                y = new_loc[1]
                if self.is_in_maze(new_loc) and (not self.maze.grid[x][y]) and (not closed[x][y]):
                    fringe.push(new_loc)
                    path[new_loc] = cur_loc
                    closed[new_loc[0]][new_loc[1]] = True
            # closed.append(cur_loc)
        if not path_found:
            return None
        cur_loc = goal
        print("SOLUTION:")
        while(cur_loc != (0,0)):
            solution.append(cur_loc)
            cur_loc = path[cur_loc]
        solution.append((0,0))
        solution.reverse()
        return solution
    def bfs(self):
        size = self.maze.dim
        goal = (size-1,size-1)
        path = {}
        closed = [[False for x in range(size)] for y in range (size)]
        solution = []
        fringe = QueueFringe()
        fringe.enqueue((0,0))
        closed[0][0]=True
        move_vectors=[(0,-1),(-1,0),(0,1),(1,0)]
        path_found = False
        while not fringe.is_empty():
            cur_loc = fringe.dequeue()
            print(cur_loc)
            if cur_loc == goal:
                path_found = True
                break
            for move in move_vectors:
                new_loc = tuple(sum(x) for x in zip(cur_loc,move))
                x = new_loc[0]
                y = new_loc[1]
                if self.is_in_maze(new_loc) and (not self.maze.grid[x][y]) and (not closed[x][y]):
                    fringe.enqueue(new_loc)
                    path[new_loc] = cur_loc
                    closed[new_loc[0]][new_loc[1]] = True
            # closed.append(cur_loc)
        if not path_found:
            return None
        cur_loc = goal
        print("SOLUTION:")
        while(cur_loc != (0,0)):
            solution.append(cur_loc)
            cur_loc = path[cur_loc]
        solution.append((0,0))
        solution.reverse()
        return solution
    def a_star(self,heuristic):
        size = self.maze.dim
        goal = (size-1,size-1)
        path = {}
        closed = [[False for x in range(size)] for y in range (size)]
        solution = []
        fringe = HeapFringe()
        print("HEURISTIC (0,0)")
        print(heuristic((0,0)))
        initial_node = MazeNode((0,0),0,heuristic((0,0)))
        fringe.add_node(initial_node)
        closed[0][0]=True
        move_vectors=[(0,-1),(-1,0),(0,1),(1,0)]
        path_found = False
        while not fringe.is_empty():
            cur_node = fringe.get_min_node()
            if cur_node == None:
                break
            print(cur_node.loc)
            if cur_node.loc == goal:
                path_found = True
                break
            for move in move_vectors:
                new_loc = tuple(sum(x) for x in zip(cur_node.loc,move))
                x = new_loc[0]
                y = new_loc[1]
                if self.is_in_maze(new_loc) and (not self.maze.grid[x][y]) and (not closed[x][y]):
                    new_node = MazeNode((new_loc),cur_node.g+1,heuristic(new_loc))
                    if not new_loc in fringe.node_lookup:
                        fringe.add_node(new_node)
                        path[new_loc] = cur_node.loc
                    else:
                        old_value = fringe.node_lookup[new_loc].f
                        new_value = new_node.f
                        if old_value > new_value:
                            fringe.update_node(new_node)
                    
                            
            closed[cur_node.loc[0]][cur_node.loc[1]]=True
        if not path_found:
            return None
        cur_loc = goal
        print("SOLUTION:")
        while(cur_loc != (0,0)):
            solution.append(cur_loc)
            cur_loc = path[cur_loc]
        solution.append((0,0))
        solution.reverse()
        return solution
        
    def render_solution(self,solution):
        solution_map = np.zeros((self.maze.dim,self.maze.dim),dtype=bool)
        for loc in solution:
            solution_map[loc[0]][loc[1]] = True
        plt.imshow(solution_map, cmap='Greys',  interpolation='nearest')
        plt.show()
if __name__ == '__main__':
    maze_generator = MazeGenerator(25)
    maze = maze_generator.generate_maze(.35)
    runner = MazeRunner(maze)
    solutions=[]
    solutions.append(runner.bfs())
    solutions.append(runner.dfs())
    solutions.append(runner.a_star(runner.get_euclid_dist))
    solutions.append(runner.a_star(runner.get_manhatten_dist))
    maze.render_maze()
    for solution in solutions:
        if solution != None:
            runner.render_solution(solution)




