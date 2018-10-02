import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, fabs

class Maze():
    """MAAAZZE"""
    def __init__(self, dim, prob):
        self.grid = np.random.choice(
                        a=[True, False],
                        size=(dim, dim),
                        p=[prob, 1-prob])
        self.grid[0][0] = False
        self.grid[dim-1][dim-1] = False
        self.dim = dim
        self.prob = prob

    def render_maze(self):
        plt.imshow(self.grid, cmap='Greys',  interpolation='nearest')
        plt.show()

    def euclid_dist(self, loc):
        a = (self.dim-1-loc[0])**2
        b = (self.dim-1-loc[1])**2
        return sqrt(a+b)

    def manhatten_dist(self, loc):
        a = fabs(self.dim-1-loc[0])
        b = fabs(self.dim-1-loc[1])
        return a + b


if __name__ == '__main__':
    dimension = int(input("What is the demnsion of the maze?\n"))
    percent = float(input("What is the percentage a tile is blocked?\n"))
    mymaze = Maze(dimension, percent)
    print(mymaze.manhat_dist100
          ((2, 3)))
    mymaze.render_maze()
