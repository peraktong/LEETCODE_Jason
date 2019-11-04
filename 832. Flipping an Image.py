class Solution(object):
    def flipAndInvertImage(self, A):
        Re = []
        for row in A:
            print([x ^ 1 for x in row[::-1]])
            Re.append([x ^ 1 for x in row[::-1]])


        return Re

A = [[1,1,0],[1,0,1],[0,0,0]]
model = Solution()
print(model.flipAndInvertImage(A= A))