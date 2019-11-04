def matrixScore(A):
    R,C = len(A),len(A[0])
    ans = 0
    for c in range(C):
        col = 0
        for r in range(R):
            col+=A[r][c]^A[r][0]
            print(col)

        ans += max(col, R - col) * 2 ** (C - 1 - c)
    print(ans)

    return ans

A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# bitshift: 1<<5=32
matrixScore(A=A)
# https://www.programiz.com/python-programming/operators
# print(3|1,3^1)=3,2
