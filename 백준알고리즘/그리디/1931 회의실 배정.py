n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1]))
time = []
cnt = 0
for i in range(n):
    if  arr[i][0] in time:
        continue
    else:
        cnt += 1
        for j in range(arr[i][0],arr[i][1]):
            time.append(j)
print(cnt)
