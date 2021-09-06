T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    print(f"#{i+1}")
    if M == 1:
        for j in range(1,N+1):
            print('*'*j)
    elif M == 2:
        for j in range(N,0,-1):
            print('*'*j)
    elif M == 3:
        for j in range(1,N+1):
            print(' '*(N-j),end='')
            print('*'*((2*j)-1))


