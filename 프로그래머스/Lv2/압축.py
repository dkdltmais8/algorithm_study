def solution(msg):
    answer = []
    dic = {}
    j = 27
    for i in range(65,91):
        dic[chr(i)] = i-64
    while msg:
        start = 1
        while msg[:start] in dic.keys() and start <= len(msg):
            start += 1
        start -=1
        answer.append(dic[msg[:start]])
        dic[msg[:start+1]] = j
        j += 1
        msg = msg[start:]
    return answer
solution("KAKAO")

