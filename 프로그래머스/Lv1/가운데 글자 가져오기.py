def solution(s):
    answer = ''
    d = len(s)
    if d%2==0:
        answer+=s[d//2-1:d//2+1]
    else:
        answer+=s[d//2]
    return answer