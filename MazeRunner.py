from MazeGenerator import MazeGenerator
from Fringe import StackFringe,QueueFringe

class MazeRunner():
    def __init__(self,maze):
        self.maze = maze
        pass
    
    def isInMaze(self,loc):
        x = loc[0]
        y = loc[1]
        if x < 0 or x >= self.maze.dim:
            return False
        elif y < 0 or y >= self.maze.dim:
            return False
        else:
            return True
    def DFS(self):
        size = self.maze.dim
        goal = (size-1,size-1)
        solution = []
        closed = [[False for x in range(size)] for y in range (size)]
        close[0][0] = True
        fringe = StackFringe()
        fringe.push((0,0))
        move_vectors=[(0,1),(-1,0),(0,-1),(1,0)]
        while not fringe.is_empty():
            cur_loc = fringe.pop()
            if cur_loc == goal:
                # Found solution
                return True
            for move in move_vectors:
                new_loc = tuple(sum(x) for x in zip(cur_loc,move))
                if self.isInMaze(new_loc) and new_loc in closed:
                    fringe.push(new_loc)
            closed.append(cur_loc)
        return False


    

if __name__ == '__main__':
    maze_generator = MazeGenerator(25)
    maze = maze_generator.generate_maze(.25)
    # maze.render_maze()
    runner = MazeRunner(maze)
    print(runner.DFS())




