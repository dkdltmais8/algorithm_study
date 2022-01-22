arr = [0]
for i in range(6):
    arr.append(int(input()))
cnt = arr[-1]
while arr[5]>0:
    w = 11
    cnt += 1
    arr[5] -= 1
    arr[1] = max(arr[1]-w,0)
while arr[4]>0:
    w = 20
    w -= min(arr[2],5)*4
    arr[4] -= 1
    cnt += 1
    arr[2] = max(arr[2]-5,0)
    arr[1] = max(arr[1]-w,0)
while arr[3]>0:
    w = 36-9*min(4,arr[3])
    if arr[3]>=4:
        arr[3] -=4
    elif arr[3] == 3:
        arr[3] -= 3
        w -= min(1,arr[2])*4
        arr[2] = max(arr[2]-1,0)
    elif arr[3] == 2:
        arr[3] -= 2
        w -= min(3,arr[2])*4
        arr[2] = max(arr[2]-3,0)
    else:
        arr[3] -= 1
        w -= min(5, arr[2]) * 4
        arr[2] = max(arr[2] - 5, 0)
    arr[1] = max(arr[1]-w,0)
    cnt += 1
while arr[2]>0:
    w = 36-4*min(arr[2],9)
    arr[2] = max(arr[2]-9,0)
    arr[1] = max(arr[1]-w,0)
    cnt += 1
while arr[1] > 0:
    arr[1] = max(arr[1]-36,0)
    cnt += 1

print(cnt)