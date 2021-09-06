for tc in range(1, 11):
    n = int(input())
    board = input()
    operator ={'+' : 0 ,
               '*' : 1,}
    s = []
    res = ''
    for i in board:
        if i == '+' or i == '*':
            if len(s) == 0:
                s.append(i)
            else:
                while True:
                    com = s.pop()
                    if operator[i] > operator[com]:
                        s.append(com)
                        s.append(i)
                        break
                    else:
                        res += com
                    if len(s) == 0:
                        s.append(i)
                        break
        else:
            res += i
    while len(s) != 0:
        res += s.pop()
    for i in res:
        if i == '+' or i == '*':
            B = s.pop()
            A = s.pop()
            if i == '+':
                i = A + B
            else:
                i = A * B
            s.append(i)
        else:
            s.append(int(i))
    print('#{} {}'.format(tc, s.pop()))


