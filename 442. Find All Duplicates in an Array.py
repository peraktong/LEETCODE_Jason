class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # since in O(n), we can not sort the array:
        """
        ans ={}
        res = []
        for n in nums:
            ans[n]=ans.get(n,0)+1
        for k,v in ans.items():
            if v==2:
                res.append(k)
        return res

        """
        # hash table
        ans = []
        for n in nums:
            if nums[abs(n) - 1] < 0:
                ans.append(abs(n))
            else:
                nums[abs(n) - 1] *= -1
        return ans


