import sys
input = sys.stdin.readline
n, w = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr1 = []
arr2 = []
for i in arr:
    if i[0] == 3:
        arr1.append(i)
    else:
        arr2.append(i)
arr1.sort(key=lambda x:-x[1])
arr2.sort(key=lambda x:-x[1])
dp1 = [0]
dp2 = [0]
for i in range(len(arr1)):
    dp1.append(dp1[i]+ arr1[i][1])
for i in range(len(arr2)):
    dp2.append(dp2[i]+ arr2[i][1])
min3 = min(w//3,len(arr1))
ans = 0
while min3>=0:
    min5 = min((w-min3*3)//5,len(arr2))
    ans = max(ans,dp1[min3]+dp2[min5])
    min3 -= 1
print(ans)