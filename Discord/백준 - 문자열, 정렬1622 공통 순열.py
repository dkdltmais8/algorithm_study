from collections import defaultdict
while 1:
    try:
        a = input()
        b = input()
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        ans = []
        for i in a:
            cnt1[i] += 1
        for i in b:
            cnt2[i] += 1
        for i in cnt1:
            if i in cnt2:
                for j in range(min(cnt1[i],cnt2[i])):
                    ans.append(i)
        print(''.join(sorted(ans)))
    except:
        break