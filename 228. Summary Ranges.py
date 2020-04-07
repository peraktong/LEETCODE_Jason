class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        temp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == 1 + nums[i - 1]:
                temp.append(nums[i])
            else:
                if len(temp) > 1:
                    ans.append(str(temp[0]) + "->" + str(temp[-1]))
                    temp = [nums[i]]
                else:
                    ans.append(str(temp[0]))
                    temp = [nums[i]]
        if len(temp) > 1:
            ans.append(str(temp[0]) + "->" + str(temp[-1]))

        else:
            ans.append(str(temp[0]))
        return ans


