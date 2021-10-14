from collections import deque
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def bfs():
    Q = deque()
    Q.append((0,0))
    visit[0][0] = 0
    while Q:
        r,c = Q.popleft()
        cnt = 0
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc <n and visit[nr][nc] == -1:
                if board[nr][nc] != 0:
                    visit[nr][nc] = visit[r][c]+board[nr][nc]
                    Q.append((nr,nc))
                elif board[nr][nc] != 0 and cnt == 1:
                    cnt = 0
                elif board[nr][nc]==0 and cnt == 0:
                    cnt += 1
                    visit[nr][nc] = visit[r][c]+ m


for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    bfs()
    print(board)
    print(visit)