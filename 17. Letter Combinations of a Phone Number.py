class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking:
        ans = []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtracking(combination, next_digits):
            if len(next_digits) == 0:
                ans.append(combination)
            else:
                for l in phone[next_digits[0]]:
                    backtracking(combination + l, next_digits[1:])

        if digits:
            backtracking("", digits)
        return ans


