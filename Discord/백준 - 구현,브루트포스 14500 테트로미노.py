import sys
input = sys.stdin.readline
dr = [1,-1,0,0]
dc = [0,0,1,-1]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
ans = 0
max_val = max(map(max,arr))
def dfs(r,c,depth,tot):
    global ans
    if ans>=tot+max_val*(4-depth):
        return
    if depth==4:
        ans = max(ans,tot)
        return
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<n and 0<=nc<m and not visit[nr][nc]:
            if depth == 2:
                visit[nr][nc]= 1
                dfs(r,c,depth+1,tot+arr[nr][nc])
                visit[nr][nc] = 0
            visit[nr][nc] = 1
            dfs(nr,nc,depth+1,tot+arr[nr][nc])
            visit[nr][nc] = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i,j,1,arr[i][j])
        visit[i][j] = 0
print(ans)
