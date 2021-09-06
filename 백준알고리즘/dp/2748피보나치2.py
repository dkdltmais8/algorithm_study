n = int(input())
arr= [0,1,0]
tmp,cnt = 0,1
while cnt <= n:
    cnt += 1
    arr[2] = tmp+arr[1]
    arr[1] = tmp
    tmp = arr[2]
print(arr[2])
