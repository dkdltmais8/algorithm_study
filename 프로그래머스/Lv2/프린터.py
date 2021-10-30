def solution(priorities, location):
    answer = 0
    max_a = 0
    idx = 0
    q = []
    ans = []
    for x in range(len(priorities)):
        q.append((priorities[x], x))
    d = len(q)
    while 1:
        for i in range(d):
            if max_a<q[i][0]:
                max_a = q[i][0]
                idx = i
        ans = q[idx:]+q[:idx]
        for i in range(d-1):
            if ans[i][0]>=ans[i+1][0]:
                if ans[i][1] == location:
                    answer = i+1
                continue
        else:
            break
    print(ans,q)
    if answer == 0:
        answer = d
    print(answer)
    return answer
solution([2, 1, 3, 2]	,2)
solution([1, 1, 9, 1, 1, 1]	,0)