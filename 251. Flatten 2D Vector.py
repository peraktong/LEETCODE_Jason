class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        ans = []
        for x in v:
            ans.extend(x)
        self.array = ans
        self.i = 0

    def next(self):
        """
        :rtype: int
        """
        self.i += 1
        return self.array[self.i - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.array)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()