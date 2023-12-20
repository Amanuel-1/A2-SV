class RandomizedSet:

    def __init__(self):
        self.data = set()
        self.randr =[]
        self.ind=0
        

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.add(val)
        self.randr = list(self.data)

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        self.data.remove(val)
        self.randr = list(self.data)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.randr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()