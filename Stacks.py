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
