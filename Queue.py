class myQueue:
    def __init__(self):
        self.queue = list()

    def addtoq(self,dataval):
    # Insert method to add element
        self.queue.insert(0,dataval)
        return True

    def size(self):
        return len(self.queue)

    def removeUserFromQueue(self, user):
        pos = self.queue.index(user)
        return self.queue.pop(pos)

    # Pop method to remove element
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
    
    def peek(self, id):
        return self.queue.index(id)
