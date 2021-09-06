import itertools
n,s = map(int,input().split())
arr1 = list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    ans = list(itertools.combinations(arr1,i))
    for j in ans:
        if sum(j) == s:
            cnt += 1
print(cnt)
