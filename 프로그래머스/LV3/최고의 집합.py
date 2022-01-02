def solution(n, s):
    answer = []
    mok = s//n
    nam = s%n
    if mok < 1:
        answer = [-1]
    else:
        for _ in range(n-nam):
            answer.append(mok)
        for _ in range(nam):
            answer.append(mok+1)
    return answer