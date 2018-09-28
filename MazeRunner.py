import MazeGenerator
import Fringe

class MazeRunner():
	def __init__(self):
		pass

	def DFS(self):
		goal = (self.maze.dim-1,self.maze.dim-1)
		solution = []
		closed = []
		fringe = StackFringe()
		fringe.push((0,0))
		move_vectors=[(0,1),(-1,0),(0,-1),(1,0)]
		while not fringe.isEmpty():
			cur_loc = fringe.pop()
			if cur_loc == goal:
				# Found solution
				return True
			for move in move_vectors:
				new_loc = tuple(sum(x) for x in zip(cur_loc,move))
				if isInMaze(new_loc) and new_loc in closed:
					fringe.push(new_loc)
			closed.append(cur_loc)
		return False


	def isInMaze(self,loc):
		x = loc[0]
		y = loc[1]
		if x < 0 or x >= self.maze.dim:
			return False
		elif y < 0 or y >= self.maze.dim:
			return False
		else:
			return True



