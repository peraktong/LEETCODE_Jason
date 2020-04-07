# Find the expectation of max continuous head for flipping N coins

import numpy as np
import matplotlib.pyplot as plt


N= np.arange(1000,10000,1000)


def helper(x):
    print("Doing %d"%x)
    N_bootstrap=1000
    ans_all = []
    for i in range(N_bootstrap):
        data = np.random.randint(low=0, high=2, size=x)
        ans = 0
        count = 0
        for i in range(len(data)):
            if data[i] == 0:
                count = 0
            else:
                count += 1
                ans = max(ans, count)
        ans_all.append(ans)
    return np.nanmean(ans_all),np.nanstd(ans_all)/((1000)**0.5)

ans_array = [helper(x) for x in N]

def function(x):
    # loge np(1-p)^x=e
    return np.log2(2*x)-np.log2(np.e)


plt.errorbar(x=N,y=[x[0] for x in ans_array],yerr=[x[1] for x in ans_array],label="simulation")
# offset...
plt.plot(N,[function(x) for x in N],"k",label="formula=%s"%"np.log2(2*x)-np.log2(np.e)")
plt.legend()
plt.show()

# Find the expectation of max continuous head for flipping N coins

# DP METHOD" N^3 but it's a strictly accurate result:
N=10000

dp = [[0]*(N+1) for i in range(N+1)]
dp2 = [[0]*(N+1) for i in range(N+1)]

dp[0][0]=1.0

for n in range(1,N+1):
    for max_l in range(n+1):
        for cur in range(max_l+1):
            dp2[max_l][0]+=0.5*dp[max_l][cur]
        for cur in range(1,max_l):
            dp2[max_l][cur]+=0.5*dp[max_l][cur-1]

        if max_l>0:
            dp2[max_l][max_l]=0.5*dp[max_l][max_l-1]+0.5*dp[max_l-1][max_l-1]
    for i in range(N+1):
        for j in range(N+1):
            dp[i][j]=dp2[i][j]
            dp2[i][j]=0

ans=0
tot=0
for max_l in range(N+1):
    for cur in range(max_l+1):
        ans+=max_l*dp[max_l][cur]
        tot+=dp[max_l][cur]

print(ans)











