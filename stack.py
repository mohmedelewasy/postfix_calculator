class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# Simple linked stack
class Stack():
    # constructor can be empty or accept list
    def __init__(self, *args):
        self.top = Node(None, None)
        self.counter = 0
        if len(args) > 0 and type(args[0]) == list:
            for i in args[0]:
                self.push(i)

    def push(self, value):
        new = Node(value, self.top)
        self.top = new
        self.counter += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('there is no element to pop')
        temp = self.top # delete from memory
        self.top = self.top.next
        del(temp)
        self.counter -= 1

    def getTop(self): # get top element without deleting
        if self.isEmpty():
            raise Exception('stack is empty!')
        return self.top.value

    def isEmpty(self):
        return self.top.next == None

    def getLength(self):
        return self.counter