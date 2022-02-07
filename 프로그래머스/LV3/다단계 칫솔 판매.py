from collections import defaultdict
def solution(enroll, referral, seller, amount):
    def send(now,tot):
        if now == '-' or tot<1:
            return
        money[now] += tot - (tot//10)
        send(dic[now],tot//10)
    answer = []
    dic = defaultdict(str)
    money = defaultdict(int)
    for i in range(len(enroll)):
        dic[enroll[i]] += referral[i]
    for i in range(len(seller)):
        send(seller[i],amount[i]*100)
    for i in range(len(enroll)):
        answer.append(money[enroll[i]])
    return answer
solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	,["young", "john", "tod", "emily", "mary"],	[12, 4, 2, 5, 10])