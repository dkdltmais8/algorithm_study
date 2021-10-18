def solution(price, money, count):
    answer = -1
    cal = 0
    for i in range(1,count+1):
        cal += price*i
    if money > cal:
        answer = 0
    else:
        answer = cal-money
    return answer
solution(3,20,4)