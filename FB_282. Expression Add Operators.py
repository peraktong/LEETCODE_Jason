# GG
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # DFS from sicheng
        if not num:
            return []
        self.inp, self.target, self.res = num, target, []
        self.dfs(num[0], 1, 0, int(num[0]), 1, True)
        return self.res

    def dfs(self, expr, i, val, multi1, multi2, isMulti1):
        if i == len(self.inp):
            if val + multi1 * multi2 == self.target:
                self.res.append(expr)
            return
        n = int(self.inp[i])
        self.dfs(expr + "*" + self.inp[i], i + 1, val, multi1 * multi2, n, False)
        self.dfs(expr + "+" + self.inp[i], i + 1, val + multi1 * multi2, n, 1, True)
        self.dfs(expr + "-" + self.inp[i], i + 1, val + multi1 * multi2, n, -1, True)

        if isMulti1:
            if multi1 != 0:
                self.dfs(expr + self.inp[i], i + 1, val, multi1 * 10 + n, multi2, True)
        else:
            if multi2 != 0:
                self.dfs(expr + self.inp[i], i + 1, val, multi1, multi2 * 10 + n, False)
        return
