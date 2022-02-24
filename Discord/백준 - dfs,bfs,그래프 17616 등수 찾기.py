from collections import deque
import sys
input = sys.stdin.readline
def bfs(me,lst):
    cnt = 0
    Q = deque()
    Q.append(me)
    visit[me] = 1
    while Q:
        now = Q.popleft()
        for i in lst[now]:
            if not visit[i]:
                visit[i] = 1
                Q.append(i)
                cnt += 1
    return cnt

n,m,me = map(int,input().split())
rank = []
win = [[] for _ in range(n+1)]
lose = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    s,e = map(int,input().split())
    win[s].append(e)
    lose[e].append(s)
print(*[1+bfs(me,lose),n-bfs(me,win)])