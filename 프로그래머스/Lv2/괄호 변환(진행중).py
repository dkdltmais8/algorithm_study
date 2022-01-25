def makeu(string):
    if string == '':
        return ''
    c1, c2 = 0, 0
    for i in range(len(string)):
        if string[i] == '(':
            c1 += 1
        else:
            c2 += 1
        if c1 == c2:
            return string[:i + 1], string[i + 1:]
def check(m):
    s = []
    for i in m:
        if i ==')':
            if not s:
                return False
            s.pop()
        if i =='(':
            s.append(i)
    return True
def solution(p):
    answer = ''
    if p == "":
        return p
    u,v = makeu(p)
    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for i in u[1:len(u)-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer
# solution("(()())()")
# solution(")(")
solution("()))((()")