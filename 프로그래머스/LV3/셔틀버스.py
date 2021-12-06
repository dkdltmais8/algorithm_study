def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    start = 540
    # 2번 이상의 스쿨버스가 남아서 시간 별로 일찍 보낼 수 있는 크루들 보내버리기
    while n> 1:
        n -= 1
        for i in range(m):
            if int(timetable[0][:2])*60+int(timetable[0][3:5]) <= start:
                timetable.pop(0)
        start += t
    #1번의 스쿨버스만 남았을 때 남은 크루들 제거하기(시간은 고정)
    for i in range(m-1):
        if int(timetable[0][:2]) * 60 + int(timetable[0][3:5]) <= start:
            timetable.pop(0)
    #마지막 남은 놈보다는 일찍 타야할 때
    if (len(timetable)>0) and (int(timetable[0][:2])*60+int(timetable[0][3:])) <=start:
        answer = timetable[0]
        if answer[-2:] == "00":
            answer = str(int(answer.split(":")[0]) - 1).zfill(2) + ":59"
        else:
            answer = answer.split(":")[0].zfill(2) + ":" + str(int(answer.split(":")[1]) - 1).zfill(2)
    #사람들 다 태우고도 자리가 남아서 제일 마지막에 갈 수 있을 때
    else:
        answer = str(start//60).zfill(2)+":"+str(start%60).zfill(2)
    print(answer)
    return answer
solution(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"])
solution(2	,10,	2,	["09:10", "09:09", "08:00"])
solution(2,	1,	2,	["09:00", "09:00", "09:00", "09:00"])