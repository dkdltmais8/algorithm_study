T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    if m == 0:
        result = 'OFF'
    elif m == 1 and n == 1:
        result = 'ON'
    else:
        for _ in range(n):
            if (m % 2) == 0:
                result = 'OFF'
                break
            m //= 2
        else:
            result = 'ON'
    print("#{} {}" .format(tc, result))



