class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return self.root
        current_node = self.root
        prev = None
        while current_node:
            if current_node.value < new_node.value:
                prev = current_node
                right = current_node.right
                current_node = right
                
            else:
                prev = current_node
                left = current_node.left
                current_node = left
        if prev.value <  new_node.value:
            prev.right = new_node
        else:
            prev.left = new_node

    
    def search(self,value):
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return current_node
            elif current_node.value < value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None

    def delete(self,value):
        current_node = self.root
        prev = None
        while current_node:
            if current_node.value == value:
                break
            elif current_node.value < value:
                prev = current_node
                current_node = current_node.right
            else:
                prev = current_node
                current_node = current_node.left
        if current_node == None:
            return None
        if current_node.left == None and current_node.right == None:
            if prev.value < current_node.value:
                prev.right = None
            else:
                prev.left = None
        elif current_node.left == None:
            if prev.value < current_node.value:
                prev.right = current_node.right
            else:
                prev.left = current_node.right
        elif current_node.right == None:
            if prev.value < current_node.value:
                prev.right = current_node.left
            else:
                prev.left = current_node.left
        else:
            temp = current_node.right
            prev = current_node
            while temp.left:
                prev = temp
                temp = temp.left
            current_node.value = temp.value
            if prev.value < temp.value:
                prev.right = temp.right
            else:
                prev.left = temp.right
        return current_node
    
    def __repr__(self):
        return repr(self.root)



bin = BinarySearchTree()
bin.insert(12)
bin.insert(90)
bin.insert(76)
bin.insert(9)
bin.insert(7)
bin.insert(120)
bin.insert(130)
bin.insert(110)

print(bin)
        

        