def change_pizza():
    if pizza:
        return pizza.pop(0)
    else:
        return 0
T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    Ci = list(map(int,input().split()))
    oven = []
    pizza = [[i,Ci[i-1]] for i in range(1, m+1)]
    oven = [pizza.pop(0) for _ in range(n)]

    while oven.count(0) < n:
        plate = oven.pop(0)
        if plate == 0:
            oven.append(change_pizza())
        else:
            plate[1] //= 2
            if plate[1] == 0:
                out = plate[0]
                oven.append(change_pizza())
            else:
                oven.append(plate)
    print("#{} {}".format(tc, out))
