def solution(n, times):
    answer = 0
    l,r = 1,max(times)*n
    while l<=r:
        mid = (l+r)//2
        tot = 0
        for i in times:
            tot += mid//i
            if tot>=n:
                break
        if tot >=n:
            answer = mid
            r = mid-1
        else:
            l = mid+1
    return answer
solution(6,[7,10])
solution(3,[1,1,1])
solution(3,[1,2,3])