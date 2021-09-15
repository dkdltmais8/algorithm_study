def solution(N, stages):
    answer = {}
    n = len(stages)
    for i in range(1,N+1):
        if n == 0:
            answer[i] = 0
            continue
        cnt = stages.count(i)
        answer[i] =  cnt/n
        n -= cnt
    # print(answer)
    return sorted(answer,reverse=True,key=lambda x:answer[x])
print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))
solution(4	,[4,4,4,4,4])
solution(8,[1,2,3,4,5,6,7])
