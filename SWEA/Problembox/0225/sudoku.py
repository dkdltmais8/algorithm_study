def garo_check():
    global result
    for r in range(9):
        for c in range(9):
            for i in range(8-c):
                if board[r][c] == board[r][c+i+1]:
                    result = 0
def sero_check():
    global result
    for r in range(9):
        for c in range(9):
            for i in range(8-c):
                if board[c][r] == board[c+i+1][r]:
                    result = 0

def block_check():
    global result
    for r in range(0,9,3):
        for c in range(0,9,3):
            board_check = []
            for i in range(3):
                for j in range(3):
                    board_check.append(board[r+i][c+j])
            for _ in range(9):
                for i in range(8):
                    if board_check[i] == board_check[i+1]:
                        result = 0

T = int(input())
for tc in range(1, T+1):
    result = 1
    board = [list(map(int,input().split())) for _ in range(9)]
    garo_check()
    sero_check()
    block_check()
    print("#{} {}".format(tc, result))
