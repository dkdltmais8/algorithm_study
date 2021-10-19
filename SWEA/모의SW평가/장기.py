dr = [1,-1,0,0]
dc = [0,0,1,-1]
def dfs(r,c,cnt,tot):
    if cnt == 4:
        return tot
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        while 0<=nr<n and 0<=nc<n:
            if board[nr][nc] ==0:
                nr = r + dr[i]
                nc = c + dc[i]
            else:
                
        dfs(nr,nc,cnt+1,tot+1)



for tc in range(1,int(input())+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    print(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 2:
                sr,sc = r,c
    dfs(sr,sc,0,0)