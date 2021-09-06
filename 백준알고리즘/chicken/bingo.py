def check():
    cnt = 0
    #가로 세로 확인
    for i in range(5):
        cnt_row = 0
        cnt_col = 0
        for j in range(5):
            if board[i][j] == 0:
                cnt_row += 1
            if board[j][i] == 0:
                cnt_col += 1
        if cnt_row == 5:
            cnt += 1
        if cnt_col == 5:
            cnt += 1
    # 대각선, 역대각선 확인
    cnt_daegak = 0
    cnt_rev = 0
    for i in range(5):
        if board[i][i] == 0:
            cnt_daegak += 1
        if board[i][4-i] == 0:
            cnt_rev += 1
    if cnt_daegak == 5:
        cnt += 1
    if cnt_rev == 5:
        cnt += 1
    if cnt >= 3:
        return True
    return False
# 철수 빙고판
board = [list(map(int,input().split())) for _ in range(5)]

#체크할 좌표 생성(숫자가 1부터기 때문에 배열을 26으로 만들어줌)
bingo = [0]*26
for r in range(5):
    for c in range(5):
        bingo[board[r][c]] = (r,c)

#체크리스트 만들기
checklist = []
for i in range(5):
    checklist += list(map(int,input().split()))
result = 0
while check() == False:
    r,c = bingo[checklist[result]]
    board[r][c] = 0
    result += 1
print(result)