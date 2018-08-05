class perfectHash:
    def __init__(self):
        self.size = 8
        self.map = [None] * self.size

    
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def add(self, key, relationship):
        keyHash = self._get_hash(key)
        keyrelationship = [key, relationship]
        
        if self.map[keyHash] is None:
            self.map[keyHash] = list([keyrelationship])
            return True
        else:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    pair[1] = relationship
                    return True
            self.map[keyHash].append(keyrelationship)
            return True
    
    def get(self, key):
        keyHash = self._get_hash(key)
        if self.map[keyHash] is not None:
            for pair in self.map[keyHash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        keyHash = slef._get_hash(key)
        
        if self.map[keyHash] is None:
            return False
        for i in range (0, len(self.map[keyHash])):
            if self.map[keyHash][i][0] == key:
                self.map[keyHash].pop(i)
                return True
    
    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

family = perfectHash()
family.add('Bryan', 'dad')
family.add('Michele', 'mom')
family.add('Sam', 'sister')
family.add('Josh', 'brother-in-law')
family.add('Mike', 'grandfather')
family.add('Christy', 'grandmother')
family.add('Chloe', 'wife')
family.add('Clara', 'sister-in-law')
family.add('Jana', 'Mother-in-law')
family.add('Carl', 'Father-in-law')
family.print()
        