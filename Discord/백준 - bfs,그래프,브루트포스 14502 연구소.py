from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline
def bfs():
    Q = deque()
    test = deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if test[i][j] == 2:
                Q.append((i,j))
    while Q:
        r,c = Q.popleft()
        for i in range(4):
            nr = r+ dr[i]
            nc = c+ dc[i]
            if not (0<=nr<n and 0<=nc<m):
                continue
            if test[nr][nc] == 0:
                test[nr][nc] = 2
                Q.append((nr,nc))
    global answer
    cnt = 0
    for i in range(n):
        cnt += test[i].count(0)
    answer = max(answer,cnt)
def make(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make(cnt+1)
                arr[i][j] = 0
dr = [1,-1,0,0]
dc = [0,0,1,-1]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0
make(0)
print(answer)