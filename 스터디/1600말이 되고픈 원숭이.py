from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
ddr = [-2,-2,-1,-1,1,1,2,2]
ddc = [1,-1,2,-2,2,-2,1,-1]
def bfs():
    Q.append((0,0,0))
    visit[0][0][0] = 1
    while Q:
        r,c,cnt = Q.popleft()
        if r == m-1 and c== n-1:
            print(visit[r][c][cnt]-1)
            return
        if cnt <k:
            monkey(r,c,cnt)
            horse(r,c,cnt)
        else:
            monkey(r,c,cnt)
    print(-1)

def monkey(r,c,cnt):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < m and 0 <= nc < n and visit[nr][nc][cnt] == 0 and arr[nr][nc] != 1:
            visit[nr][nc][cnt] = visit[r][c][cnt] + 1
            Q.append((nr, nc, cnt))
def horse(r,c,cnt):
    for i in range(8):
        nr = r + ddr[i]
        nc = c + ddc[i]
        if 0 <= nr < m and 0 <= nc < n and visit[nr][nc][cnt+1] == 0 and arr[nr][nc]==0:
            visit[nr][nc][cnt+1] = visit[r][c][cnt] + 1
            Q.append((nr, nc, cnt + 1))
k = int(input())
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
visit = [[[0]*31 for _ in range(n)] for _ in range(m)]
Q = deque()
bfs()
