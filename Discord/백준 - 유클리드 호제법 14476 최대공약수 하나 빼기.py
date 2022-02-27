import sys
input = sys.stdin.readline
def check(a,b,now):
    tmp = 0
    while a:
        tmp = b%a
        b = a
        a = tmp
    return [b,now] if confirm(b,now) else [-1,-1]
def confirm(a,b):
    tmp = 0
    if a>b:
        tmp = a%b
    else:
        tmp = b%a
    if tmp == 0:
        return False
    else:
        return True
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
ans = []
for i in arr:
    for j in range(len(arr)-1):
        if i==arr[j]:
            continue
        ans.append(check(arr[j],arr[j+1],i))
answer = sorted(ans,key=lambda x:-x[0])[0]
print(*answer if answer != [-1,-1] else [-1])
