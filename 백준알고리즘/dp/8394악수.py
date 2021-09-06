n = int(input())
arr = [0]*(n+1)
arr[1:7] = 2,3,5,8,3,1
##문제 좀 잘 읽자...
for i in range(7,n+1):
    arr[i] = (arr[i-1]+arr[i-2])%10
print(arr[n-1])
