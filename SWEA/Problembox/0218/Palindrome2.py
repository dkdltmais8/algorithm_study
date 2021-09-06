for tc in range(1,11):
    n = int(input())
    string = [input() for i in range(100)]
    new_string = []
    ans = []
    rev = ''

    for r in range(100):
        for c in range(100):
            rev += string[c][r]
        new_string.append(rev)
        rev = ''

    for r in range(100):
        for c in range(100):
            for i in range(c,100):
                if string[r][c:i] == string[r][c:i][::-1]:
                    ans.append(string[r][c:i])

    for r in range(100):
        for c in range(100):
            for i in range(c,100):
                if new_string[r][c:i] == new_string[r][c:i][::-1]:
                    ans.append(new_string[r][c:i])
    high = len(ans[0])
    for i in range(len(ans)):
        if len(ans[i]) > high:
            high = len(ans[i])

    print("#{} {}".format(tc, high))


