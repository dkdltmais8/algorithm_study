import sys
input = sys.stdin.readline
n, k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,n+1):
    wt,wm,ct,cm = map(int,input().split())
    if i == 1:
        dp[i][wt] = wm
        # wt, ct가 같은 경우를 대비
        dp[i][ct] = max(dp[i][ct],cm)
    else:
        for j in range(k+1):
            if dp[i-1][j] == 0:
                continue
            else:
                if j+wt<=k:
                    dp[i][j+wt] = max(dp[i][j+wt],dp[i-1][j]+wm)
                if j+ct<=k:
                    dp[i][j+ct] = max(dp[i][j+ct],dp[i-1][j]+cm)

print(max(dp[-1]))