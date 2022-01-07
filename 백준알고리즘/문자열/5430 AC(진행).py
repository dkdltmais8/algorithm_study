from collections import deque
T = int(input())
for tc in range(1,T+1):
    p= input()
    n = int(input())
    Q = input()[1:-1].split(",")
    if n == 0:
        Q = deque()
    else:
        Q = deque(Q)
    cnt = 0
    flag = True
    for i in p:
        if i =='R':
           cnt += 1
        else:
            if len(Q)==0:
                print("error")
                flag = False
                break
            else:
                if cnt %2 == 0:
                    Q.popleft()
                else:
                    Q.pop()

    if cnt%2 and flag:
        Q.reverse()
        print("["+",".join(Q)+"]")
    elif not cnt%2 and flag:
        print("["+",".join(Q)+"]")
