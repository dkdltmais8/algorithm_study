def dfs(r,c,dp,arr):
    if r<0 or c<0:
        return 0
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = arr[r][c]
    dp[r][c]  += max(dfs(r-1,c,dp,arr),dfs(r,c-1,dp,arr))
    return dp[r][c]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visit = [[-1]*m for _ in range(n)]
visit[0][0] = arr[0][0]
dfs(n-1,m-1,visit,arr)
print(visit[-1][-1])