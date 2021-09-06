point = [list(map(int, input().split())) for _ in range(5)]
ans = []
for i in range(5):
    tot = 0
    for j in range(4):
        tot += point[i][j]
    ans.append(tot)
for i in range(len(ans)):
    if ans[i] == max(ans):
        print("{} {}".format(i+1,ans[i]))