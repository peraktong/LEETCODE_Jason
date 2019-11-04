class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(i, s):
            count = 0
            if s[i] == s[i + 1]:
                count += 1
                start = i
                stop = i + 1
                while start > 0 and stop < len(s) - 1:
                    start -= 1
                    stop += 1
                    if s[start] == s[stop]:
                        count += 1
                    else:
                        break

            count += 1
            start = stop = i
            while start > 0 and stop < len(s) - 1:
                start -= 1
                stop += 1
                if s[start] == s[stop]:
                    count += 1
                else:
                    break

            return count

        ans = 0
        for k in range(len(s) - 1):
            ans += helper(k, s)
        ans += 1

        return ans






