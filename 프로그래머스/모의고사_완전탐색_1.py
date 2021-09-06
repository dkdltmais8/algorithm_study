def solution(answers):
    global cnt
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            cnt[1] += 1
        if answers[i] == p2[i]:
            cnt[2] += 1
        if answers[i] == p3[i]:
            cnt[3] += 1
    answer = []
    return answer,cnt
cnt=[0,0,0,0]
p1 = [1,2,3,4,5]*2000
p2 = [2,1,2,3,2,4,2,5,2,1]*1000
p3 = [3,3,1,1,2,2,4,4,5,5] * 1000
answers = list(map(int,input()))
print(solution(answers))