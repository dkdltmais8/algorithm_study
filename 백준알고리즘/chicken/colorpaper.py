n = int(input())

board = [[0]*101 for _ in range(101)]
paper = {}
# cnt = [0]*101

for i in range(1,n+1):
    info = list(map(int,input().split()))
    paper[i] = info

for i in range(1, n+1):
    for r in range(paper[i][0],paper[i][2]+paper[i][0]):
        for c in range(paper[i][1],paper[i][3]+paper[i][1]):
            board[r][c] = i

for i in range(1,n+1):
    cnt = 0
    for r in range(101):
        for c in range(101):
            if board[r][c] == i:
                cnt += 1
    print(cnt)

