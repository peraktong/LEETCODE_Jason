class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0
        ans = [1] * n
        ans[0] = 0
        ans[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if ans[i] == 1:
                # This is because this number is i*(i+k*i) and has a factor smaller than the sqrt[n]
                ans[i * i:n:i] = [0] * len(ans[i * i:n:i])
        return sum(ans)



