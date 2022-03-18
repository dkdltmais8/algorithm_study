from collections import defaultdict
n,m = map(int,input().split())
arr = [list(map(str,input())) for _ in range(n)]
ans = ""
cnt = 0
for i in range(m):
    dic = defaultdict(int)
    for j in range(n):
        dic[arr[j][i]] += 1
    dic = sorted(dic.items(),key= lambda x:(-x[1],x[0]))
    ans += dic[0][0]
    if dic[0][1] == n:
        continue
    else:
        for i in dic[1:]:
            cnt += i[1]
print(ans)
print(cnt)
