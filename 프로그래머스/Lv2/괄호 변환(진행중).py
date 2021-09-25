def solution(p):
    answer = ''
    s = [0]
    u=''
    v = ''
    flag = False
    def check(p):
        for i in p:
            if i == '(':
                s.append(i)
            if i ==')' and s[-1] == '(':
                s.pop()
        if s == [0]:
            answer = p
        else:
            flag = True
        print(answer,flag)
    while flag:
        tot = 0
        res = ''
        for i in p:
            if i == '(':
                tot += 1
                res += i
            elif i == ')':
                tot -= 1
                res += i
            if tot == 0:
                break
        u = res
        v = p[len(u):]
        p = v
        answer += u
        if u
        print(u,v)


    return answer
solution("(()())()")
solution(")(")
solution("()))((()")