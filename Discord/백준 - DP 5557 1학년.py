n = int(input())
lst = list(map(int,input().split()))
dp = [[0]*21 for _ in range(n-1)]
dp[0][lst[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0<=j+lst[i]<=20:
                dp[i][j+lst[i]] += dp[i-1][j]
            if 0<=j-lst[i]<=20:
                dp[i][j-lst[i]] += dp[i-1][j]
print(dp[n-2][lst[-1]])
