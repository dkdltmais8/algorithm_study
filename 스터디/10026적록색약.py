from collections import deque
dr = [1,-1,0,0]
dc = [0,0,-1,1]
def bfs(r,c,color):
    Q = deque()
    Q.append([r,c])
    while Q:
        r,c = Q.popleft()
        if visit[r][c] == 0:
            visit[r][c] = 1
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if 0<=nr<n and 0<=nc<n and visit[nr][nc]==0 and arr[nr][nc]==color:
                    Q.append([nr,nc])

n = int(input())
arr = [list(input()) for _ in range(n)]
# print(arr)
cntNoSick = 0
visit = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if visit[r][c] == 0:
            color = arr[r][c]
            bfs(r,c,color)
            cntNoSick+=1
cntSick = 0
visit = [[0]*n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if arr[r][c] == 'G':
            arr[r][c] = 'R'
for r in range(n):
    for c in range(n):
        if visit[r][c] == 0:
            color = arr[r][c]
            bfs(r,c,color)
            cntSick+=1
print(cntNoSick,cntSick)




