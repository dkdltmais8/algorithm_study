def dfs(idx,size,time):
    global ans
    if time > m:
        return
    if time <= m:
        ans = max(ans,size)
    if idx <= n-1:
        dfs(idx+1,size+board[idx+1],time+1)
    if idx <= n-2:
        dfs(idx+2, size//2 + board[idx+2], time+1)
n,m = map(int,input().split())
board = [0] + list(map(int,input().split()))
ans = -1
dfs(0,1,0)
print(ans)
