class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1
        # Here the su means cumulative sum:
        # If su-k in count, which is the count for element x, we add one to this cumulative value
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su - k]
            count[su] += 1
        return ans
