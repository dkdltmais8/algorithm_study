def solution(n):
    answer = 0
    lst = [1]*(n+1)
    d = int(n**0.5)
    for i in range(2,d+1):
        if lst[i] == 1:
            for j in range(i+i,n+1,i):
                lst[j] = 0
    lst[0],lst[1] = 0,0
    answer = lst.count(1)
    return answer
solution(10)
solution(5)