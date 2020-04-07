class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        # BFS
        def helper(cur, res):
            # print(cur,res)

            if sum(cur) > n or len(cur) > k:
                return
            if sum(cur) == n and len(cur) == k:
                ans.append(cur)
                return
            for r in res:
                # from small to big!
                helper(cur + [r], set([i for i in range(r + 1, 10)]))

        helper(cur=[], res=set([k for k in range(1, 10)]))
        return ans

