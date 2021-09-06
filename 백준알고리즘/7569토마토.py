from collections import deque
M, N, H = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]

def safety(nx,ny,nz):
    if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
        return True

def bfs():
    while Q:
        z,x,y = Q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if safety(nx,ny,nz):
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    Q.append((nz,nx,ny))
Q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                Q.append((i,j,k))
bfs()
tomato = 1
ans =0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                tomato = 0
            ans = max(ans,k)

if ans == 1:
    print(0)
elif tomato == 0:
    print(-1)
else:
    print(ans-1)