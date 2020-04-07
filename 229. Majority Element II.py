class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        data = {}
        ans = set([])
        threshold = int(len(nums) / 3)
        for n in nums:
            data[n] = data.get(n, 0) + 1
            if data[n] > threshold:
                ans.add(n)
        return ans



