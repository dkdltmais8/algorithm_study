from collections import deque

def bfs():
    global time
    Q = deque()
    Q.append((0, 0))
    visit[0][0] = 1
    while Q:
        r,c = Q.popleft()
        if castle[r][c] == 2:
            time = (n-1-r)+(m-1-c)+(visit[r][c]-1)
        if r == n-1 and c == m-1:
            return min(time,visit[r][c]-1)
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<= nr<n and 0<=nc <m and castle[nr][nc] != 1 and visit[nr][nc] == 0:
                Q.append((nr,nc))
                visit[nr][nc] = visit[r][c]+1
                print(visit)
    return time

dr = [1,-1,0,0]
dc = [0,0,1,-1]
n,m,t = map(int,input().split())
castle = [list(map(int,input().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
time = 1000000
ans = bfs()
print(ans if ans<= t else 'Fail')
