class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        # we start with ( and find ) inside
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if stack:
                    print(stack)
                    top = stack.pop()
                    print(top)
                    print(stack)

                else:
                    top = None


                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        if len(stack)==0:
            return True
        else:
            return False





model = Solution()
print(model.isValid(s="([{}])"))