n = int(input())
arr = [1,1,1,2,3,4,6,9,13,19]
for i in range(10,n):
    arr.append(arr[i-1]+arr[i-3])
print(arr[n-1])