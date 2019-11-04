class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        carry = 0
        res = []
        while len(num1) > 0 or len(num2) > 0:
            m1 = ord(num1.pop()) - ord("0") if len(num1) > 0 else 0
            m2 = ord(num2.pop()) - ord("0") if len(num2) > 0 else 0
            carry_temp = carry + m1 + m2
            res.append(carry_temp % 10)
            carry = carry_temp // 10
        if carry:
            res.append(carry)
        return "".join([str(c) for c in res[::-1]])



