def solution(n):
    def move(s,e,m,n):
        nonlocal answer
        if n == 1:
            return answer.append([s,e])
        move(s,m,e,n-1)
        answer.append([s,e])
        move(m,e,s,n-1)
    answer = []
    move(1,3,2,n)
    return answer