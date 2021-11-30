def solution(n, computers):
    def dfs(check):

    answer = 0
    ans = [[] for _ in range(n)]
    visit = [0]*(n+1)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                ans[i].append(j)
    for i in ans:
        if not
    print(ans)
    return answer
solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])