import sys
def dfs(r,c,h,shield,dist):
    global ans
    if h+shield <= 0:
        return -1
    if abs(er-r) +abs(ec-c) <= h+shield:
        ans = min(ans,dist + abs(er-r) +abs(ec-c))
        return

    for i in range(len(umbrella)):
        d = abs(umbrella[i][0]-r)+ abs(umbrella[i][1]-c)
        if d > h+shield or visit[i] == 1:
            continue
        if shield < d:
            visit[i] = 1
            dfs(umbrella[i][0],umbrella[i][1],h+shield-d,D,dist+d)
            visit[i] = 0
        else:
            visit[i] = 1
            dfs(umbrella[i][0],umbrella[i][1],h,D,dist+d)
            visit[i] = 0

N,H,D = map(int,input().split())
board = [list(input()) for _ in range(N)]
#우산은 총 10개이므로 1번우산부터 10번우산까지
visit = [0]*11
umbrella = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 'S':
            sr = r; sc=c;
        elif board[r][c] == 'E':
            er =r; ec=c;
        elif board[r][c] == 'U':
            umbrella.append((r,c))
ans = sys.maxsize
dfs(sr,sc,H,0,0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
# https://www.acmicpc.net/problem/22944