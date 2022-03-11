n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    if i == 0:
        for j in range(1,m):
            dp[i][j] = dp[i][j-1]+arr[i][j]
    for j in range(1):
        dp[i][j] = dp[i-1][j]+arr[i][j]
for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = max(dp[i - 1][j] + arr[i][j], dp[i][j - 1] + arr[i][j], dp[i - 1][j - 1] + arr[i][j])

print(dp[-1][-1])
