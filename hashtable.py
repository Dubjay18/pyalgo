class HashTable:
    def __init__(self,size):
         self.data = [0 for _ in range(size)]

    def _hash(self,key):
        hash = 0
        for char in key:
            hash = (hash + ord(char)) % len(self.data)

        return hash

    def set(self,key,value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key,value])
        return self.data

    def get(self,key):
        address = self._hash(key)
        if self.data[address]:
            for i in range(len(self.data[address])
                if self.data[address][i][0] = key
                    return self.data[address][i][1]
        return None
    def keys(self):
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i]:
                keysArray.append(self.data[i][0][0])
        return keysArray
    

    #usage
    hastab = HashTable(50)
    print(hastab.set("jay",100)
    print(hastab.get("jay"))
    print(hastab.keys())
    


            
        
