T = int(input())

for i in range(T):
    result = []
    N = int(input())
    for j in range(N,0,-1):
        if N % j == 0:
            result.append(j)
    print(f"#{i+1}",end=' ')
    for j in result:
        print(f"{j}",end=' ')
    print()
