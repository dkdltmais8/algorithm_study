import copy
def change1(arr):
    cnt = 1
    arr[0],arr[1] = 1-arr[0], 1-arr[1]
    for i in range(1,n):
        if arr[i-1] == end[i-1]:
            continue
        else:
            cnt += 1
            if i == n-1:
                arr[i - 1], arr[i] = 1-arr[i-1],1-arr[i]

            else:
                arr[i-1],arr[i],arr[i+1] = 1-arr[i-1],1-arr[i],1-arr[i+1]
    if arr == end:
        return cnt
    return 987654321
def change2(arr):
    cnt = 0
    for i in range(1, n):
        if arr[i - 1] == end[i - 1]:
            continue
        else:
            cnt += 1
            if i == n - 1:
                arr[i - 1], arr[i] = 1 - arr[i - 1], 1 - arr[i]

            else:
                arr[i - 1], arr[i], arr[i + 1] = 1 - arr[i - 1], 1 - arr[i], 1 - arr[i + 1]
    if arr == end:
        return cnt
    return 987654321
n = int(input())
now = list(map(int,input()))
end = list(map(int,input()))
c1,c2 = copy.deepcopy(now),copy.deepcopy(now)
cnt1 = change1(c1)
cnt2 = change2(c2)
answer = min(cnt1,cnt2)
if answer!=987654321:
    print(answer)
else:
    print(-1)
