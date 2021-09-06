dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check_A():
    global board
    for i in range(4):
        nr, nc = r+dr[i],c+dc[i]
        board[nr][nc] = 'X'

    return board
def check_B():
    global board
    i = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        while  i <= 1:
            board[nr][nc] = 'X'
            i += 1
def check_C():
    global board
    i = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        while i <= 2:
            board[nr][nc] = 'X'
            i += 1


for tc in range(1, int(input())+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]

    cnt = 0
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'A':
                check_A()
            elif board[r][c] == 'B':
                check_B()
            elif board[r][c] == 'C':
                check_C()

    print(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'H':
                cnt += 1
    print(cnt)