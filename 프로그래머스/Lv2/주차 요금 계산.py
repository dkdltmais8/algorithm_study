import math
def cal(lst,fees):
    bt, bf, at, af = fees
    n = len(lst)
    tot = 0
    for i in range(1,n,2):
        h1 = int(lst[i][0:2])
        h2 = int(lst[i-1][0:2])
        m1 = int(lst[i][3:5])
        m2 = int(lst[i-1][3:5])
        tot += (h1-h2)*60 + m1-m2
    if tot>bt:
        ans = bf + math.ceil((tot-bt)/at)*af
    else:
        ans = bf
    return ans

def solution(fees, records):
    answer = []
    for i in range(len(records)):
        records[i] = records[i].split(' ')
    records.sort(key=lambda x:x[1])
    dic = dict()
    for i in records:
        if i[1] not in dic:
            dic[i[1]] = [i[0]]
        else:
            dic[i[1]].append(i[0])
    for i in dic.items():
        if len(i[1])%2:
            i[1].append("23:59")
    for i in dic.values():
        answer.append(cal(i,fees))
    # print(answer)
    return answer
solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
#기본 시간 180
#기본 요금 5000 ( 0~180분 까지 5000원) -> 전체 시간으로 확인
#1~10분사이 600원 추가
#차량 번호가 작은 자동차부터 가격 출력
#출차 기록이 없으면 23:59에 출차한것으로 간주
