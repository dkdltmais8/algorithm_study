def row_search(a,b,ans):
    #시작점을 기록하기 위해 글로벌변수 지정
    global  white, black, win
    #시작점부터 5칸 세로로 진행했을 때 합이 5인지판단
    if sum(board[a][b+i] == ans for i in range(5)) == 5:
        #합은 5인데 그전이나 그다음 숫자가 ans이면 오목이 아니라 육목 칠목이기 때문에 조건을 세움
        if board[a][b+5] != ans and board[a][b-1] != ans:
            #정확히 오목이면 시작점을 글로벌 변수에 저장(출력용도)
            white, black, win = a,b,ans
def col_search(a,b,ans):
    global  white, black, win
    if sum(board[a+i][b] == ans for i in range(5)) == 5:
        if board[a+5][b] != ans and board[a-1][b] != ans:
            white, black, win = a,b,ans
def daegak_search(a,b,ans):
    global  white, black, win
    if sum(board[a+i][b+i] == ans for i in range(5)) == 5:
        if board[a+5][b+5] != ans and board[a-1][b-1] != ans:
            white, black, win = a,b,ans
def daegak_rev_search(a,b,ans):
    global  white, black, win
    if sum(board[a-i][b+i] == ans for i in range(5)) == 5:
        if board[a-5][b+5] != ans and board[a+1][b-1] != ans:
            white, black, win = a,b,ans
## 오목판때기 만들기.
board = []
board.append([0]*21)
for _ in range(19):
    ls = [0] + list(map(int,input().split())) +[0]
    board.append(ls)
board.append([0]*21)
#시작점을 기록하기 위한 글로벌 변수
white, black, win = 0, 0, 0
#오목판을 전부 돌면서
for r in range(1,20):
    #승자가 1 또는 2로 정해졌을 때 멈춘다
    if win != 0:
        break
    for c in range(1,20):
        # 오목판이 1 일때
        if board[r][c] == 1:
            #14보다 크면 어차피 5개가 완성이 안되기 떄문에 범위지정
            if c <= 15:
                row_search(r,c,1)
            if r <= 15:
                col_search(r,c,1)
            if r <= 15 and c <= 15:
                daegak_search(r,c,1)
            if r >= 5 and c <= 15:
                daegak_rev_search(r,c,1)
        #오목판이 2일떄
        elif board[r][c] == 2:
            #시간 감소를 위해 범위 지정
            if c <= 15:
                row_search(r,c,2)
            if r <= 15:
                col_search(r,c,2)
            if r <= 15 and c <= 15:
                daegak_search(r,c,2)
            if r >= 5 and c <= 15:
                daegak_rev_search(r,c,2)
#승자를 출력하고
print(win)
# 무승부가 아닐 때
if win != 0:
    print(white, black)

