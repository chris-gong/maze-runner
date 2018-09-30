import matplotlib.pyplot as plt
import numpy as np

class MazeGenerator():
    """MazeRunner"""
    def __init__(self, dim):
        self.dim = dim

    def generate_maze(self,prob):
        new_maze = Maze(self.dim,prob)
        return new_maze

class Maze():
    """MAAAZZE"""
    def __init__(self,dim,prob):
        self.grid = np.random.choice(a=[True, False], size=(dim, dim), p=[prob, 1-prob])
        self.grid[0][0] = False
        self.grid[dim-1][dim-1] = False
        self.dim = dim

    def render_maze(self):
        plt.imshow(self.grid, cmap='Greys',  interpolation='nearest')
        plt.show()

        
if __name__ == '__main__':
    dimension = int(input("What is the demnsion of the maze?\n"))
    percent = float(input("What is the percentage a tile is blocked?\n"))
    mymaze = Maze(dimension,percent)
    mymaze.render_maze()