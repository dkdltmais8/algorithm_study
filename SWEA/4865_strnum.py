def my_max(a):
    max_num = a[0]
    for i in range(1, len(a)):
        if a[i] >= max_num:
            max_num = a[i]
    return max_num

T = int(input())
for tc in range(1,T+1):
    a = input()
    b = input()
    ans = []
    for j in a:
        cnt = 0
        for i in b:
            if j == i:
                cnt += 1
        ans.append(cnt)
    print("#{} {}".format(tc, my_max(ans)))