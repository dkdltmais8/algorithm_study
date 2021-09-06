import itertools
n, k = map(int,input().split())
N = list(map(int,input().split()))
ans = list(itertools.permutations(N,n))
cnt = 0
for i in ans:
    weight = 500
    for j in i:
        weight = weight-k+j
        if weight < 500:
            cnt += 1
            break
print(len(ans)-cnt)
