def solution(x, n):
    answer = []
    n = x*n
    if x<n:
        for i in range(x,n+1,x):
            answer.append(i)
    elif x==n:
        answer.append(x)
    else:
        for i in range(x,n-1,x):
            answer.append(i)
    return answer