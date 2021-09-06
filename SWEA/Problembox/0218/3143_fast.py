T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())
    cnt = 0
    if b in a:
        c = a.count(b)
        a = a.replace(b,'')

    result = len(a)+c
    print("#{} {}".format(tc,result))