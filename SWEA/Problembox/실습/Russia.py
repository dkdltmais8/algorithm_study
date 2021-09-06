T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    board = [list(input()) for _ in range(n)]

    for r in range(n):
        cnt_w = []
        cnt_b = []
        cnt_r = []
        for c in range(m):
            if board[r][c] == 'W':
                cnt_w.append(1)
            elif board[r][c] == 'B':
                cnt_b.append(1)
            else:
                cnt_r.append(1)
        print(max(len(cnt_b),len(cnt_w),len(cnt_r)))
