l,w,h = map(int,input().split())
n = int(input())
cube = []
for _ in range(n):
    a,b = map(int,input().split())
    cube.append([2**a,b])
v = l*w*h
#실제 큐브의 개수
cnt = 0
#큐브의 크기에 따라 개수를 변화시킬 변수
tot = 0
for i in range(n-1,-1,-1):
    #큐브의 크기가 1/8로 줄어들기 때문에 개수를 8배로 늘려주면 마지막 큐브(제일 작은 1큐브)에서의 개수가 부피와 같음
    tot <<= 3
    #현재 큐브 한변의 길이
    cl = cube[i][0]
    #갖고 있는 큐브의 개수와 전체를 현재 큐브로 채우는 개수 - 전의 넣은 큐브(개수*8을 해줬기 때문에 같은 크기로 비교)
    #작은 값 => 실제로 넣을 수 있는 값
    cnt += min((l//cl)*(w//cl)*(h//cl)-tot,cube[i][1])
    tot += min((l//cl)*(w//cl)*(h//cl)-tot,cube[i][1])
    print(cnt,tot)
if tot != v:
    print(-1)
else:
    print(cnt)