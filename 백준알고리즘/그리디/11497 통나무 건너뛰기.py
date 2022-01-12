for tc in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = []
    tot = 0
    for i in range(2,n):
        tot = max(tot,arr[i]-arr[i-2])
    print(tot)