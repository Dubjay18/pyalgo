# with linked list
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s>' % self.data


class Stack_with_linked_list:
    def __init__(self):
        self.top = None
        self.size = 0
        self.bottom = None
    
    def peek(self):
        return self.top.data
    
    def push(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next_node = self.top
            self.top = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next_node
            self.size -= 1
            return temp.data
    
    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        current = self.top
        string = ''
        while current:
            string += str(current.data) + ' -> '
            current = current.next_node
        return string


stack = Stack_with_linked_list()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())


class Stack_with_array:
    def __init__(self):
        self.stack = []
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        return self.stack.pop()
    
    def push(self, data):
        self.stack.append(data)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

    def __repr__(self):
        return ' -> '.join(map(str, self.stack))


stack = Stack_with_array()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())