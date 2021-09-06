T = int(input())
for i in range(T):
    result =[]
    N, M = map(int, input().split())
    for j in range(N,M+1,N):
        result.append(j)
    print(f'#{i+1}',end=' ')
    for j in result:
        print(f"{j}", end=' ')
    print()