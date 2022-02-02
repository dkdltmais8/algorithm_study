def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while 1:
        lst = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    for k in range(i,i+2):
                        for l in range(j,j+2):
                            lst[k][l] = 1
        cnt = 0
        for i in range(m):
            cnt += sum(lst[i])
        if cnt == 0:
            break
        answer += cnt
        for i in range(m-1,-1,-1):
            for j in range(n):
                if lst[i][j] == 1:
                    r = i-1
                    while r>=0 and lst[r][j] == 1:
                        r -= 1
                    if r<0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[r][j]
                        lst[r][j] = 1
    return answer
solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])