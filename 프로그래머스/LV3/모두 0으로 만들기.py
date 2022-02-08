import sys
sys.setrecursionlimit(10**6)
def solution(a, edges):
    def dfs(idx,a,graph):
        nonlocal answer
        now = a[idx]
        visit[idx] = 1
        for i in graph[idx]:
            if visit[i] == 0:
                now += dfs(i,a,graph)
        answer += abs(now)
        return now
    answer = 0
    graph = [[] for _ in range(len(a))]
    if sum(a) != 0:
        return -1
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    visit = [0]*len(a)
    dfs(0,a,graph)
    return answer
solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]])