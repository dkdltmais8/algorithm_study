# c => 최소 증가 인원
# n => 도시 개수
def check(lst):
    global now
    for i in range(len(lst)):
        if lst[i] == min(lst):
            now = i
            return


c, n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
# print(arr)
now = 0
ans = 0
efficiency = []
for i in arr:
    efficiency.append(i[0]/i[1])
check(efficiency)
# print(efficiency)
while c>0:
    if c < arr[now][1]:
        efficiency.pop(now)
        arr.pop(now)
        check(efficiency)
    if c >= arr[now][1]:
        mok = c//arr[now][1]
        ans += mok*arr[now][0]
        c -= mok*arr[now][1]
        # efficiency.pop(now)
        # arr.pop(now)
        if c <= 0:
            break
    # elif c >= arr[now][1] and len(arr) == 1:
    #     mok = c // arr[now][1] +1
    #     ans += mok * arr[now][0]
    #     c -= mok * arr[now][1]
    #     # efficiency.pop(now)
    #     # arr.pop(now)
    #     if c <= 0:
    #         break
    check(efficiency)
print(ans)
##효율은 좋지만 최소인원보다 수가 작으면 실행 자체를 시킬 수 없음