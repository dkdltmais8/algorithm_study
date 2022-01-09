from itertools import combinations
def check():
    global ans,lst
    for i in range(1,n+1):
        for com in combinations(range(1,n+1),i):
            a,b,c,d,tot = 0,0,0,0,0
            for j in com:
                a += candidate[j-1][0]
                b += candidate[j-1][1]
                c += candidate[j-1][2]
                d += candidate[j-1][3]
                tot += candidate[j-1][4]
            if a>=plan[0] and b>=plan[1] and c>=plan[2] and d>=plan[3]:
                if ans>tot:
                    ans = tot
                    lst = com
                elif ans == tot:
                    lst = sorted((lst,com))[0]
n = int(input())
plan = list(map(int,input().split()))
candidate = [list(map(int,input().split())) for _ in range(n)]
lst = []
ans = 987654321
check()
if ans == 987654321:
    print(-1)
else:
    print(ans)
    print(*lst)

