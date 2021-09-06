T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    idx_max = 0
    idx_min = 0
    for i in range(len(num)):
        if num[i] == max(num):
            idx_max = i

    for i in range(len(num)):
        if num[i] == min(num):
            idx_min = i
            break
    result = idx_max - idx_min
    if result < 0:
        result *= -1
    print("#{} {}".format(tc, result))