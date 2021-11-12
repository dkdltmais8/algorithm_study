def solution(s):
    answer = ''
    s=s.split()
    ans = []
    for i in s:
        ans.append(int(i))
    answer += str(min(ans))
    answer += ' '
    answer += str(max(ans))

    return answer
solution("1 2 3 4")
solution("-1 -2 -3 -4")
solution("-1 -1")