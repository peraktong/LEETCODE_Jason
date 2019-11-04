import random
class Solution:

    def __init__(self, nums: List[int]):
        # hash table
        self.table = {}
        for i in range(len(nums)):
            # print(self.table)
            if nums[i] in self.table.keys():
                self.table[nums[i]].append(i)
            else:
                self.table[nums[i]] = [i]

    def pick(self, target: int) -> int:

        ans = self.table[target]
        u = random.randint(0, len(ans) - 1)
        return ans[u]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)