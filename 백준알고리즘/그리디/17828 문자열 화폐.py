n,x = map(int,input().split())
if n*26<x or n>x:
    print('!')
else:
    basic = ['A']*n
    x -= n
    idx = n-1
    while x>0:
        if x>=25:
            basic[idx] = 'Z'
            idx-=1
            x -= 25
        else:
            basic[idx] = chr(65+x)
            break
    print(''.join(basic))
