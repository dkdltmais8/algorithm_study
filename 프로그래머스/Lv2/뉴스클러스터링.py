def solution(str1, str2):
    answer = 0
    d1 = len(str1)
    d2 = len(str2)
    ans1,ans2 = [],[]
    res1,res2 = dict(),dict()
    for i in range(d1-1):
        if str1[i].isalpha()and str1[i+1].isalpha():
            ans1.append(str1[i].lower()+str1[i+1].lower())
    for i in range(d2 - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            ans2.append(str2[i].lower() + str2[i + 1].lower())
    # print(ans1,ans2)
    for i in ans1:
        if i in res1:
            res1[i]+=1
        else:
            res1[i] = 1
    for i in ans2:
        if i in res2:
            res2[i] += 1
        else:
            res2[i] = 1
    # print(res1,res2)
    tot1,tot2,tot3 = 0,0,0
    for i in res1:
        if i in res2:
            tot1 += min(res1[i],res2[i])
            tot2 += max(res1[i],res2[i])
        else:
            tot3 += res1[i]
    for i in res2:
        if i in res1:
            tot1 += min(res1[i],res2[i])
            tot2 += max(res1[i],res2[i])
        else:
            tot3 += res2[i]
    tot1 //= 2
    tot2 //= 2
    tot3 = tot3+tot2
    # print(tot1,tot3)
    if tot3 != 0:
        answer = int((tot1/tot3)*65536)
    else:
        answer = 65536
    # print(answer)
    return answer
solution('FRANCE',	'french')
solution('aa1+aa2','AAAA12')