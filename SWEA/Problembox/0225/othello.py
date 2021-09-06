dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]
T = int(input())
for t in range(T):
    n, m = map(int, input().split())

    board= [[0]*n for _ in range(n)]

    point = n // 2
    board[point - 1][point - 1] = 2
    board[point][point] = 2
    board[point - 1][point] = 1
    board[point][point - 1] = 1
    # 새로 입력받기
    for _ in range(m):
        c, r,  color = map(int, input().split())
        c, r = c-1, r-1
        board[r][c] = color

        for i in range(8):
            nr, nc = r+dr[i], c+dc[i]

            while 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 0:
                    break
                if board[nr][nc] == color:
                    tr, tc = nr-dr[i], nc - dc[i]
                    while tr != r or tc != c:
                        board[tr][tc] = color
                        tr, tc = tr-dr[i], tc-dc[i]
                    break
                nr, nc = nr+dr[i], nc+dc[i]
    w = b = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b += 1

            elif board[i][j] == 2:
                w += 1

    print("#{} {} {}".format(t+1, b,w))