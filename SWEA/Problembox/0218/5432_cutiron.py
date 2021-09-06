T = int(input())
for tc in range(1, T+1):
    iron = input()
    ans = []
    cnt = 0
    cut = 0
    for i in range(len(iron)):
        if iron[i] == '(':
            cut += 1
        else:
            if iron[i-1] == '(':
                cut -= 1
                cnt += cut
            else:
                cnt += 1
                cut -= 1
    print("#{} {}".format(tc,cnt))



