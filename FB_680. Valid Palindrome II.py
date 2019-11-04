class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                m1, m2 = s[left:right], s[left + 1:right + 1]
                return m1 == m1[::-1] or m2 == m2[::-1]
            left += 1
            right -= 1
        return True



