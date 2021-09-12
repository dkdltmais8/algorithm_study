def solution(id_list, report, k):
    answer = []
    good = []
    bad = []
    candidate = []
    get_message = []
    res = []
    for i in report:
        a,b = i.split(" ")
        good.append(a)
        bad.append(b)
    # print(good,bad)
    for i  in range(len(bad)):
        if bad.count(bad[i]) >= k:
            candidate.append(bad[i])
    # print(list(set(candidate)))
    for r in list(set(candidate)):
        for i,v in enumerate(bad):
            if r == v:
                get_message.append(good[i])
        get_message = list(set(get_message))
        if len(get_message) >= k:
            res.append(get_message)
        get_message = []
    for i in id_list:
        cnt = 0
        for r in res:
            for c in r:
                if i == c:
                    cnt += 1
        answer.append(cnt)
    return print(answer)
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],	3)