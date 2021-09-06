for tc in range(int(input())):
    N , Q = map(int, input().split())
    ans = [0] * N
    cnt = []
    for j in range(1,Q+1):
        L, R = map(int, input().split())
        cnt.append(j)
        for k in range(L-1,R):
            ans[k] = cnt[j-1]
    print(f"#{tc+1} {' '.join(map(str, ans))}")


