def solution(play_time, adv_time, logs):
    def realtime(time):
        h,m,s = time.split(':')
        return int(h)*3600 + int(m)*60 + int(s)
    def faketime(time):
        h = time // 3600
        h = '0' + str(h) if h < 10 else str(h)
        time = time % 3600
        m = time // 60
        m = '0' + str(m) if m < 10 else str(m)
        time = time % 60
        s = '0' + str(time) if time < 10 else str(time)
        return h + ':' + m + ':' + s

    play_time = realtime(play_time)
    adv_time = realtime(adv_time)
    time = [0 for i in range(play_time + 1)]
    for i in logs:
        s,e = i.split('-')
        s = realtime(s)
        e = realtime(e)
        time[s]+=1
        time[e]-=1
    for i in range(1,len(time)):
        time[i] += time[i-1]
    for i in range(1,len(time)):
        time[i]+= time[i-1]
    p = 0
    ans = 0
    for i in range(adv_time-1,play_time):
        if i >= adv_time:
            if p < time[i]-time[i-adv_time]:
                p = time[i]-time[i-adv_time]
                ans = i-adv_time+1
        else:
            if p < time[i]:
                p = time[i]
                ans = i - adv_time + 1
    return faketime(ans)
solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])