class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # I don't think we need this but I want to make sure len(A)-1>0
        if len(A) < 3:
            return True
        # two passes?
        return (all(A[i] <= A[i + 1] for i in range(len(A) - 1))) or (all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

        """
        # also try one pass:
        def cmp(a, b):
            return (a > b) - (a < b)
        temp=0

        for i in range(len(A)-1):
            c = cmp(A[i],A[i+1])
            if c:
                if temp !=0 and c!= temp:
                    return False
                temp=c
        return True

        """



