class StackFringe:
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return len(self.stack) == 0
    def pop(self):
        if(self.isEmpty):
            return None
        else:
            return self.stack.pop()
    def push(self,loc):
        if loc in self.stack:
            return
        else:
            return self.stack.append(loc)
    
class QueueFringe:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        if self.IsEmpty():
            return None
        else:
            return self.queue.pop()
