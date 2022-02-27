T = int(input())
for i in range(T):
    ans = ""
    p = list(map(str,input().split()))
    lst= []
    while 1:
        a = list(map(str,input().split()))
        if len(a) == 5:
            break
        lst.append(a[2])
    for i in p:
        if i in lst:
            continue
        ans+= i
        ans += ' '
    print(ans)