
class Point:
	def __init__(x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		# otherwise
		return False

class Maze:
	def __init__(self, start_pt, final_pt, map):
		self.start_pt = start_pt
		self.final_pt = final_pt
		self.map = map
		self.visited = {}

	def isOutside(self, pt):
		if pt == final_pt:
			return True
		return False

	def getStartPosition(self):
		return self.start_pt

	def isOutside(self, pt):
		return self.final_pt == pt

	def wallExists(self, pt, dir):
		if dir == 'NORTH':
			new_pt = Point(start_point.x, start_point.y - 1)
		if dir == 'SOUTH':
			new_pt = Point(start_point.x, start_point.y + 1)
		if dir == 'EAST':
			new_pt = Point(start_point.x + 1, start_point.y)
		if dir == 'WEST':
			new_pt = Point(start_point.x - 1, start_point.y)
		return start_point

	def markSquare(self, pt):
		self.visited[pt] = True

	def unmarkSquare(self, pt):
		self.visited[pt] = False

	def isMarked(self, pt):
		if pt not in self.visited:
			return False
		return self.visited[pt]

def adjacentPoint(start_point, dir):
	if dir == 'NORTH':
		return Point(start_point.x, start_point.y - 1)
	if dir == 'SOUTH':
		return Point(start_point.x, start_point.y + 1)
	if dir == 'EAST':
		return Point(start_point.x + 1, start_point.y)
	if dir == 'WEST':
		return Point(start_point.x - 1, start_point.y)
	return start_point

dir_list = ['NORTH', 'WEST', 'SOUTH', 'EAST']
def solveMaze(maze, start_point):
	if maze.isOutside(start_point):
		return True
	elif maze.isMarked(start_point):
		return False
	maze.markSquare(start_point)
	for dir in dir_list:
		if not maze.wallExists(start_point, dir):
			if solveMaze(maze, adjacentPoint(start_point, dir)):
				return True
	maze.unmarkSquare(start_point)
	return False
