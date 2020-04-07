class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # recursive:
        ans = []

        def helper(temp, val):
            if val == target:
                temp.sort()
                if temp in ans:
                    pass
                else:
                    ans.append(temp)

                return

            elif val > target:
                return
            else:
                for c in candidates:
                    helper(temp + [c], val + c)

        helper([], 0)
        return ans


