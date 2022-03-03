import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+arr[i-1][j-1]
for i in range(m):
    sr,sc,er,ec = map(int,input().split())
    print(dp[er][ec]-dp[er][sc-1]-dp[sr-1][ec]+dp[sr-1][sc-1])