class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        ans = []

        def dfs(s, path, ans):
            if not s:
                ans.append(path[:])
                return
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, ans)
                    # find the element for s[i:], pop the result
                    path.pop()

        dfs(s, [], ans)
        return ans

