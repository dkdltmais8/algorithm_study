T = int(input())
for tc in range(1, T+1):
    n = input()
    num = list(map(int,input().split()))
    com = dict(zip(set(num),[0]*len(set(num))))
    ans = []
    for i in num:
        com[i] += 1
    for value in com.values():
        ans.append(value)
    for key, value in com.items():
        if value == max(ans):
            print("#{} {}".format(tc,key))

