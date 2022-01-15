for tc in range(int(input())):
    n = int(input())
    lst = [0,0,0,0,0]
    s,t,o = n//60,(n%60)//10,n%10
    if o>5:
        t += 1
        o-= 10
    if t> 3:
        s += 1
        t -= 6
    if t<0 and o == 5:
        t += 1
        o -= 10
    lst[0] = s
    lst[2-(t>=0)] = abs(t)
    lst[4-(o>=0)] = abs(o)
    print(*lst)
