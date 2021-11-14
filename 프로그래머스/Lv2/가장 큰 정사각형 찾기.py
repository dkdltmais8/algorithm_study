def solution(board):
    answer = 0
    len_row = len(board)
    len_col = len(board[0])
    dp = [[0 for _ in range(1001)] for _ in range(1001)]
    for i in range(1,len_row):
        for j in range(1,len_col):
            if board[i-1][j-1] != 0:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                answer = max(answer,dp[i][j])
                print(answer)
    return answer**2
solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
solution([[0,0,1,1],[1,1,1,1]])