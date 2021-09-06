T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0


    new_board = [[0]*n for _ in range(n)]
    #가로 세로 바꾸기
    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[j][i]

    for r in range(n):
        total = 0
        for c in range(n):
            if board[r][c] == 1:
                total += 1

            if board[r][c] == 0:
                total = 0

            if total == m and ((c == n-1) or (board[r][c+1] == 0)):
                cnt += 1
                total = 0

    for r in range(n):
        total = 0
        for c in range(n):
            if new_board[r][c] == 1:
                total += 1

            if new_board[r][c] == 0:
                total = 0

            if total == m and ((c == n-1) or (new_board[r][c+1]==0)) :
                cnt += 1
                total = 0
    print("#{} {}".format(tc,cnt))

