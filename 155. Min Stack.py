class MinStack:
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        ## Each time we must include the min in each stack
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]



model = MinStack()

model.push(-2)
print(model.q)
model.push(0)
print(model.q)
model.push(-3)
print(model.q)
model.push(-5)
print(model.q)
model.push(-10)
print(model.q)
print(model.getMin())
print(len(model.q))
print(model.top())

