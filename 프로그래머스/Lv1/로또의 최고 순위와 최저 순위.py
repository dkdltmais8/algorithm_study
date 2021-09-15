def solution(lottos, win_nums):
    answer = []
    cnt,o = 0,0
    for i in range(6):
        if lottos[i] in win_nums:
            cnt += 1
        if lottos[i] == 0:
            o += 1
    res = cnt + o
    if res == 6:
        answer.append(1)
    elif res == 5:
        answer.append(2)
    elif res == 4:
        answer.append(3)
    elif res == 3:
        answer.append(4)
    elif res == 2:
        answer.append(5)
    else:
        answer.append(6)
    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer
solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])