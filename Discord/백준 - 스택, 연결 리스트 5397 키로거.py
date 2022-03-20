for _ in range(int(input())):
    a = input()
    ans = []
    store = []
    for i in a:
        if i =='<':
            if ans:
                store.append(ans.pop())
        elif i == '>':
            if store:
                ans.append(store.pop())
        elif i =='-':
            if ans:
                ans.pop()
        else:
            ans.append(i)
    ans.extend(reversed(store))
    print(''.join(ans))