class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # hash table
        # nlogn
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i = 0
        N = len(num)
        while i <= N - 1 - i:
            if (num[i], num[N - 1 - i]) not in maps:
                return False
            i += 1
        return True


