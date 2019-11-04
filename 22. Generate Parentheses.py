# time/space complexity: A(2n,n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.ans = []

        # A good parenthesis means the number of "(" before ")" must be bigger than 0
        # backtracking:
        def helper(S="", left=0, right=0):
            if len(S) == 2 * n:
                self.ans.append(S)
                return
            if left < n:
                helper(S + "(", left + 1, right)
            if right < left:
                helper(S + ")", left, right + 1)

        helper()
        return self.ans




