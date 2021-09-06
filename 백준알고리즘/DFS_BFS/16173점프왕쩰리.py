from collections import deque
dr = [0,1]
dc = [1,0]
def bfs(r,c):
    global visited
    Q=deque()
    Q.append((r,c))
    while Q:
        nr,nc = Q.popleft()
        if board[nr][nc] == -1:
            return True
        length = board[nr][nc]
        for i in range(2):
            x,y = nr+dr[i]*length,nc+dc[i]*length
            if 0<= x<n and 0<=y<n and not visited[x][y]:
                visited[x][y] = 1
                Q.append((x,y))
    return False
def answer():
    ans = bfs(0,0)
    return 'HaruHaru' if ans else 'Hing'

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
print(answer())