def solution(s):
    answer = 0
    ans = []
    for i in s:
        if ans != [] and i == ans[-1]:
            ans.pop()
        else:
            ans.append(i)

    if not ans:
        answer = 1
    return answer
solution('baabaa')
solution('cdcd')