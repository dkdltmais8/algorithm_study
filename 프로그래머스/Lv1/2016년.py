def solution(a, b):
    answer = ''
    day =  ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    cnt = 0
    for i in range(a):
        for j in range(month[i]):
            cnt += 1
            if i == a-1:
                if j == b-1:
                    break
    answer = day[(cnt-1)%7]
    return answer
solution(5,24)
solution(1,1)
solution(1,2)