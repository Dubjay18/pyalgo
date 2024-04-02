class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first.data
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            self.length -= 1
            return temp.data
    
    def is_empty(self):
        return self.length == 0

    def __repr__(self):
        current = self.first
        string = ''
        while current:
            string += str(current.data) + ' -> '
            current = current.next
        return string

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)

class CrazyQueues:
    def __init__(self):
        self.first = []
        self.last = []

    def push(self, x):
        while self.first:
            self.last.append(self.first.pop())
        self.first.append(x)
        while self.last:
            self.first.append(self.last.pop())

        

    def pop(self):
        return self.first.pop()

    def peek(self):
        return self.first[-1]

    def empty(self):
        return not self.first

    def __repr__(self):
        return str(self.first)



crazy = CrazyQueues()
crazy.push(1)
crazy.push(2)
crazy.push(3)
print(crazy)
print(crazy.peek())
print(crazy.pop())
print(crazy)
print(crazy.peek())
print(crazy.pop())
print(crazy.peek())
