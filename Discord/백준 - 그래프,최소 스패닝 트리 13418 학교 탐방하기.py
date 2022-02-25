import heapq,sys
input = sys.stdin.readline
def check(lst,graph):
    Q = [lst]
    cnt = 0
    ans = 0
    visit = [0]*(n+1)
    visit[0] = 1
    while Q:
        if cnt == n:
            break
        w,s = heapq.heappop(Q)
        if not visit[s]:
            visit[s] = 1
            cnt += 1
            if w == 0:
                ans += 1
            for i in graph[s]:
                if not visit[i[1]]:
                    heapq.heappush(Q, i)
    return ans

n,m = map(int,input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for i in range(m+1):
    a,b,c = map(int,input().split())
    graph1[a].append((-c,b))
    graph1[b].append((-c,a))
    graph2[a].append((c,b))
    graph2[b].append((c,a))
print(check(graph2[0][0],graph2)**2-check(graph1[0][0],graph1)**2)
