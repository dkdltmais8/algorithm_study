def dfs(r):
    global tot, my_min
    if my_min < tot:
        return
    if r == n:
        if my_min > tot:
            my_min = tot
            return
    for c in range(n):
        if visited[c] == 0:
            visited[c] = 1
            tot += board[r][c]
            dfs(r+1)
            tot -= board[r][c]
            visited[c] = 0
for tc in range(1, int(input())+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [0]*n
    tot, my_min = 0, n*9
    dfs(0)
    print("#{} {}".format(tc, my_min))