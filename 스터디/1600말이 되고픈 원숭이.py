from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
ddr = [-2,-2,-1,-1,1,1,2,2]
ddc = [1,-1,2,-2,2,-2,1,-1]
def bfs():
    cnt = 0
    Q = deque()
    Q.append((0,0))
    visit[0][0] = 1
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<= nc < n and visit[nr][nc] == 0 and arr[nr][nc]!=1:
                visit[nr][nc] = visit[r][c]+1
                Q.append((nr,nc))
        for i in range(8):
            nr = r+ddr[i]
            nc = c+ddc[i]
            if 0<=nr<n and 0<= nc<n and visit[nr][nc] == 0 and cnt<k:
                visit[nr][nc] = visit[r][c]+1
                Q.append((nr,nc))
        cnt+=1
k = int(input())
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
visit = [[0]*n for _ in range(m)]
bfs()
print(visit)