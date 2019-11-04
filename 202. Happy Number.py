class Solution:
    def isHappy(self, n: int) -> bool:
        # use set to memory the number:
        memory = set()
        while n != 1:
            sum_i = sum([int(i) ** 2 for i in str(n)])
            n = sum_i
            if sum_i in memory:
                return False
            memory.add(n)
        else:
            return True

