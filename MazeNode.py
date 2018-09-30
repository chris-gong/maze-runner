class MazeNode():
    def __init__(self,loc,g,h):
        self.g = g
        self.h = h
        self.f = g + h
        self.loc = loc
        self.valid = True
    def __lt__(self,other):
        return self.f < other.f
    
    def set_invalid(self):
        self.valid = False
    def is_valid(self):
        return self.valid