n,m = map(int,input().split())
work = sorted(list(map(int,input().split())))
dp = [float('inf') for _ in range(10001)]
visit = [0]*(22222)
dp[0] = 0
visit[0] = 1
for i in range(m):
    visit[work[i]] = 1
    for j in range(i+1,m):
        visit[work[i]+work[j]] = 1
for i in range(1,n):
    if not visit[i]:continue
    for j in range(i,n):
        dp[j] = dp[j] if dp[j]<dp[j-i]+1 else dp[j-i]+1
print(dp[n] if dp[n]!=float('inf') else -1)

