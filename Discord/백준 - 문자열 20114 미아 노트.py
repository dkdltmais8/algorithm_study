n,h,w = map(int,input().split())
arr = [list(map(str,input())) for _ in range(h)]
ans = ["?" for _ in range(n)]
for i in range(h):
    for j in range(0,n*w,w):
        for k in range(j,j+w):
            if arr[i][k] != "?":
                ans[j//w] = arr[i][k]
print(''.join(ans))
