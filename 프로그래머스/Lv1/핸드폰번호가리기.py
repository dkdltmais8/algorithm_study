def solution(phone_number):
    answer = ''
    d = len(phone_number)
    for i in range(d):
        if i<d-4:
            answer+='*'
        else:
            answer+=phone_number[i]
    return answer