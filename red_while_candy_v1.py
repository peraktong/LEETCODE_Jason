# r 90
# w 10
# eat if red
# eat second pick if first is while
# probability last pick is white
dp = [[0]*11 for i in range(0,91)]

for w in range(1,11):
    # no red left, all while
    # dp[r][0]=0
    dp[0][w]=1


for r in range(1,91):
    for w in range(1,11):
        # red: eat it so r=r-1
        # while, put back so w=w and each second so second...
        dp[r][w]=r/(r+w)*dp[r-1][w]+(w/(r+w))*\
                 (r/(r+w)*dp[r-1][w]+(w)/(r+w)*dp[r][w-1])
print(dp[90][10])