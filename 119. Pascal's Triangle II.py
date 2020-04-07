class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        cur = [1]
        if rowIndex == 0:
            return ans
        for i in range(rowIndex + 1):
            ans = [1] * (i + 1)
            if i > 1:
                for j in range(1, len(ans) - 1):
                    ans[j] = cur[j - 1] + cur[j]
                cur = ans
            else:
                cur = ans
        return ans


