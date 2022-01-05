def check(num):
    a = str(num)
    for i in a:
        num += int(i)
    if num == n:
        return True
    else:
        return False
def cal(num):
    global answer
    ans = num
    a = str(num)
    for i in a:
        num -= int(i)
    if check(num):
        cal(num)
    else:
        answer = ans
n = int(input())
answer= 0
tmp = n
cal(tmp)
print(answer)