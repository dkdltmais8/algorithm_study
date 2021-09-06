import itertools
n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans = sorted(list(set(itertools.permutations(arr,m))))
for i in ans:
    for j in i:
        print(j,end=' ')
    print()