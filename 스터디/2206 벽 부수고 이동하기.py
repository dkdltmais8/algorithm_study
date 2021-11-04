from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs():
    Q = deque()
    Q.append((0,0,0))
    visit[0][0][0] = 1
    while Q:
        r,c,cnt = Q.popleft()
        if r == n-1 and c==m-1:
            return visit[r][c][cnt]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m:
                if arr[nr][nc]=='1' and cnt== 0:
                    visit[nr][nc][1] = visit[r][c][0]+1
                    Q.append((nr,nc,cnt+1))
                elif arr[nr][nc]=='0' and visit[nr][nc][cnt] ==0:
                    visit[nr][nc][cnt] = visit[r][c][cnt]+1
                    Q.append((nr,nc,cnt))

    return -1
n,m = map(int,input().split())
arr = [input() for _ in range(n)]
visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(bfs())

# print(arr)
