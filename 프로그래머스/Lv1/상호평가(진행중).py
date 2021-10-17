def solution(scores):
    answer = ''
    n =len(scores)
    res = [0]*n
    store = [0]*n
    for i in range(n):
        max_cnt,min_cnt = 0,0
        max_score,min_score = 0,100
        for j in range(n):
            if scores[j][i] > max_score:
                max_score = scores[j][i]
            if scores[j][i] < min_score:
                min_score = scores[j][i]
        for j in range(len(scores[i])):
            if max_score == scores[i][i] and max_score != scores[j][i]:
                max_cnt += 1
            elif min_score ==scores[i][i] and min_score != scores[j][i]:
                min_cnt += 1
        if max_cnt > 0 or min_cnt > 0:
            store[i] = 1
    for i in range(len(scores)):
        if store[i] == 1:
            scores[i][i] = 0
    # print(scores)
    for i in range(n):
        for j in range(n):
            res[i] += scores[j][i]
    for i in range(n):
        if store[i] == 1:
            res[i] = res[i]/(n-1)
        else:
            res[i] = res[i]/n
    for i in res:
        if i>= 90:
            answer+='A'
        elif 90>i>=80:
            answer+='B'
        elif 80>i>=70:
            answer+='C'
        elif 70>i>=50:
            answer+='D'
        else:
            answer+='F'
    return answer
solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
solution([[50,90],[50,87]])
solution([[70,49,90],[68,50,38],[73,31,100]])