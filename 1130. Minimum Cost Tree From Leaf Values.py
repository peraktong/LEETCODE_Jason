class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # GREEDY

        ans = 0
        while len(arr) > 1:
            mini_index = arr.index(min(arr))
            if 0 < mini_index < len(arr) - 1:
                ans += min(arr[mini_index - 1], arr[mini_index + 1]) * arr[mini_index]
            else:
                ans += arr[1 if mini_index == 0 else mini_index - 1] * arr[mini_index]
            arr.pop(mini_index)
        return ans







