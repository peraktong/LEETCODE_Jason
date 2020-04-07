from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        # similar to task manager:

        ans = []
        # you can replace counter with your own dictionary code
        c = Counter(S)
        pq = [(-value, k) for k, value in c.items()]
        heapq.heapify(pq)
        pa, pb = 0, ""
        while pq:
            a, b = heapq.heappop(pq)
            ans += [b]
            # This means p_a still have count since we use -key
            if pa < 0:
                heapq.heappush(pq, (pa, pb))
            a += 1
            pa, pb = a, b
        ans = "".join(ans)
        if len(ans) != len(S):
            return ""
        return ans
