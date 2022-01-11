T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int,input().split()))
    now = arr[-1]
    tot = 0
    for i in range(n-2,-1,-1):
        if arr[i]<now:
            tot += now-arr[i]
        else:
            now = arr[i]
    print(tot)