for tc in range(1, int(input())+1):
    string = list(map(str, input().split()))
    S = []
    n = len(string)
    try:
        for i in range(n):

            if string[i] == '+':
                if len(S) <= 1:
                    print("#{} error".format(tc))
                    break
                else:
                    a = S.pop()
                    b = S.pop()
                    ans = b + a
                    S.append(ans)
            elif string[i] == '*':
                if len(S) <= 1:
                    print("#{} error".format(tc))
                    break
                else:
                    a = S.pop()
                    b = S.pop()
                    ans = b * a
                    S.append(ans)
            elif string[i] == '-':
                if len(S) <= 1:
                    print("#{} error".format(tc))
                    break
                else:
                    a = S.pop()
                    b = S.pop()
                    ans = b - a
                    S.append(ans)
            elif string[i] == '/':
                if len(S) <= 1:
                    print("#{} error".format(tc))
                    break
                else:
                    a = S.pop()
                    b = S.pop()
                    ans = b // a
                    S.append(ans)
            elif string[i] == '.':
                if len(S) >= 2 or len(S) == 0:
                    print("{} error".format(tc))
                else:
                    print("#{} {}".format(tc,S.pop()))
            else:
                S.append(int(string[i]))
    except:
        print("{} error".format(tc))

