dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

def check():
    global tc
    cnt = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'o':
                for i in range(8):
                    cnt = 1
                    nr , nc = r + dr[i], c + dc[i]
                    while 0 <= nr < n and 0 <= nc < n:
                        if board[nr][nc] == '.':
                            break
                        cnt += 1
                        if cnt == 5:
                            return "#{} YES".format(tc)
                        nr, nc = nr + dr[i] , nc + dc[i]
    return "#{} NO".format(tc)
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [input() for _ in range(n)]
    print(check())

