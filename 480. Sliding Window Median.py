class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # bisect in python: O(n*k)
        # start with edge case
        if not nums:
            return None
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k // 2] + window[-(k // 2) - 1]) / 2.)
            window.remove(a)
            bisect.insort(window, b)

        return medians



