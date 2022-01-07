from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs():
    Q = deque()
    Q.append((0,0))
    visit[0][0] = 1
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc < n and not visit[nr][nc]:
                if arr[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c]+1
                    Q.append((nr,nc))
                else:
                    visit[nr][nc] = visit[r][c]
                    Q.appendleft((nr,nc))

n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
bfs()
print(visit[n-1][n-1]-1)