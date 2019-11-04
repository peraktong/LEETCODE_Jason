from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Use sliding window:
        # check edge case:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        # Let's put (element,index) from s which is in t into a filter array.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l = r = formed = 0
        window_count = {}
        ans = [float("inf"), None, None]
        # only check char in filter_s to save time:
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_count[character] = window_count.get(character, 0) + 1
            if window_count[character] == dict_t[character]:
                formed += 1
            # if formed==required: remember this in the ans:
            while l <= r and formed == required:
                character = filtered_s[l][1]
                start = filtered_s[l][0]
                end = filtered_s[r][0]
                if end - start + 1 < ans[0]:
                    ans = [end - start + 1, start, end]
                # we use l+=1
                window_count[character] -= 1
                if window_count[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]




