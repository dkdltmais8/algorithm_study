import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def check(idx,depth):
    #depth가 4가 되면 가능한 관계이므로 return True 해주기
    global flag
    if flag:
        return
    if depth==4:
        flag = True
        return
    for i in graph[idx]:
        if not visit[i] and not flag :
            visit[i] = 1
            check(i,depth+1)
            visit[i] = 0
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
flag = False
visit = [0] * n
for i in range(n):
    visit[i] = 1
    check(i,0)
    visit[i] = 0
    if flag:
        break
print(1 if flag else 0)

