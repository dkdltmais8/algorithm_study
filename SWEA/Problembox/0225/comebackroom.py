T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    room = [0]*201
    for _ in range(n):
        a, b = map(int, input().split())
        a = (a+1) >> 1
        b = (b+1) >> 1
        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            room[i] += 1

    print("#{} {}".format(tc, max(room)))