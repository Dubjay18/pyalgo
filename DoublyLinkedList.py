class Node:
    data = None
    next_node = None
    previous_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s>' % self.data

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == 0
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        if self.head:
            self.head.previous_node = new_node
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self,data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1
            prev = current
            next_node = current.next_node
            prev.next_node = new
            new.next_node = next_node
            new.previous_node = prev
            next_node.previous_node = new
    
    def remove(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.previous_node:
                    current.previous_node.next_node = current.next_node
                    if current.next_node:
                        current.next_node.previous_node = current.previous_node
                else:
                    self.head = current.next_node
                    if current.next_node:
                        current.next_node.previous_node = None
                return True
            else:
                current = current.next_node
        return False

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)
            current = current.next_node
        return '-> '.join(nodes)



d = DoublyLinkedList()
d.add(1)
d.add(2)
d.add(3)
d.add(4)
d.add(5)
print(d)