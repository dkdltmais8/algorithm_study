T = int(input())
for i in range(T):
    N = int(input())
    cnt = [0,0,0,0,0]
    while N % 2 == 0:
        N //= 2
        cnt[0] += 1
    while N % 3 == 0:
        N //= 3
        cnt[1] += 1
    while N % 5 == 0:
        N //= 5
        cnt[2] += 1
    while N % 7 == 0:
        N //= 7
        cnt[3] += 1
    while N % 11 == 0:
        N //= 11
        cnt[4] += 1
    print(f"#{i+1}",end=" ")
    for j in range(5):
        print(f"{cnt[j]}",end=' ')
    print()