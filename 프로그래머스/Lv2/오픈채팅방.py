def solution(record):
    answer = []
    dic = dict()
    ans = '님'
    for i in record:
        i = i.split(' ')
        if i[0] =="Enter":
            answer.append(f"{i[1]}님이 들어왔습니다.")
            dic[i[1]] = i[2]
        elif i[0] == "Leave":
            answer.append(f"{i[1]}님이 나갔습니다.")
        elif i[0] == "Change":
            dic[i[1]] = i[2]
    # print(dic)
    # print(record)
    # print(answer)
    res = []
    for i in answer:
        i = i.split('님')
        if i[0] in dic:
            res.append(dic[i[0]]+ans+i[1])
            print(i[0],dic[i[0]])
    return res
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])