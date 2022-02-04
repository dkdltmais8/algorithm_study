from itertools import combinations
from bisect import bisect_left
def solution(info, query):
    answer = []
    dic = {}
    for i in range(len(info)):
        info[i] = info[i].split(' ')
        k = info[i][:-1]
        v = info[i][-1]
        for j in range(5):
            for c in combinations(k,j):
                tmp = ''.join(c)
                if tmp in dic:
                    dic[tmp].append(int(v))
                else:
                    dic[tmp] = [int(v)]
    for i in dic:
        dic[i].sort()
    for i in query:
        a = i.split(' ')
        k = a[:-1]
        v = a[-1]
        while 'and' in k:
            k.remove('and')
        while '-' in k:
            k.remove('-')
        k = ''.join(k)
        if k in dic:
            score = dic[k]
            if score:
                idx = bisect_left(score,int(v))
                answer.append(len(score)-idx)
            else:
                answer.append(0)
        else:
            answer.append(0)
    # print(answer)

    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])