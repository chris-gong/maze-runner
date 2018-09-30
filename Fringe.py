class StackFringe:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack) == 0
    def pop(self):
        return self.stack.pop()
    def push(self,loc):
        if loc in self.stack:
            return
        else:
            return self.stack.append(loc)
    
class QueueFringe:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self,loc):
        return self.queue.insert(0,loc)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

class HeapFringe: