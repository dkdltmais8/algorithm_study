for _ in range(int(input())):
    S = []
    p = input()
    for i in p:
        if not S:
            S.append(i)
        else:
            if S[-1] != i:
                if S[-1] == ')':
                    break
                else:
                    S.pop()
            else:
                S.append(i)
    if S:
        print('NO')
    else:
        print('YES')