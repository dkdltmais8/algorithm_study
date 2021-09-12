def solution(answers):
    answer = []
    res = [0,0,0,0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if p1[i%5] == answers[i]:
            res[1] += 1
        if p2[i%8] == answers[i]:
            res[2] += 1
        if p3[i%10] == answers[i]:
            res[3] += 1
    max_res = max(res)
    for i in range(1,4):
        if res[i] == max_res:
            answer.append(i)
    return answer

solution([1,2,3,4,5])