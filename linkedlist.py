class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '<Node data: %s>' % self.data


class Linked_list:

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
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            prev = current
            next_node = current.next_node

            prev.next_node = new
            new.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current
        
    def reverse(self):
        current = self.head
        prev_node = None
        next_node = None

        while current:
            next_node = current.next_node
            current.next_node = prev_node
            prev_node = current
            current = next_node

        self.head = prev_node

    def getMiddle(self):
        arr = []
      
        if self.head is not None:
            middleIdx = self.size() // 2
            return self.node_at_index(middleIdx).data
        return None

    def are_Identical(self, list):
        a = self.head
        b = list.head
        while a != None and b != None:
            if a.data != b.data:
                return False
            a = a.next_node
            b = b.next_node
        return True


    def node_at_index(self, index):

        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position+=1

            return current
    def move_last_to_first(self):
        tail = self.head
        current = self.head
        while current and self.size() > 1:
            if current.next_node.next_node is None:
                tail = current.next_node
                current.next_node = None
                
            current = current.next_node

        return self.add(tail.data)


    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '->'.join(nodes)


l = Linked_list()
l.add(10)
l.add(21)
l.add(4)
l2 = Linked_list()
l2.add(10)
l2.add(21)
l2.add(4)
print(l2)
print(l)
print(l.are_Identical(l2))
print(l.move_last_to_first())
print(l)