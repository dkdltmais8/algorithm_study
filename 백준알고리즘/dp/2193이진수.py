n = int(input())
arr = [1,1,2,3,5]
for i in range(5,n+1):
    arr.append(arr[i-2]+arr[i-1])
print(arr[n-1])