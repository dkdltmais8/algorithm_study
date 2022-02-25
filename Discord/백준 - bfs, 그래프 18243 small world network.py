from collections import deque
import sys
input=sys.stdin.readline
def check(me):
    Q = deque([me])
    visit = [0]*(n+1)
    visit[me] = 1
    while Q:
        idx = Q.popleft()
        for i in graph[idx]:
            if not visit[i]:
                Q.append(i)
                visit[i] = visit[idx]+1
    for i in visit[1:]:
        if i>7 or i == 0:
            return False
    return True

n,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(k):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
flag = True
for i in range(1,n+1):
    if not check(i):
        flag = False
        break
print("Small World!" if flag else "Big World!")
