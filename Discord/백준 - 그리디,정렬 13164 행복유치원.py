import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = []
if n<=k:
    ans.append(0)
else:
    for i in range(1,n):
        ans.append(arr[i]-arr[i-1])
    ans.sort()
    for i in range(k-1):
        ans.pop()

print(sum(ans))