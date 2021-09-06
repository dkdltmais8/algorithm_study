T = int(input())

for tc in range(1, T+1):
    N = int(input())
    base = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    for i in range(len(base)):
        while N > 1:
            if N % base[i] == 0:
                N //= base[i]
                cnt[i] += 1
            else:
                break
    ans = ' '.join(map(str, cnt))
    print(f'#{tc} {ans}')

