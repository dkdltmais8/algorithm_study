def solution(clothes):
    answer = 0
    dic = dict()
    ans = []
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = [i[0]]
        else:
            dic[i[1]].append(i[0])
    # print(dic)
    for i in dic.values():
        ans.append(len(i)+1)
    # print(ans)
    cnt = 1
    for i in ans:
        cnt = cnt*i
    cnt -= 1
    answer = cnt
    return answer
solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])