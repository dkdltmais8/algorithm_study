for tc in range(1,11):
    n = int(input())
    p = input()
    t = input()
    cnt = 0
    for j in range(len(t)):
        if p == t[j:j+len(p)]:
            cnt += 1
    print("#{} {}".format(tc,cnt))
