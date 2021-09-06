def sizecomp(a,b):
    if abs(ord(a)-ord(b)) > 13:
        if ord(a) > ord(b):
            return (26-ord(a)+ord(b))*-1
        else:
            return (-26-ord(a)+ord(b))*-1
    elif abs(ord(a)-ord(b)) == 13:
        return -13
    else:
        if ord(a) > ord(b):
            return ord(b)-ord(a)
        else:
            return ord(a)-ord(b)

def direct(i,num):
    if i == 1:
        if num >= 0:
            return ( num * 1)
        else:
            return (num * -1)
    elif num >= 0 and i == 2:
        return (num * 3)
    elif num < 0 and i == 2:
        return (num * -2)
    elif num >= 0 and i == 3:
        return (num * 5)
    elif num < 0 and i == 3:
        return (num * -4)
    elif num >= 0 and i == 4:
        return (num * 7)
    elif num < 0 and i == 4:
        return (num * -6)

for tc in range(1, int(input())+1):
    first = input()
    ans = input()
    res = 0
    for i in range(4):
        res += direct(i+1,sizecomp(first[i],ans[i]))
        print(res,tc)
    print(res)
