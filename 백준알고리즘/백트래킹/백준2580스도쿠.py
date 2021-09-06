
arr = [list(map(int,input().split())) for _ in range(9)]
new_arr = []
for r in range(9):
    for c in range(9):
        if arr[r][c] == 0:
            new_arr.append((r,c))
def alter(r,c):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if arr[r][i] in num:
            num.remove(arr[r][i])
        if arr[i][c] in num:
            num.remove(arr[i][c])
    r = r//3
    c = c//3
    for i in range(r*3,(r+1)*3):
        for j in range(c*3,(c+1)*3):
            if arr[i][j] in num:
                num.remove(arr[i][j])
    return num
def dfs(cnt):
    if cnt == len(new_arr):
        for i in arr:
            print(*i)
        return
    (i,j) = new_arr[cnt]
    alt = alter(i,j)
    for k in alt:
        arr[i][j] = k
        dfs(cnt+1)
        arr[i][j] = 0
dfs(0)