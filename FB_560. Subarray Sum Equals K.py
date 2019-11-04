class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        # Here the current means cumulative sum:
        # If current-k in count, which is the count for element x, we add one to this cumulative value

        ans = 0
        current = 0
        for x in nums:
            current += x
            ans += count.get(current - k, 0)
            # This means we find it at current value, and we add +1: subarray
            count[current] = count.get(current, 0) + 1

        return ans

