import sys
input = sys.stdin.readline
x = []
y = []
tc = int(input())
for _ in range(tc):
    r,c = map(int,input().split())
    x.append(r)
    y.append(c)
x.sort()
y.sort()
a = x[tc//2]
b = y[tc//2]
tot = 0
for i in range(tc):
    tot += abs(a-x[i])
    tot += abs(b-y[i])
print(tot)