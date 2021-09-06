T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    order = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if order[i] != 0:
            ans.append(order[i])
        else:
            ans.pop()
    print("#{} {}".format(tc, sum(ans)))
