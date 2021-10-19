def solution(s):
    answer = ''
    s = list(s.split(' '))
    # print(s)
    for i in s:
        for j in range(len(i)):
            if j % 2 != 0:
                answer += i[j].lower()
            else:
                answer+= i[j].upper()
        answer += ' '
    # print(answer)
    if answer[-1] == ' ':
        answer = answer[:-1]
    return answer
solution("try hello world")