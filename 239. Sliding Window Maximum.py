class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # bisect in python: O(n*k)
        # start with edge case

        """
        if not nums:
            return None
        window = sorted(nums[:k])
        ans = []
        for a, b in zip(nums, nums[k:] + [0]):
            ans.append(window[-1])
            window.remove(a)
            bisect.insort(window, b)

        return ans


        """

        if not nums:
            return []
        ans = []
        pq = []
        # iterate through nums
        for i, num in enumerate(nums):
            heapq.heappush(pq, (-num, i))
            if i >= k:
                # remove elements which are already out of window
                while pq and pq[0][1] <= i - k:
                    heapq.heappop(pq)

            if i >= k - 1:
                ans.append(-pq[0][0])

        return ans
