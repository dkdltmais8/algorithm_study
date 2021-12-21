n = int(input())
num = list(map(int,input().split()))
#각 면에 대칭인 면과 비교해서 작은 것을 앞으로 오게 하기.(a와 b중에 하나를 고를 수 없고 a와 f가 만남)
lst = []
for i in range(0,3):
    lst.append(min(num[i],num[5-i]))
lst.sort()
tot = 0
#주사위가 1개면 제일 큰수를 뺴고 더하기
if n ==1:
    tot = sum(num)-max(num)
#3면이 보이는 주사위 = 4 한면당 위 모서리 한개
#2면이 보이는 주사위 = 8n-12 한면당 (n-2)+(n-1)
#1면이 보이는 주사위 = 4*(n-2)가로*(n-1)세로+(n-2)**2윗면의 정사각형
else:
    tot += lst[0]*(4*(n-2)*(n-1)+(n-2)**2)
    tot += (lst[0]+lst[1])*((8*n)-12)
    tot += (lst[0]+lst[1]+lst[2])*4
print(tot)

