n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],-x[0]))
w,c = 0,0
lst = []
for i in range(n):
    w += arr[i][0]
    if i>=1 and arr[i][1] == arr[i-1][1]:
        c += arr[i][1]
    else:
        c = arr[i][1]
    if w>=m:
        lst.append(c)
        if c == arr[i][1]:
            break
if lst:
    print(min(lst))
else:
    print(-1)