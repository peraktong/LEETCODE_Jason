import random


class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val):
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val):
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        t = len(self.set) - 1
        list_set = list(self.set)
        return list_set[random.randint(0, t)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()