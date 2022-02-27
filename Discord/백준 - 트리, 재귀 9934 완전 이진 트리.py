def make(arr,m,idx):
    global ans
    if arr == []:
        return
    ans[idx].append(arr[m])
    make(arr[0:m],(m-1)//2,idx+1)
    make(arr[m+1:],(m-1)//2,idx+1)

k = int(input())
arr = list(map(int,input().split()))
ans = [[] for _ in range(k)]
#최상위 노드
m = len(arr)//2
make(arr,m,0)
for i in ans:
    print(*i)
