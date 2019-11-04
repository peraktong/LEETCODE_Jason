"""
# brutal force:
class Solution:
    def countBits(self, num: int) -> List[int]:
        # brutal force
        ans = [0]
        for i in range(num):
            temp = "{0:b}".format(i + 1)
            ans.append(temp.count("1"))

        return ans



"""

for i in range(10):
    temp = "{0:b}".format(i + 1)
    print(temp.count("1"))
