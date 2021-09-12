import math
def solution(fees, records):
    answer = []
    lst = []
    def pay(num):
        if num <= basetime:
            return basefee
        else:
            return basefee+(math.ceil((num-basetime)/addtime))*addfee if (num-basetime)//addtime >0 else basefee+(((num-basetime)//addtime+1))*addfee
    def calculate(timein,timeout):
        a,b = timein.split(':')
        c,d = timeout.split(':')
        a,b,c,d = int(a),int(b),int(c),int(d)
        if d-b < 0:
            c -= 1
            d += 60
        return (c-a)*60 + (d-b)
    basetime = fees[0]
    basefee = fees[1]
    addtime = fees[2]
    addfee = fees[3]
    for i in records:
        i = i.split(' ')
        lst.append(i)
    lst.sort(key=lambda x: x[1])
    # print(lst)
    for i in range(len(lst)):
        if i == len(lst)-1 and lst[i][2] == 'IN':
            lst.append(['23:59', lst[i][1], 'OUT'])
        if lst[i][2] == 'IN' and lst[i+1][2] !='OUT':
            lst.append(['23:59', lst[i][1], 'OUT'])
    lst.sort(key=lambda x: x[1])
    # print(lst)
    fee = [0]*9999
    for i in range(0,len(lst),2):
        fee[int(lst[i][1])] += calculate(lst[i][0],lst[i+1][0])
    # print(fee)
    for i in fee:
        if i ==0:
            continue
        answer.append(pay(i))
    print(answer)
    return answer
solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10],	["00:00 1234 IN"])