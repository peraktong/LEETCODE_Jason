class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return False
        # brutal force: NlogN?
        return sorted(nums)[len(nums) - k]
