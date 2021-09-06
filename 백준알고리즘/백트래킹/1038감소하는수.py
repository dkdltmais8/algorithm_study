def main(n):
    cnt = 0
    num = 1
    while 1:
        str_num = str(num)
        flag = True
        if len(str_num)== 1:
            pass
        else:
            for i in range(1,len(str_num)):
                if int(str_num[i]) < int(str_num[i-1]):
                    continue
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1
n = int(input())
if n> 1022:
    print(-1)
elif n==0:
    print(0)
else:
    print(main(n))
