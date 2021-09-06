dr = [0,-1,0,1]
dc = [-1,0,1,0]
def start_point():
    for r in range(n):
        for c in range(n):
            if miro[r][c] == '2':
                return r,c
def bfs():
    while Q:
        start = Q.pop(0)
        for i in range(4):
            nr, nc = start[0] + dr[i], start[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and miro[nr][nc] == '3':
                return visited[start[0]][start[1]]
            elif 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and miro[nr][nc] == '0':
                Q.append((nr,nc))
                visited[nr][nc] = visited[start[0]][start[1]] + 1

    return 0

for tc in range(1,int(input())+1):
    n = int(input())
    miro = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    Q = [start_point()]
    print("#{} {}".format(tc, bfs()))

