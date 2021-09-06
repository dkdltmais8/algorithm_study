n = int(input())
arr = list(map(int,input().split()))
ans = []
cnt = 1
length = 1
for i in range(1,n):
    if arr[i] <= arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    if length < cnt:
        length = cnt

cnt = 1

for i in range(1,n):
    if arr[i] >= arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    if length < cnt:
        length = cnt
print(length)