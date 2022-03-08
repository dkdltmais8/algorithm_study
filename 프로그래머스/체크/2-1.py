def solution(s):
    answer = ''
    s = list(map(int,s.split()))
    s.sort()
    answer += str(s[0])
    answer += ' '
    answer += str(s[-1])
    return answer
solution("1 2 3 4")