T = int(input())
for i in range(T):
    N = int(input())
    print(f'#{i+1}')
    for j in range(1,N+1):
        print(" "*(N-j),end='')
        print('*'*j)

