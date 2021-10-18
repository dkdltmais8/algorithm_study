n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
arr = [[0]*n for _ in range(n)]
arr[0][0] = 1
for r in range(n):
    for c in range(n):
        if r == n-1 and c== n-1 :
            break
        dist = board[r][c]
        down = r+dist
        right = c+dist
        if down < n:
            arr[down][c] += arr[r][c]
        if right < n:
            arr[r][right] += arr[r][c]
        # print(arr)
print(arr[n-1][n-1])
