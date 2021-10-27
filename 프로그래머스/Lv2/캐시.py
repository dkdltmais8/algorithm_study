from collections import deque
def solution(cacheSize, cities):
    answer = 0
    lst = deque()
    for j in cities:
        j = j.lower()
        if j in lst:
            answer +=1
            if len(lst) == cacheSize:
                lst.remove(j)
            lst.append(j)
        else:
            answer +=5
            if len(lst) == cacheSize and cacheSize !=0:
                lst.popleft()
            if cacheSize != 0:
                lst.append(j)
    print(answer)
    return answer
solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3,	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(5,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2,	["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])