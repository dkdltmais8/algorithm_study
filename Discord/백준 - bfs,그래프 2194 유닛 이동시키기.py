from collections import deque
import sys
input = sys.stdin.readline
dR = [1,-1,0,0]
dC = [0,0,1,-1]
def bfs():
    Q = deque([s])
    visit[s[0]][s[1]] = 1
    while Q:
        nr,nc = Q.popleft()
        for i in range(4):
            R = nr+dR[i]
            C = nc+dC[i]
            if check((R,C)) and not visit[R][C]:
                visit[R][C] = visit[nr][nc]+1
                Q.append((R,C))
                if board[R][C] == 3:
                    return
def check(point):
    s,e = point
    for i in range(r):
        for j in range(c):
            if not (0<=s+i<n and 0<= e+j<m):
                return False
            if board[s+i][e+j] == 1:
                return False
    return True
n,m,r,c,k = map(int,input().split())
board = [[0]*m for _ in range(n)]
for _ in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1
s = list(map(int,input().split()))
e = list(map(int,input().split()))
s[0],s[1],e[0],e[1] = s[0]-1,s[1]-1,e[0]-1,e[1]-1
board[s[0]][s[1]] = 2
board[e[0]][e[1]] = 3
visit = [[0]*m for _ in range(n)]
bfs()
print(visit[e[0]][e[1]]-1)

#장애물의 위치를 저장해놓고 현재 위치 포인트에서 r,c만큼 더했을 때 장애물위치와 겹치면 탈락
#현재 위치 포인트에서 r,c 만큼 더했을 때 크기를 넘어간다면 탈락