class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        current_num = 0
        current_string = ""
        for c in s:
            if c == '[':
                stack.append(current_string)
                stack.append(current_num)
                current_string = ""
                current_num = 0
            elif c == "]":
                num = stack.pop()
                previous_string = stack.pop()
                current_string = previous_string + num * current_string
            # Eg: 2 continuous numbers
            elif c.isdigit():
                current_num = current_num * 10 + int(c)
            else:
                current_string += c
        return current_string

