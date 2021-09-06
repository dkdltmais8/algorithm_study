t = int(input())
answer = ''
for tc in range(1, t+1):
    string = input()
    alpha = dict(zip(set(string), [0] * len(set(string))))
    for i in string:
        alpha[i] += 1
    alpha = sorted([alphabet for alphabet in alpha if alpha[alphabet] % 2])
    if len(alpha) == 0:
        answer += "#{} Good\n".format(tc)
    else:
        answer += "#{} {}\n".format(tc, ''.join(alpha))
print(answer)