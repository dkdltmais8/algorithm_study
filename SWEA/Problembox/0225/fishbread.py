T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int,input().split())
    guest = sorted(list(map(int,input().split())))
    cnt = 0
    for i in range(n):
        if (guest[i] // m) * k-i >= 1:
            cnt += 1
        else:
            cnt = 0
            break

    if cnt >= 1:
        print('#{} Possible'.format(tc))
    else:
        print("#{} Impossible".format(tc))

