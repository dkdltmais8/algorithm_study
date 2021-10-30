def solution(numbers):
    answer = ''
    d = len(numbers)
    res=[]
    for i in numbers:
        res.append(str(i))
    res.sort(reverse=True)
    for i in range(d-1):
        if 10<int(res[i])<100 and (int(res[i])%10)<int(res[i+1]) and int(res[i])//10 == int(res[i+1]):
            res[i+1],res[i] = res[i],res[i+1]
        if 100<int(res[i])<1000 and (int(res[i])%100)<int(res[i+1]) and int(res[i])//100 == int(res[i+1]):
            res[i+1],res[i] = res[i],res[i+1]
    for i in res:
        answer+=i
    print(answer)
    return answer
solution([3,30,34,6,9])
solution([6,10,2])