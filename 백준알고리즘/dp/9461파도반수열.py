t = int(input())
ans = []
for tc in range(1, t+1):
    n = int(input())
    arr = [1,1,1,2,2,3,4,5,7,9]
    for i in range(10,n+1):
        arr.append(arr[i-2]+arr[i-3])
    ans.append(arr[n-1])
for i in ans:
    print(i)