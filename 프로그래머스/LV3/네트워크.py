def solution(n, computers):
    def dfs(now):
        nonlocal answer
        visit[now] = 1
        for i in range(n):
            if i != now and computers[now][i] == 1 and visit[i] == 0:
                answer -=1
                dfs(i)
    answer = n
    visit = [0]*(n)
    for i in range(n):
        if visit[i] == 0:
            dfs(i)


    # print(answer)

    return answer
solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])