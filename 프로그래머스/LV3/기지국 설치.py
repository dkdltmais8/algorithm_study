import math
def solution(n, stations, w):
    answer = 0
    local = []
    for i in range(1,len(stations)):
        local.append((stations[i]-w-1)-(stations[i-1]+w))
    local.append(stations[0]-w-1)
    local.append(n-(stations[-1]+w))
    num = 2*w+1
    for i in local:
        if i <= 0:
            continue
        if i <=num:
            answer += 1
        else:
            answer += math.ceil(i/num)
    return answer
solution(11,[4,11],1)
solution(16,[9],2)