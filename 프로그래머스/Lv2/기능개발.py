def solution(progresses, speeds):
    answer = []
    d = len(progresses)
    cnt = [0]*d
    while progresses.count(100) < d:
        for i in range(d):
            if progresses[i] < 100:
                progresses[i] = progresses[i]+speeds[i]
                cnt[i] += 1
            else:
                progresses[i] = 100
                continue
    print(cnt)
    i = 0
    while i<d:
        tot = 1
        for j in range(i+1,d):
            if cnt[i] >= cnt[j]:
               tot += 1
            else:
                break
        answer.append(tot)
        i += tot
    print(answer)
    print(progresses,cnt)
    return answer
solution([93, 30, 55],[1, 30, 5])
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])