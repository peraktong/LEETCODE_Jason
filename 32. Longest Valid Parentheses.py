class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use stack to store the index for each bracket. If we remove a set of valid parenthesis,
        # remove these inde

        stack = [(-1,")")]
        ans = 0
        for i, parenthesis in enumerate(s):
            if parenthesis==")" and stack[-1][1]=="(":
                # remove the valid parenthesis
                stack.pop()
                # the ans is the different between index and index +1
                ans = max(ans,i-stack[-1][0])
            else:
                stack+=(i,parenthesis),
        return ans
model = Solution()
print(model.longestValidParentheses(s=")()())"))