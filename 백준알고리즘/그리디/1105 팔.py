l,r = map(int,input().split())
L,R = str(l),str(r)
cnt = 0
tot1,tot2 = 0,0
if len(L) != len(R):
    print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == '8':
                cnt += 1
        else:
            break
    print(cnt)


