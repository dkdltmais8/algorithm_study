T = int(input())
for tc in range(1, T+1):
    board = [list(map(str,input())) for _ in range(5)]
    a = []
    for r in range(5):
        a.append(len(board[r]))
    length = max(a)

    big_board = [['']*length for _ in range(length)]
    babo = ''
    for r in  range(5):
        for c in range(len(board[r])):
            big_board[r][c] = board[r][c]

    for r in range(length):
        for c in range(5):
            if len(big_board[c][r]) == 0:
                pass
            babo += big_board[c][r]
    print("#{} {}".format(tc,babo))
