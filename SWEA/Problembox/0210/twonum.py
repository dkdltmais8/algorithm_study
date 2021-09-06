T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    result = []
    ans = []
    if N > M:
        for k in range(N - M + 1):
            for j in range(k,  M + k):
                result.append(B[j-k] * A[j])
            ans.append(sum(result))
            result = []
    else:
        for k in range(M - N + 1):
            for j in range(k,  N + k):
                result.append(A[j-k] * B[j])
            ans.append(sum(result))
            result = []
    print(f'#{i+1} {max(ans)}')