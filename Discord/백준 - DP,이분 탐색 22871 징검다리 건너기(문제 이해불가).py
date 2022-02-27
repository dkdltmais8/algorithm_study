import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
dp = [float('inf')]*n
i=0
for j in range(i+1,n):
    dp[j] =min(dp[j],(j-i)*(1+abs(arr[j]-arr[i])))
print(dp)