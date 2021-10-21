def solution(n):
    answer = []
    n = str(n)
    d= len(n)
    for i in range(d-1,-1,-1):
        answer.append(int(n[i]))
    return answer