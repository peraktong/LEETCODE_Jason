class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Let's have a mathematical solution:
        count_t = {}
        for t in tasks:
            count_t[t] = count_t.get(t, 0) + 1

        M = max(count_t.values())
        max_num = 0
        for c in count_t.items():
            if c[1] == M:
                max_num += 1
        ans = max(len(tasks), (M - 1) * (n + 1) + max_num)
        return ans