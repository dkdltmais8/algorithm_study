def solution(n):
    answer = ''
    n = str(n)
    n=list(n)
    n.sort(reverse=True)
    # print(n)
    for i in n:
        answer += i

    return int(answer)
solution(118372)