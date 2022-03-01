dr = [1,-1,0,0]
dc = [0,0,1,-1]
from collections import deque,defaultdict
import sys
input = sys.stdin.readline
def bfs(lst):
    Q = deque()
    while lst:
        a,b = lst.popleft()
        for i in range(4):
            na = a+dr[i]
            nb = b+dc[i]
            if 0<=na<n and 0<=nb<n and arr[na][nb] == 0:
                arr[na][nb] = arr[a][b]
                Q.append((na,nb))
    return Q
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
s,x,y = map(int,input().split())
x,y = x-1,y-1
lst = defaultdict(deque)
for i in range(n):
    for j in range(n):
        if arr[i][j] !=0:
            lst[arr[i][j]].append((i,j))
for i in range(s):
    for j in range(1,m+1):
        lst[j] = bfs(lst[j])
print(arr[x][y])
