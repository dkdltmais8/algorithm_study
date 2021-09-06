a, b = map(str, input().split())
n, m = len(a), len(b)
board = [['.']*n for _ in range(m)]
point_r = 0
point_c = 0
for r in range(n):
    for c in range(m):
        if a[r] == b[c]:
            point_r = r
            point_c = c
            break
    if point_r != 0 or point_c != 0:
        break
for c in range(n):
    board[point_c][c] = a[c]
for r in range(m):
    board[r][point_r] = b[r]

for r in range(m):
    print(''.join(board[r]))
