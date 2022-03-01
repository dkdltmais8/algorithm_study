#밑장을 빼서 상대에게도 줄 수 있음
#밑장을 빼면 분배 순서가 바뀜
#밑장 빼기는 1번
n = int(input())
lst = list(map(int,input().split()))
#밑장 빼기를 안 했을 때 내 합
me = sum(lst[0::2])
#최종 답
ans = me
#비교하기 위한 변수
tot = me
#마지막 인덱스가 내 패이니까 그 패를 더해주고 그 전 패를 지운다.
for i in range(n-1,0,-2):
    tot += lst[i]
    tot -= lst[i-1]
    ans = max(tot,ans)
#상대 차례 때 밑장 빼기
tot = me
#마지막 인덱스가 상대방 패이니까 그 전을 뺴고 그 전전을 더해준다.
for i in range(n-2,1,-2):
    tot -= lst[i]
    tot += lst[i-1]
    ans = max(tot,ans)
print(ans)

