from collections import deque
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]
# def bfs():
#     global hp,shield
#     Q = deque()
#     Q.append((0,0))
#     while Q:
#         r,c = Q.popleft()
#         for i in range(4):
#             nr = r+dr[i]
#             nc = c+dc[i]
#             if 0<=nr<N and 0<=nc<N and visit[nr][nc] == 0:
#                 if board[nr][nc] == 'U':
#                     shield = D
#                 hp -= 1
#                 visit[nr][nc] = visit[r][c]+1
#                 Q.append((nr,nc))
#                 if hp == 0:
#                     return -1
#                 if nr == N - 1 and nc == N - 1:
#                     return visit[nr - 1][nc - 1]
#
#
#
# N,H,D = map(int,input().split())
# shield = 0
# hp = H+shield
# board = [list(input()) for _ in range(N)]
# visit = [[0] * N for _ in range(N)]
# ans = bfs()
# print(ans)
# print(N,H,D)
# print(board)
# print(visit)

def search_start_end():
    for r in range(N):
        for c in range(N):
            if board[r][c] =='S':
                start.append((r,c))
            elif board[r][c] == 'E':
                end.append((r,c))


def search_umbrella():
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'U':
                umb.append((r,c))

def go_umbrella():
    r1,c1 = start.pop()
    r2,c2 = end.pop()
    for x,y in umb:
        if H >= abs(r1-x)+abs(c1-y):
            if D+H - abs(r1-x)+abs(c1-y) >= abs(r2-x)+abs(c2-y):
                hp = D+H - abs(r1-x)+abs(c1-y)
                visit[x][y] = abs(r1-x)+abs(c1-y)
                visit[r2][c2] +=visit[x][y]+ abs(r2-x)+abs(c2-y)
                hp = hp - abs(r2 - x) + abs(c2 - y)
                return visit[r2][c2]
            else:
                continue
        else:
            continue
    return -1



N,H,D = map(int,input().split())
umbrella = 0
hp = H+umbrella
umb = []
start = []
end = []
board = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
res = []
search_start_end()
search_umbrella()
ans = go_umbrella()

# print(N,H,D)
# print(board)
# print(visit)
# print(umb)
print(ans)
# https://www.acmicpc.net/problem/22944