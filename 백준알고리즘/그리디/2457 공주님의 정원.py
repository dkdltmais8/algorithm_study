import sys
input = sys.stdin.readline
n = int(input())
day =[]
for i in range(n):
    fake = list(map(int,input().split()))
    day.append([fake[0]*100+fake[1],fake[2]*100+fake[3]])
day.sort(key=lambda x:(x[0],x[1]))
cnt = 0
now = 301
end = 0
while day:
    #현재 12월1일이면 성공이니까 종료 남은 꽃의 시작일보다 현재가 작다면 중간에 끊기기 떄문에 실패로 종료
    if now >= 1201 or now < day[0][0]:
        break
    #꽃을 반복하면서 현재(종료시점)보다 같거나 작은 시작일이 있고 더 긴 종료일이 있다면 그것으로 바꿔주고 기존의 꽃은 삭제
    for _ in range(len(day)):
        if now>=day[0][0]:
            if end<day[0][1]:
                end = day[0][1]
            day.remove(day[0])
        else:
            break
    #첫번째 시작 날짜에 종료 날짜를 넣어준다.
    now = end
    #바꿨으니까 꽃 1개 추가
    cnt += 1
#종료시점이 11월30일 이하이면 꽃이 11월30일이전에 사라지므로 실패
if now<1201:
    print(0)
else:
    print(cnt)