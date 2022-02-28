from itertools import permutations
import sys
input = sys.stdin.readline
def check(n):
    lst = [1]*(n)
    m = int(n**0.5)
    for i in range(2,m+1):
        if lst[i] == 1:
            for j in range(i+i,n,i):
                lst[j] = 0
    lst[0],lst[1] = 0,0
    return [i for i in range(len(lst)) if lst[i] == 1]
def one(lst,n):
    for i in lst:
        for j in lst:
            if i == j:
                continue
            if i+j>=n:
                continue
            S[i+j] = 1
def two(lst,n):
    for i in lst:
        for j in lst:
            if i*j>=n:
                continue
            M[i*j] = 1

k,m = map(int,input().split())
a = [0,10,99,988,9877,98766]
S,M = [0]*a[k],[0]*a[k]
p = check(a[k])
one(p,a[k])
two(p,a[k])
cnt = 0
print(S,M)
for i in range(a[k]):
    if S[i] == 1 and M[i] == 1:
        cnt += 1
print(cnt)


