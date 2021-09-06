T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mylist = list(map(int, input().split()))[::-1]
    answer = 0
    now_max = mylist[0]

    for j in range(1, N):
        if now_max > mylist[j]:
            answer += now_max - mylist[j]
        else:
            now_max = mylist[j]

    print("#{} {}".format(tc, answer))
