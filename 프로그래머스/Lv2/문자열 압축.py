def solution(s):
    answer = 0
    if len(s) == 1:
        return 1
    d = len(s)
    for j in range(1,d//2+1):
        lst = ''
        cnt = 0
        for i in range(0,d,j):
            now = s[i:i+j]
            next = s[i+j:i+j*2]
            before = []
            if i-j >=0:
                before = s[i-j:i]
            if now == next:
                cnt += 1
                # continue
            else:
                if before !=[] and before == now:
                    cnt += 1
                    lst += str(cnt)+now
                    cnt = 0
                else:
                    lst += now
                    # continue
        if answer == 0:
            answer = len(lst)
        else:
            answer = min(answer,len(lst))

    return answer