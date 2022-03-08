def check(n):
    global answer
    if n == 0:
        return
    while n>0:
        if n%2 == 1:
            answer = "FUCK"
            break
        if n>=4:
            n-=4
            answer += 'AAAA'
        if n == 2:
            n -= 2
            answer +='BB'
    return
a = input()
cnt = 0
answer = ""
for i in a:
    if i =='X':
        cnt += 1
    else:
        check(cnt)
        if answer == 'FUCK':
            break
        answer += '.'
        cnt = 0
check(cnt)
print(answer if answer != "FUCK" else -1)