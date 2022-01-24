import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def out(r,c,d,grid,dic):
    nr = r + dic[d][0]
    nc = c + dic[d][1]
    if nr>=len(grid):
        nr = 0
    elif nr<0:
        nr = len(grid)-1
    if nc>=len(grid[0]):
        nc = 0
    elif nc<0:
        nc = len(grid[0]) - 1
    return nr,nc
def dfs(now,origin,cnt,grid):
    dic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    r = now[0]
    c = now[1]
    d = now[2]
    visit[d][r][c] = 1
    nr,nc = out(r,c,d,grid,dic)
    v = grid[nr][nc]
    if v == 'R':
        d = (d+5) % 4
    elif v == 'L':
        d = (d+7) % 4
    if origin[0] == nr and origin[1] == nc and origin[2] == d:
        answer.append(cnt)
        return
    if not visit[d][nr][nc]:
        dfs([nr,nc,d],origin,cnt+1,grid)
def solution(grid):
    global answer,visit
    answer = []
    visit = [[[0]*len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                dfs([i,j,k],[i,j,k],1,grid)
    return sorted(answer)
