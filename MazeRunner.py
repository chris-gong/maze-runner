import MazeGenerator
import Fringe

class MazeRunner():
	def __init__(self):
		pass

	def DFS(self):
		solution = []
		closed = []
		fringe = StackFringe()
		fringe.push((0,0))
		while not fringe.isEmpty():
			currentCoord = fringe.
