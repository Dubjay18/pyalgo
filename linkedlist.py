class Node:
    data = None
    next_node = None
    
    def __init__(self,data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s" % self.data
    
class linked:
 
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count= 0
        
        while current:
            count+=1
            current = current.next_node
            
        return count
    
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def insert(self,data,index):
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1:
                current = new.next_node
                position -= 1
            
            prev = current
            next = current.next_node
            
            
                
            
    def __repr__(self):
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        return '->'.join(nodes)

l = linked()
i = 0

for i in range(0,9):
    l.add(i)
    i+=1
    
print(l)