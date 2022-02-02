def solution(k, dungeons):
    answer = -1
    def dfs(idx,k,cnt):
        nonlocal answer,visit
        if answer<cnt:
            answer = cnt
        now = k
        for i in range(len(dungeons)):
            if not visit[i]:
                if now>=dungeons[i][0]:
                    now -= dungeons[i][1]
                    visit[i] = 1
                    dfs(i+1,now,cnt+1)
                    now += dungeons[i][1]
                    visit[i] = 0
    visit = [0 for _ in range(len(dungeons))]
    for i in range(len(dungeons)):
        dfs(i,k,0)
    print(answer)
    return answer
solution(80,	[[80,20],[50,40],[30,10]])