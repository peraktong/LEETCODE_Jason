class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # I will use two pointer:
        ans = []
        start, stop = 0, 0
        # start stop for index in A and B
        while start < len(A) and stop < len(B):
            low = max(A[start][0], B[stop][0])
            high = min(A[start][1], B[stop][1])
            if low <= high:
                # is intersection
                ans.append([low, high])
            if A[start][1] < B[stop][1]:
                # This means A[start] can only insect in B[stop], and we can checkk A[start+1]
                start += 1
            else:
                stop += 1
        return ans

