def change(m):
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    return m
def solution(m, musicinfos):
    answer = []
    m = change(m)
    for i in musicinfos:
        s,e,t,p= i.split(',')
        sh,sm,eh,em = map(int,s.split(":")+e.split(":"))
        d = 60*(eh-sh)+ em-sm
        p = change(p)
        check = (p*d)[:d]
        if m in check:
            answer.append((t,d,s))
    answer.sort(key=lambda x:(-x[1],x[2]))

    if answer:
        return answer[0][0]
    else:
        return "(None)"
# solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("ABC",	["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("CC#BCC#BCC#BCC#B"	,["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])