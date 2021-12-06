def solution(m, n, puddles):
    board = [list(0 for i in range(m+1)) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0 or [j,i] in puddles:
                board[i][j] = 0
            elif i ==1 and j==1:
                board[i][j] = 1
            else:
                board[i][j] = board[i-1][j]+board[i][j-1]
            print(board)
    return board[n-1][m-1]%1000000007
solution(4,3,[[2,2]])