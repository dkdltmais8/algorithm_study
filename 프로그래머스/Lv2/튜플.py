def solution(s):
    answer = []
    temp = [[] for _ in range(500)]
    idx = 0
    p = ''
    for i in s[1:-1]:
        if i =='{' :
            continue
        elif i=='}':
            temp[idx].append(p)
            idx += 1
            p = ''
            continue
        if i ==',':
            if p=='':
                continue
            else:
                temp[idx].append(p)
                p = ''
                continue
        p += i
    cnt = 0
    for i in temp:
        if len(i)>cnt:
            cnt = len(i)
        if i == []:
            break
    d = 1
    while len(answer) < cnt:
        for i in temp:
            if len(i) == d:
                for j in i:
                    if int(j) not in answer:
                        answer.append(int(j))
                        break
                d += 1
                break
    # print(answer)
    return answer
solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"	)
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"	)
solution("{{20,111},{111}}"	)
solution("{{123}}"	)
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"	)