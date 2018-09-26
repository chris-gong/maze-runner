import random
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

class MazeGenerator():
	"""MazeRunner"""
	def __init__(self, dim):
		self.arg = arg

class Maze():
	"""MAAAZZE"""
	def __init__(self,dim,prob):
		self.grid = np.random.choice(a=[True, False], size=(dim, dim), p=[prob, 1-prob])
		self.grid[0][0] = False
		self.grid[dim-1][dim-1] = False


		cmap = colors.ListedColormap(['white','black'])
		plt.imshow(self.grid, cmap='Greys',  interpolation='nearest')
		plt.show()


	
def isBlocked(p):
	return (random.random()<p)
		
if __name__ == '__main__':
	mymaze = Maze(50,1)