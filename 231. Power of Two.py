def isPowerOfTwo(n):
    if n == 1:
        return True
    ans = list(bin(n)[2:])
    print(ans)
    print(ans.count(str(1)))


    if ans.count(str(1))==1 and ans[0]==str(1):
        return True
    else:
        return False


print(isPowerOfTwo(n=2))
n=4
print(n > 0 and not (n & n-1))
# bitwise
# print((n & n-1))