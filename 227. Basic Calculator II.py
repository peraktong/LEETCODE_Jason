class Solution:
    def calculate(self, s: str) -> int:
        # only return int part:

        # use stack
        # proOp is the sign before num
        # use stack
        if not s:
            return "0"
        s += '+0'
        stack, num, preOp = [], 0, "+"
        # num remember the value between two operational signs
        for i in range(len(s)):
            if s[i].isdigit():
                # Eg: 23: num=2 for "3"
                num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if preOp == "-":
                    stack.append(-num)
                elif preOp == "+":
                    stack.append(num)
                elif preOp == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                # Here preOp means the operational signs before numbers
                preOp, num = s[i], 0
        return sum(stack)





