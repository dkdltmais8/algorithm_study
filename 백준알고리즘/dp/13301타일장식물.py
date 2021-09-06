n = int(input())
arr = [4,6]
for i in range(2,n+1):
    arr.append(arr[i-2]+arr[i-1])
print(arr[n-1])