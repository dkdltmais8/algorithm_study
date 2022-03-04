n,k = map(int,input().split())
arr = list(map(int,input().split()))
tot = sum(arr)
if k >= tot:
    k -= tot
    for i in range(n-1,-1,-1):
        k -= arr[i]
        if k<0:
            print(i+1)
            break
else:
    for i in range(n):
        k -= arr[i]
        if k<0:
            print(i+1)
            break