n = int(input())
arr = [1,2,3,5]
for i in range(4,n+1):
    arr.append((arr[i-1]+arr[i-2])%15746)
print(arr[n-1])