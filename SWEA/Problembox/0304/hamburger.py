def diet(idx,point,kcal):
    global ans
    if kcal > l:
        return
    if point > ans:
        ans = point
    for i in range(idx,n):
        print(i+1, point+info[i][0], kcal + info[i][1])
        diet(i+1, point+info[i][0], kcal + info[i][1])
T = int(input())
for tc in range(1, T+1):
    n, l = map(int,input().split())
    info = [tuple(map(int,input().split())) for _ in range(n)]
    ans = 0
    diet(0,0,0)
    print(info[1])
    print("#{} {}".format(tc, ans))