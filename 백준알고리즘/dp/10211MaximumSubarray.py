T = int(input())
for tc in range(1, T+1):
    n = int(input())
    ans = []
    arr = list(map(int,input().split()))
    for i in range(n):
        tot = 0
        for j in range(i,n):
            tot += arr[j]
            ans.append(tot)
    for i in range(n):
        tot = 0
        for j in range(0,n-i):
            tot += arr[j]
            ans.append(tot)
    print(max(ans))