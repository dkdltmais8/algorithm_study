from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def solution(maps):
    def bfs():
        Q = deque()
        Q.append((0,0))
        visit[0][0] = 1
        while Q:
            r,c = Q.popleft()
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0<=nr<n and 0<=nc<m and not visit[nr][nc] and maps[nr][nc]:
                    Q.append((nr,nc))
                    visit[nr][nc] += visit[r][c] + 1
    answer = 0
    n,m = len(maps),len(maps[0])
    visit = [[0]*(m) for _ in range(n)]
    bfs()
    answer = visit[n-1][m-1]
    return answer if answer !=0 else -1
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	)