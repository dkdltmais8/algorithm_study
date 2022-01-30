from collections import deque
def bfs(s,visit,lst):
    Q = deque([s])
    ans = 1
    visit[s] = 1
    while Q:
        now = Q.popleft()
        for i in lst[now]:
            if visit[i] == 0:
                ans += 1
                Q.append(i)
                visit[i] = 1
    return ans
def solution(n, wires):
    answer = n
    lst = [[] for _ in range(n+1)]
    for i in wires:
        s,e = i[0],i[1]
        lst[s].append(e)
        lst[e].append(s)
    for s,e in wires:
        visit = [0]*(n+1)
        visit[e] = 1
        ans = bfs(s,visit,lst)
        if abs(ans-(n-ans))<answer:
            answer = abs(ans-(n-ans))

    return answer
solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])