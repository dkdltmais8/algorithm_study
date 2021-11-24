def solution(s):
    answer = ''
    s = s.split(' ')
    for i in s:
        answer += i.capitalize()
        answer +=' '
    answer = answer[:-1]

    return answer
solution("3people unFollowed me")
solution("for the last week")