n = int(input())
arr = list(map(str,input()))
r = arr.count('R')
b = arr.count('B')
good = min(r,b)
cnt = 0
for i in range(n):
    if arr[i]  != arr[0]:
        break
    cnt+=1
if arr[0] == 'R':
    good = min(good,r-cnt)
else:
    good = min(good,b-cnt)
cnt = 0
for i in range(n-1,-1,-1):
    if arr[i] != arr[-1]:
        break
    cnt+= 1
if arr[-1]=='R':
    good = min(good,r-cnt)
else:
    good = min(good,b-cnt)
print(good)