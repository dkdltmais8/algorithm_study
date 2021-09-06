n = int(input())
arr = [1,1,3,5]
for i in range(4,n+1):
    arr.append(arr[i-1]+arr[i-2]+1)
print(arr[n]%1000000007)