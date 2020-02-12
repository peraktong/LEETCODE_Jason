class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return None
        a,b,c = len(A),len(A[0]),len(B[0])
        ans = [[0 for i in range(c)] for j in range(a)]
        # sparse matrix
        for i,row in enumerate(A):
            for k,va in enumerate(row):
                if va:
                    for j,vb in enumerate(B[k]):
                        ans[i][j]+=va*vb
        return ans