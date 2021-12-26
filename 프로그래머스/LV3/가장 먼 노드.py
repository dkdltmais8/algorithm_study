from collections import deque
def solution(n, edge):
    def check(lst):
        Q = deque()
        for i in lst:
            Q.append(i)
            visit[i] = 2
        while Q:
            now = Q.popleft()
            for i in node[now]:
                if visit[i] == 0:
                    visit[i] = visit[now]+1
                    Q.append(i)


    answer = 0
    node = [[] for _ in range(n+1)]
    for i in edge:
        node[i[0]].append(i[1])
        node[i[1]].append(i[0])
    visit = [0]*(n+1)
    visit[1] = 1
    check(node[1])
    ans = max(visit)
    answer = visit.count(ans)
    return answer
solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])