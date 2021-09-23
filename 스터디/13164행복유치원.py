def check():
    ans = []
    if n <= k:
        return 0
    else:
        for i in range(1,n):
            ans.append(arr[i]-arr[i-1])
    ans.sort()
    for i in range(k-1):
        ans.pop()
    return sum(ans)
n,k = map(int,input().split())
arr = list(map(int,input().split()))
# print(n,k,arr)
res = check()

print(res)