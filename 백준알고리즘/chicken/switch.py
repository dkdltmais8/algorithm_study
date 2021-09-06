#전구 개수
n = int(input())
#전구 스위치 계산을 편하게 하기위해 앞에 임의로 0 붙임
s = [0]+input().split()

#학생 수 대로 반복
student = int(input())
for _ in range(student):
    sex, on_off = input().split()
    i = int(on_off)
    if sex == '1':

        while(i < n +1):
            if s[i] == '1':
                s[i] = '0'
            elif s[i] =='0':
                s[i] = '1'
            i += int(on_off)
    else:
        if s[i] == '1':
            s[i] = '0'
        elif s[i] == '0':
            s[i] = '1'
        j = 1
        while (i - j > 0 and i+j < n + 1 and s[i+j] == s[i-j]):
            if s[i-j] == '1':
                s[i+j] = '0'
                s[i-j] = '0'
            elif s[i-j] == '0':
                s[i+j] = '1'
                s[i-j] = '1'
            j += 1
for k in range(1,n+1,20):
    print(*s[k:k+20])