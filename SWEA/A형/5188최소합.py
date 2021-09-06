def section(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r,c):
    global tot, ans
    if ans < tot:
        return
    if r == n-1 and c == n-1:
        ans = tot
        return
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if section(nr,nc) and (nr,nc) not in visited:
            visited.append((nr,nc))
            tot += board[nr][nc]
            dfs(nr,nc)
            visited.remove((nr,nc))
            tot -= board[nr][nc]

T = int(input())
for tc in range(1, T+1):
    dr = [0, 1]
    dc = [1, 0]
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = []
    tot = board[0][0]
    ans = 9999999
    dfs(0,0)
    print("#{} {}".format(tc, ans))