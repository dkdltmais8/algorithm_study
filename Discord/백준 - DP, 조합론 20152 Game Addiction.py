N, H = map(int,input().split())
if N>H:
    a,b = 0,N-H
else:
    a,b = 0,H-N
dp = [[0]*(b+1) for _ in range(b+1)]
for i in range(b+1):
    for j in range(b+1):
        if i<j:continue
        if i == b:
            dp[i][j] = 1
        elif j == 0:
            dp[i][j] = 1
for i in range(a,b+1):
    for j in range(a,b+1):
        if i<j:
            continue
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
print(dp[-1][-1]-1)
