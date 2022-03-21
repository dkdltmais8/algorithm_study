def check(num):
    global ans
    for i in range(2,int(num**0.5)+1):
        if ans[i]:
            for j in range(i+i,num+1,i):
                ans[j] = 0
n = int(input())
cnt = 0
arr = list(map(int,input().split()))
ans = [1]*(max(arr)+1)
ans[0],ans[1] = 0,0
check(max(arr))
for i in arr:
    if ans[i]:
        cnt += 1
print(cnt)