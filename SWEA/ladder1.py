for tc in range(1, 11):
    board = [list(map(int, input().split())) for _ in range(100)]
    r, c = 0, 0
    while board[r][c] != 2:
        if board[r][c] == 1:
            if board[r][c+1] == 0:
                if board[r + 1][c] == 1:
                    r += 1
                    c += 0
            elif 0 < c < 99 and board[r][c+1] == 1:
                c += 1
            elif c > 0 and board[r][c-1] == 1:
                c -= 1
    print(f"#{tc} {r}")

