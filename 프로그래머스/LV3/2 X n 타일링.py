def solution(n):
    answer = 0
    lst = [0,1,2,2,3,4]
    for i in range(6,n+1):
        lst.append(lst[i-2]+lst[i-3])
    answer = lst[n]%1000000007
    return answer