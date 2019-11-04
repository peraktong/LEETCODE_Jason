class Solution:
    def simplifyPath(self, path: str) -> str:

        commands = [c for c in path.split("/") if c != "." and c != ""]
        stack = []
        for c in commands:
            if c == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        return "/" + "/".join(stack)

