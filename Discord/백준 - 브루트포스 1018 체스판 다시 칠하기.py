def check(r,c):
    global tot
    cntw = 0
    cntb = 0
    for i in range(r,r+8):
        for j in range(c,c+8):
            #시작이 검정인 경우
            if (i+j)%2 == 0:
                if lst[i][j] != 'W':
                    cntw += 1
                if lst[i][j] != "B":
                    cntb += 1
            #시작이 흰색인 경우
            else:
                if lst[i][j] != 'B':
                    cntw += 1
                if lst[i][j] != "W":
                    cntb += 1
    tot = min(tot,cntw,cntb)

n,m = map(int,input().split())
lst = []
tot = float('inf')
for i in range(n):
    lst.append(list(input()))
for i in range(n-7):
    for j in range(m-7):
        check(i,j)
print(tot)
#8*8배열을 골라 몇 개를 고쳐야 하는지 정하자