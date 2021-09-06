
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def start():
    for r in range(n):
        for c in range(n):
            if board[r][c] == 2:
                return r, c

def check(s):
    global ans
    r, c = s
    if board[r][c] == 3:
        ans = 1
        return ans
    visited.append((r,c))
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited and (board[nr][nc] == 0 or board[nr][nc] == 3):
            check((nr,nc))


for tc in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    visited = []
    ans = 0
    check(start())
    print("#{} {}".format(tc, ans))