T = int(input())
for i in range(T):
    N = int(input())
    N_li = list(map(int, input().split()))
    min_N = N_li[0]
    cnt = 0
    for j in range(1,N):
        if N_li[j] < min_N:
            N_li[j - 1] = N_li[j]
            N_li[j] = min_N
            max_N = N_li[j]
            cnt += 1
        else:
            min_N = N_li[j]
    print(f"#{i+1} {cnt}")


