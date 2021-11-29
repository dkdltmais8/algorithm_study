def solution(genres, plays):
    answer = []
    dic = dict()
    lst = []
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]]=[plays[i]]
        else:
            dic[genres[i]].append(plays[i])
    # print(dic)
    dic = sorted(dic.items(), key=lambda x: sum(x[1]),reverse=True)
    # print(dic)
    for i in dic:
        i[1].sort(reverse=True)
    # print(dic)
    for i  in dic:
        cnt = 0
        for j in i[1]:
            if cnt == 2:
                break
            lst.append(j)
            cnt+=1
    print(dic)
    print(lst)
    for i in lst:
        first = plays.index(i)
        if first not in answer:
            answer.append(first)
        else:
            answer.append(plays.index(i,first+1))
    # print(answer)
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "pop", "test"], [500, 600, 150, 800, 2500, 100]))
print(solution(["classic"], [300]))