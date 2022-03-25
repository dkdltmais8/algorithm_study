for i in range(int(input())):
    a = input()
    now = a[0]
    flag = True
    for j in a:
        if now not in ('A','B','C','D','E','F'):
            print('Good')
            flag = False
            break
        if now == 'A':
            if j !='A' and j != 'F':
                print('Good')
                flag = False
                break
        elif now == 'F':
            if j != 'F' and j != 'C':
                print('Good')
                flag = False
                break
        elif now == 'C':
            if j != 'C' and j not in ('A','B','C','D','E','F'):
                print('Good')
                flag = False
                break
        now = j
    if flag:
        print('Infected!')