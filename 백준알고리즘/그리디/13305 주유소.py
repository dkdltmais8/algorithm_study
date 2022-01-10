n = int(input())
d = list(map(int,input().split()))
oil = list(map(int,input().split()))
now = oil[0]
tot = 0
for i in range(n-1):
    if oil[i]< now:
        now = oil[i]
    tot += now*d[i]
print(tot)