from collections import deque
n,m,t = map(int,input().split())
arr = [[]]
order = []
for i in range(n):
    arr.append(deque(list(map(int,input().split()))))
for i in range(t):
    order.append(list(map(int,input().split())))
#돌리기
for i in order:
    for j in range(i[0],n+1,i[0]):
        for k in range(i[2]):
            if i[1] == 0:
                arr[j].appendleft(arr[j].pop())
            else:
                arr[j].append(arr[j].popleft())
print(arr,order)
#같은 숫자 있는지 체크하기
def check(lst):
    for i in range(len(lst)):
        for j in range(len(i))
#같은 숫자들 x로 만들어버리기
def cal(lst):
    for i in lst:
        a,b = i
        arr[a][b] = 0
    tot = 0
    cnt = 0
    for i in arr:
        for j in i:
            if j != 0:
                tot += j
                cnt += 1
    middle = tot//cnt
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0 and arr[i][j]<middle:
                arr[i][j] += 1
            elif arr[i][j]>middle:
                arr[i][j] -= 1



